---
title: "Machine Learning Foundations"
source_id: "agentic-ai-notes"
source_file: "raw/Agentic AI Course Notes.md"
source_sections: ["Class 3: Machine learning foundations"]
source_sha256: "8636ad7ce14a6322a8145981eb5902dd2eddf9f1c4f231e237f6aac98fc880d2"
generated_by: "mlx-community/gemma-4-e2b-it-4bit"
generated_at: "2026-09-29T20:01:09"
---

# Machine Learning Foundations

## Summary

Machine learning involves different learning paradigms such as supervised, unsupervised, and reinforcement learning. The process of fitting a model involves adjusting parameters using gradient descent, and training data is used to fit these parameters. Model evaluation involves metrics like precision and recall, and concepts like generalization and distribution shift are important for assessing model performance.

## Key points

- Three learning paradigms are: Supervised learning, which learns from input and answer pairs; Unsupervised learning, which finds structure in inputs alone; and Reinforcement learning, where an agent collects rewards from an environment to learn a policy.
- Parameters start arbitrary and move by gradient descent; the loss measures prediction errors, the gradient points downhill, and the learning rate sets the step size.
- Training fits parameters on historical labeled data, while inference applies the frozen model to new cases without retraining.
- Overfitting occurs when fitting noise, and regularization constrains complexity to prevent overfitting.
- Evaluation metrics include Precision (TP / (TP + FP)) and Recall (TP / (TP + FN)), which measure how many flagged cases were correct and how many real cases were caught.
- Distribution shift causes prediction failures when new inputs stop resembling training data, such as moving a digit sideways collapsing accuracy.

## Related notes

- [[Deep Learning and Transformers]]: This note covers advanced deep learning architectures, which are often used in modern ML models.
- [[LLM Prompting and RAG]]: This note covers prompting techniques for Large Language Models, a modern application area.

## Sources

- [[Agentic AI Course Notes]], section "Class 3: Machine learning foundations"
