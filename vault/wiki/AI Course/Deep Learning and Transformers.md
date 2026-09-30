---
title: "Deep Learning and Transformers"
source_id: "agentic-ai-notes"
source_file: "raw/Agentic AI Course Notes.md"
source_sections: ["Class 4: Deep learning, embeddings and transformers"]
source_sha256: "8636ad7ce14a6322a8145981eb5902dd2eddf9f1c4f231e237f6aac98fc880d2"
generated_by: "mlx-community/gemma-4-e2b-it-4bit"
generated_at: "2026-09-29T20:01:13"
---

# Deep Learning and Transformers

## Summary

Deep learning involves using adjustable weights and biases in neural networks to convert input numbers into output numbers. Training involves repeating moves to predict examples, measure loss, and adjust parameters using gradients computed by backpropagation. Transformers utilize attention mechanisms to connect tokens, and language models are often pretrained by predicting the next token on large amounts of text.

## Key points

- A neuron combines weighted inputs with a bias and passes the result through an activation function.
- Training repeats three moves: predict on examples, measure the loss, and adjust parameters using gradients computed by backpropagation.
- Mini batches average the gradient over a small group of examples, and an epoch is a full pass over the data.
- Embeddings are learned vectors that represent a word or token, where similar meanings end up near each other.
- Attention gives each token direct connections to earlier positions through query, key and value computations.
- A transformer stacks blocks of self attention and feed forward networks, including residual connections, positional information for word order, and multi head attention.
- Causal masking stops a position from seeing future tokens, which allows parallel training and honest generation.
- Foundation models are pretrained by predicting the next token trillions of times on internet text, and fine tuning then adapts them to specific tasks.
- The custom nanoGPT has 2 blocks, 4 attention heads, 64 number embeddings, a 48 token context window, batches of 32, and about 100 thousand parameters.
- The nanoGPT was trained from random weights on a classroom corpus of about 4,600 sentences using about 133 distinct words, and the corpus is never consulted again after training.

## Related notes

- [[Machine Learning Foundations]]: This note covers the foundational concepts necessary to understand the machine learning aspects mentioned in the first note.
- [[LLM Prompting and RAG]]: This note details how to interact with and build upon large language models, which is a direct application of the transformer concepts.

## Sources

- [[Agentic AI Course Notes]], section "Class 4: Deep learning, embeddings and transformers"
