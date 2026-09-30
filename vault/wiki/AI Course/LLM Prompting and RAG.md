---
title: "LLM Prompting and RAG"
source_id: "agentic-ai-notes"
source_file: "raw/Agentic AI Course Notes.md"
source_sections: ["Class 5: LLM behavior, prompting and retrieval"]
source_sha256: "8636ad7ce14a6322a8145981eb5902dd2eddf9f1c4f231e237f6aac98fc880d2"
generated_by: "mlx-community/gemma-4-e2b-it-4bit"
generated_at: "2026-09-29T20:01:17"
---

# LLM Prompting and RAG

## Summary

This topic covers various aspects of Large Language Model (LLM) behavior, including token prediction, model training methods, prompting techniques, context window limitations, and retrieval methods like RAG. It also discusses issues like hallucination and deployment considerations for local models.

## Key points

- Temperature controls sampling randomness: lower favors likely continuations, higher adds variety.
- Model behavior is achieved through three stages: pretraining on internet text, supervised fine tuning on instruction and response pairs, and reinforcement learning from human feedback (RLHF) using preference data.
- Prompting involves including the audience and purpose, background facts, constraints, the deliverable, and a clear ask, with detail reshaping the probability distribution toward useful answers.
- Large models can accept huge contexts, but larger contexts increase cost and latency, and "lost in the middle" effects can still bury details.
- RAG retrieves relevant passages from own sources and supplies them as context without retraining, with an enterprise usage rate of roughly 86 percent.
- Local model deployment requires a runtime and quantization; for example, 4 bit storage uses about 75 percent less memory than 16 bit.

## Related notes

- [[Deep Learning and Transformers]]: This is a foundational concept related to the underlying models used in LLMs.
- [[Production LLMs and Agents]]: This discusses the deployment and practical application of LLMs, connecting to prompting.

## Sources

- [[Agentic AI Course Notes]], section "Class 5: LLM behavior, prompting and retrieval"
