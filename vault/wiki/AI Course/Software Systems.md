---
title: "Software Systems"
source_id: "agentic-ai-notes"
source_file: "raw/Agentic AI Course Notes.md"
source_sections: ["Class 2: Software systems, from frontend to deployment"]
source_sha256: "8636ad7ce14a6322a8145981eb5902dd2eddf9f1c4f231e237f6aac98fc880d2"
generated_by: "mlx-community/gemma-4-e2b-it-4bit"
generated_at: "2026-09-29T20:01:06"
---

# Software Systems

## Summary

This section describes the five layers of a web application, the role of APIs, database operations, authentication, secrets management, and deployment processes. It details how different parts of a system interact and the security considerations involved in data handling and production hosting.

## Key points

- The five layers of a web application include Frontend, Backend, Database, Secrets and identity, and Cloud deployment.
- APIs use an analogy where tables are frontends, waiters are APIs, and the kitchen is the backend, with HTTP verbs carrying intent (GET, POST, PUT, DELETE).
- Databases use tables of records linked by one to one, one to many, or many to many relationships, and SQL filters, joins, sorts, and aggregates.
- Authentication proves who you are, while authorization decides what you may touch.
- Secrets like API keys and passwords must not appear in committed code, with local secrets in .env.local and production secrets in host's environment variables.
- CI/CD pipelines run tests on every change and block deployment when tests fail, and regression tests catch breakage in distant parts of the system.

## Related notes

- [[Code Foundations]]: This note likely provides the foundational knowledge needed to understand the system's underlying structure.
- [[AI Tools for Excel]]: This might relate to how data is processed or modeled within the system's operations.

## Sources

- [[Agentic AI Course Notes]], section "Class 2: Software systems, from frontend to deployment"
