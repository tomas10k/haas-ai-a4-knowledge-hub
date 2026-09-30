---
title: "Production LLMs and Agents"
source_id: "agentic-ai-notes"
source_file: "raw/Agentic AI Course Notes.md"
source_sections: ["Class 6: Production LLMs and single agents"]
source_sha256: "8636ad7ce14a6322a8145981eb5902dd2eddf9f1c4f231e237f6aac98fc880d2"
generated_by: "mlx-community/gemma-4-e2b-it-4bit"
generated_at: "2026-09-29T20:01:20"
---

# Production LLMs and Agents

## Summary

This section covers various aspects of production Large Language Models (LLMs) and agents, including deployment options, budget enforcement, structured output requirements, agent interaction patterns, and evaluation methods. It details how to manage LLM usage, define contracts for results, structure agent loops, and measure performance against defined criteria.

## Key points

- LLM deployment options include calling a model provider's API, running the model on a self-managed server, or running it on a laptop.
- Every run is enforced with a budget in code, detailing policies such as tool call limits, fallback times, and costs per attempt.
- Structured output replaces free text with explicit fields and types, where a schema serves as the answer contract.
- The agent loop follows a ReAct pattern where the model chooses a tool, the application runs it, and the result is fed back into the context.
- The harness controls execution by supplying context and running tools, with tools defining available capabilities rather than what is read from the context window.
- Evaluation involves repeatable checks using fixed inputs, expected behavior, actual output, and failure reasons, often utilizing tools like promptfoo or datasets for investigation.

## Related notes

- [[LLM Prompting and RAG]]: This details how to structure prompts and use Retrieval-Augmented Generation.

## Sources

- [[Agentic AI Course Notes]], section "Class 6: Production LLMs and single agents"
