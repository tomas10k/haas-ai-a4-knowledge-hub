"""Local Gemma through MLX: load once, generate text, and measure time and memory."""
import os
import re
import resource
import time

from . import config

# Never reach the internet at run time: the model must come from the local cache.
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")


class ModelUnavailable(RuntimeError):
    pass


def peak_memory_gb():
    """Peak memory MLX has used for the model on the GPU, in GB."""
    import mlx.core as mx
    getter = getattr(mx, "get_peak_memory", None) or getattr(getattr(mx, "metal", None), "get_peak_memory", None)
    return round(getter() / 1e9, 3) if getter else None


def process_peak_rss_gb():
    """Peak memory of the whole Python process (macOS reports bytes)."""
    return round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9, 3)


def strip_thinking(text):
    """Remove any 'thinking' block and end markers so only the answer is shown."""
    text = re.sub(r"<\|channel>thought.*?<channel\|>", "", text, flags=re.S)
    if "<|channel>thought" in text:        # thinking that never finished: no answer inside it
        text = text.split("<|channel>thought")[0]
    for marker in ("<end_of_turn>", "<turn|>", "<eos>"):
        text = text.replace(marker, "")
    return text.strip()


class LocalGemma:
    def __init__(self, model_id=config.MODEL_ID):
        try:
            from mlx_lm import load
        except ImportError as err:
            raise ModelUnavailable("mlx-lm is not installed. Activate the venv: source .venv/bin/activate") from err
        start = time.perf_counter()
        try:
            self.model, self.tokenizer = load(model_id)
        except Exception as err:
            raise ModelUnavailable(
                f"Could not load {model_id} from the local cache ({err}). "
                f"While online, download it once with: mlx_lm.generate --model {model_id} --prompt hi"
            ) from err
        self.model_id = model_id
        self.load_seconds = round(time.perf_counter() - start, 2)
        self.last = {}

    def build_prompt(self, messages):
        """Turn chat messages into Gemma's prompt format, with thinking switched off."""
        try:
            return self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        except Exception:
            # Fallback for templates without a system role: fold it into the first user turn
            if messages and messages[0]["role"] == "system":
                system, rest = messages[0]["content"], list(messages[1:])
                rest[0] = {"role": "user", "content": system + "\n\n" + rest[0]["content"]}
                messages = rest
            return self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    def generate(self, messages, max_tokens, temperature, raw=False):
        from mlx_lm import generate
        from mlx_lm.sample_utils import make_sampler

        prompt = self.build_prompt(messages)
        start = time.perf_counter()
        text = generate(self.model, self.tokenizer, prompt=prompt, max_tokens=max_tokens,
                        sampler=make_sampler(temp=temperature), verbose=False)
        seconds = time.perf_counter() - start
        output_tokens = len(self.tokenizer.encode(text))
        self.last = {
            "response_seconds": round(seconds, 2),
            "prompt_tokens": len(self.tokenizer.encode(prompt)),
            "output_tokens": output_tokens,
            "tokens_per_second": round(output_tokens / seconds, 1) if seconds else None,
            "peak_model_memory_gb": peak_memory_gb(),
            "process_peak_rss_gb": process_peak_rss_gb(),
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        return text if raw else strip_thinking(text)
