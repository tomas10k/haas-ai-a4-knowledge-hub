# Agentic AI Course Notes

My personal study notes for MBA 290T, Fundamentals of Agentic AI ("From Zero to AI Agents"), Berkeley Haas, Fall 2026. Covers Classes 1 to 6, written from the class slides on the course site and my own class summaries. These notes paraphrase the material in my own structure; they are not a copy of the slides.

## Course schedule

| Class | Date | Topic | Assignment |
|---|---|---|---|
| 1 | Tue Aug 25, 2026 | Code and programming foundations | |
| 2 | Tue Sep 1, 2026 | Software systems, frontend to deployment | Assignment 1 assigned (discount engine), due Sep 8 |
| 3 | Tue Sep 8, 2026 | Machine learning foundations | Assignment 2 (Pac Man DQN and MNIST), due Sep 15 |
| 4 | Tue Sep 15, 2026 | Deep learning, embeddings and transformers | Assignment 3 (custom nanoGPT), due Sep 22 |
| 5 | Tue Sep 22, 2026 | LLM behavior, prompting and retrieval | Assignment 4 (personal wiki with local Gemma and RAG), due Sep 29 |
| 6 | Tue Sep 29, 2026 | Production LLMs and single agents | Assignment 5 part 1 (enrichment agent) |
| 7 | Tue Oct 6, 2026 | Multi agent systems, ops and safety | Assignment 5 (insight pipeline), due Oct 13 |

Assignments 1 to 4 are due one week after they are assigned, at 11:59 pm PT. Assignment 5 spans Classes 6 and 7 and has one submission on Tuesday October 13 at 11:59 pm PT. Every assignment is graded on the same framework: deliverable quality (4 points), testing and evaluation (3 points), and working result (3 points), for 10 points total.

## Class 1: Code and programming foundations

**Why code literacy matters for an MBA.** AI writes more and more of the code, but people still steer it: they review AI generated work, evaluate vendors, debug production issues, and manage engineers. Without literacy you ship insecure prototypes, leak API keys, or run experiments against production data instead of a copy.

**What code is.** A precise recipe with three parts: input, processing, output. Turning a fuzzy business policy ("give loyal customers a discount") into exact rules (what counts as loyal, what percent, which exceptions) is most of what programming actually is.

**How code runs.** Everything ends up as binary. Interpreted languages such as Python and JavaScript are translated line by line as they run; compiled languages such as C, Go and Rust are translated fully before running. Python is recommended for readability and AI support, JavaScript is essential for the web, and SQL is a high return skill for querying data.

**The four building blocks.** Variables hold data of a type (number, string, boolean, list, dictionary). Conditionals make decisions. Loops repeat work over collections. Functions package reusable logic behind a name, with inputs and a return value.

**Three kinds of error.**

| Error | What happens | Why it matters |
|---|---|---|
| Syntax error | The code cannot even be read | Caught immediately |
| Runtime error | The code starts, then crashes | Visible, so it gets fixed |
| Logic error | The code runs and returns a confident wrong answer | The most dangerous, because nothing complains |

**Clean code.** Readability beats cleverness. One job per function, names that state intent (monthly_revenue rather than x), named constants instead of magic numbers, guard clauses instead of deep nesting, and comments that explain why rather than what. Organize projects by feature, with layers such as routers, services, repositories and models, so each file has one reason to change.

**Git and GitHub.** A commit is a named, reviewable snapshot of a coherent change, not just a save. A branch is a parallel version for experimenting. A diff shows the exact lines added and removed. A pull request proposes a change with the review conversation around it. Typical flow: pull, branch, write, add and commit, push, open a pull request, merge. Never commit secrets; that is what .gitignore is for.

**Localhost and the terminal.** localhost (127.0.0.1) is your own machine, and requests to it never touch the internet. Ports are like apartment numbers at one address, for example 3000, 8000 and 5432. A website is a running process, not a file: close the terminal and the site stops. A localhost link means nothing to anyone else. Terminal grammar is program, action, flag, argument, with basic commands such as pwd, ls, cd and mkdir.

**AI coding agents.** Tools such as Claude Code and Codex read the codebase, write files, run commands and iterate. Plan mode drafts an approach for review before any file changes. Skipping permission prompts is acceptable for a brand new project and reckless in production. Before accepting an agent's diff, check that it matches the brief, has no unexpected files, keeps secrets in environment variables, passes the tests, and can be explained out loud.

**Assignment 1, the discount engine.** Rules: standard tier 5 percent, gold 10 percent, strategic 15 percent; any invoice more than 90 days overdue gets 0 percent unless an exception is approved; no discount may exceed $25,000. Business rules had to be separated from the data and web layers, covered by passing unit tests, served on localhost, and built after using plan mode.

## Class 2: Software systems, from frontend to deployment

**The five layers of a web application.**

1. Frontend: the interface in the browser, usually built with component frameworks such as React and Next.js and component libraries such as shadcn/ui.
2. Backend: business logic, access control and the single source of truth.
3. Database: persistent storage.
4. Secrets and identity: authentication and authorization.
5. Cloud deployment: production hosting on a public URL.

**APIs.** The restaurant analogy: tables are frontends, waiters are APIs, and the kitchen is the backend. The frontend never reaches into the kitchen. HTTP verbs carry intent: GET reads, POST creates, PUT updates, DELETE removes. Data travels as JSON. The backend treats every request as potentially hostile and validates it, even if the frontend already did.

**Databases.** Tables of records with consistent columns, linked by one to one, one to many, or many to many relationships. SQL filters, joins, sorts and aggregates. Push heavy data work down the stack: filter a million rows in the database rather than in the browser. Relational databases such as PostgreSQL are the default.

**Authentication versus authorization.** Authentication proves who you are; authorization decides what you may touch. Typical flow: the frontend sends credentials, the backend returns a token, the frontend attaches the token to later requests, and the backend verifies it before returning protected data. Row level security makes the database itself enforce that a row belongs to a user, which is real protection rather than hiding data in the interface.

**Secrets.** API keys, passwords and tokens never appear in committed code or in frontend JavaScript. Local secrets live in .env.local; production secrets live in the host's environment variables. A leaked key must be revoked immediately.

**Deployment.** The cloud is someone else's computers in a data center. CI/CD pipelines run tests on every change and block the deploy when tests fail. Regression tests catch breakage in distant parts of the system.

**Assignment 2 context, the networking tracker.** A Next.js, Supabase and Vercel app for tracking people met at Berkeley, with sign in, create, read, update and delete for contacts, per user privacy enforced by row level security, graceful input errors, at least one automated test, and a live public URL.

## Class 3: Machine learning foundations

**Three learning paradigms.** Supervised learning learns from input and answer pairs. Unsupervised learning finds structure in inputs alone. Reinforcement learning has an agent collect rewards from an environment and learn a policy.

**Fitting a model.** Parameters start arbitrary and move by gradient descent. The loss measures how wrong predictions are, the gradient points downhill, and the learning rate sets the step size. Classification predicts a category; regression predicts a number.

**Training versus inference.** Training fits parameters on historical labeled data. Inference applies the frozen model to new cases, and making predictions does not retrain it.

**Generalization.** Training data fits the parameters, validation data chooses settings and model family, and test data stays untouched until the end to estimate real performance. Overfitting means fitting noise. Too rigid a model underfits and too flexible a model overfits; regularization constrains complexity.

**Model families.** Logistic regression passes a weighted sum through a sigmoid to get a probability. k nearest neighbors votes among the most similar labeled examples. Decision trees learn yes or no questions, and deeper trees overfit. Random forests vote across many trees to reduce variance.

**Evaluation.** The confusion matrix counts true positives, false positives, false negatives and true negatives. Precision = TP / (TP + FP): of the cases flagged, how many were right. Recall = TP / (TP + FN): of the real cases, how many were caught. Accuracy can hide the error that matters when classes are imbalanced or error costs are asymmetric. The decision threshold trades precision against recall according to business cost.

**Unsupervised methods.** k means groups points around centroids, with k chosen by the analyst. PCA compresses correlated columns into fewer dimensions. Anomaly detection flags the unusual, which is not the same as the harmful.

**Reinforcement learning.** State is what the agent knows now, an action is a choice, a reward is feedback, and a policy maps states to actions. The objective is cumulative discounted future reward. Q(s, a) estimates the total discounted reward from taking action a in state s. Epsilon greedy explores randomly with probability epsilon and otherwise exploits the best known action. A Q table works for small state spaces; Pac Man pixels need a neural network to approximate Q, called a deep Q network. Reward design matters: the agent optimizes the reward, which is rarely exactly what you wanted.

**Distribution shift.** Predictions fail when new inputs stop resembling training data. In the MNIST shifted digit experiment, moving a digit sideways collapses accuracy, because the model learned which pixels predict each digit rather than the shape.

## Class 4: Deep learning, embeddings and transformers

**Neurons and training.** A neural network turns input numbers into output numbers using adjustable weights and biases. A neuron combines weighted inputs with a bias and passes the result through an activation function. Training repeats three moves: predict on examples, measure the loss, and adjust parameters using gradients computed by backpropagation. Loss can improve before accuracy does. Mini batches average the gradient over a small group of examples; an epoch is a full pass over the data.

**Depth.** Layers build a hierarchy: pixel values, simple patterns, combinations, prediction. Nonlinear activations let networks learn curved decision boundaries.

**Embeddings.** An embedding is a learned vector that represents a word or token, and similar meanings end up near each other. Word2Vec showed that king minus man plus woman lands near queen. Contextual representations shift meaning with surrounding words, so "bank" differs next to "river" versus "money."

**Attention and transformers.** Attention gives each token direct connections to earlier positions through query, key and value computations. A transformer stacks blocks of self attention and feed forward networks, with residual connections that add each block's output to its input, positional information for word order, and multi head attention that learns several relationship patterns in parallel. Causal masking stops a position from seeing future tokens, which allows parallel training and honest generation.

**Language model training.** Foundation models are pretrained by predicting the next token trillions of times on internet text, which needs no manual labels. Fine tuning then adapts them to specific tasks.

**Assignment 3, the custom nanoGPT.** A tiny word level transformer: 2 blocks, 4 attention heads, 64 number embeddings, a 48 token context window, batches of 32, about 100 thousand parameters, trained from random weights on a classroom corpus of about 4,600 sentences using about 133 distinct words. After training, the corpus is never consulted again; everything learned lives in the weights. Temperature only affects generation variety and never changes knowledge. A separate suite of 48 fixed evals acts as the exam, and training on the exam would fake a pass.

## Class 5: LLM behavior, prompting and retrieval

**Token prediction.** An LLM predicts the next token, appends it, and predicts again. The output is a probability distribution, so the same prompt can produce different answers. Temperature controls sampling randomness: lower favors likely continuations, higher adds variety.

**How models get their behavior.** Three stages: pretraining on internet text, supervised fine tuning on instruction and response pairs, and reinforcement learning from human feedback (RLHF) using preference data. Frontier pretraining costs over $100 million. Fine tuning changes weights, so it is expensive and permanent; prompting steers a frozen model, so it is cheap and reversible. LoRA adapters update roughly 0.1 to 1 percent of weights.

**The ladder of levers,** cheapest first: system prompt, few shot examples, RAG, LoRA fine tune, full fine tune, pretraining. Each rung costs roughly ten times the one above. Move down only when the rung above has demonstrably failed.

**Prompting.** A good prompt includes the audience and purpose, background facts, constraints, the deliverable, and a clear ask. Detail reshapes the probability distribution toward useful answers. System prompts carry instructions the user does not see, and files such as CLAUDE.md keep durable rules across conversations.

**Context windows.** Large models accept huge contexts (about 1 million tokens for Claude Opus, roughly two full Lord of the Rings trilogies), but larger contexts raise cost and latency, and "lost in the middle" effects can still bury details. The whole conversation is resent every turn, so long chats cost more per turn. Compaction summarizes old turns and is lossy. When a thread gets confused, start fresh.

**Thinking models.** Extended thinking generates intermediate reasoning before the answer. It helps hard problems at the cost of latency and tokens, but it cannot create facts the model never had.

**Hallucination.** Fluency is optimized, truth is not. Defenses: retrieval for grounding, citations, higher reasoning effort, and lower temperature where supported.

**RAG (retrieval augmented generation).** Retrieve relevant passages from your own sources and supply them as context without retraining. Pipeline: chunk documents, embed chunks and the question into vectors, search for the nearest chunks, inject them into the prompt, answer with citations. Keyword search and AI generated SQL are alternative retrieval methods. Roughly 86 percent of enterprises use RAG to connect AI to their data.

**Local models.** Open weights, open source and local deployment are different properties. Running Gemma locally needs a runtime (Ollama on Windows or Linux, MLX on Apple Silicon, CPU inference on Intel Macs) and quantization: 4 bit storage uses about 75 percent less memory than 16 bit. Download models and dependencies while online, then prove offline operation with the internet disconnected.

**Assignment 4, the personal wiki.** A terminal CLI with chat, ask, search, ingest and help commands over at least three original sources, using local Gemma and RAG, working fully offline, with three answerable test questions, one unsupported question, and Obsidian screenshots of the wiki.

## Class 6: Production LLMs and single agents

**Where an LLM lives.** Three options: call a model provider's API (quick start, managed capacity; tradeoffs are usage bills, lock in, and data handling terms), run the model on your own server (control and data containment; tradeoffs are hardware and reliability burden), or run it on a laptop (local experiments, limited by the device). Self hosting alone does not guarantee privacy; configuration matters. Choose by testing quality, latency, cost and data sensitivity on the real task.

**Budgets and failures.** Every run gets a budget enforced in code, not in the prompt. The illustrative policy: 6 tool calls, 30 seconds before fallback, and $0.10 per attempt, counting input and output tokens, retries and tool calls. Failure responses: retry transient outages and rate limits with increasing delays, fix invalid inputs, stop or escalate on permission denied, and check status before retrying a timed out write, because a timeout means you lost the answer, not that the action failed.

**Structured output.** Replace free text with explicit fields and types so software can read the result. A schema is the answer contract, for example topic (billing, technical, sales, other), severity (integer 1 to 5), needs_review (boolean), and evidence_quote (text from the source). Define labels and the rubric before writing the prompt. A valid schema does not guarantee a correct answer, so check before acting: the model proposes, code validates schema, evidence, ownership and permissions, and only then does the application act.

**Tool use and the agent loop.** A model requests an action by choosing a tool; the application runs it and returns the result into context. A tool call is a request, not permission. The agent loop repeats: read, choose a tool, inspect the result, decide the next step or stop. This observe, act, update pattern is called ReAct, in contrast to fixed workflows where code sets the sequence in advance.

**The harness.** The software around the model supplies context, runs tools, keeps state and enforces limits: "the model chooses, the harness controls execution." Project access does not mean every file is in the context window; tools define what is available, not what is read.

**Inside one agent.** Four parts, with a kitchen analogy: memory (recipes and the current order), planning (deciding what to do next), tools (knife, stove, ingredients), and the loop (cook, check, adjust, finish). State tracks goal, evidence, progress, remaining budget and permissions. Memory has three layers: the context window (the working desk), the session log (run history), and external stores (durable files and databases). Save what matters, retrieve what this step needs, discard stale scratch work.

**Stopping, permissions and review.** A loop needs an exit: task complete, time or spend exhausted, repeated tool failures, or missing evidence or permission. A state machine makes allowed transitions explicit. Permissions belong outside the prompt, through tool allowlists and permission checks; prompt isolation is not a security boundary. Human review requests should show the proposed action, reason, evidence and choices, and silence must never count as approval.

**Errors and idempotency.** Structured errors distinguish "nothing found" from "the tool broke." Idempotency means repeating an operation does not repeat its effect, achieved with an operation ID and a record of completed actions.

**Guardrails versus evals.** Evals measure how often the system succeeds on test cases; guardrails restrict what actions are allowed. "Stay under $10" needs a budget check in code.

**Code, classification or generation.** Exact rules go in code (totals, permissions, sorting, validation). Bounded judgment goes to a classification model, which picks from a fixed label set, for example Jev by TypeSafe, which returns a choice with probabilities. Open ended writing goes to a generative LLM. This mix is called "skeleton and spark": code is the skeleton, model calls are the spark.

**Case study: OpenClaw.** A personal agent behind a chat app: messaging channels connect through a self hosted gateway to an agent runtime with tools and persistent memory. Workspace instructions such as SOUL.md guide behavior but do not replace permission enforcement.

**Tools, MCP and skills.** A tool has a job description: purpose, inputs, constraints, result and failure modes, with the application enforcing the contract. Tool results are data and may contain mistakes or hostile instructions. Computer use (look, click, type) is for legacy systems without APIs. MCP (Model Context Protocol) is a shared connector standard providing tools, resources and prompts; the USB analogy describes standardization, not trust, and MCP does not replace authentication. A skill is a reusable playbook, for example a SKILL.md file in Claude Code; a skill guides behavior but grants no permission.

**Workflow patterns.** Chaining runs fixed steps in order. Routing uses a rule or classifier to pick a path. Evaluator and optimizer drafts, checks and revises within a round limit. A fixed workflow suits known steps; an agent loop suits paths that depend on discoveries. Use the simplest system that works: a function for a calculation, one model call to interpret one message, a workflow for a known process, an agent loop for an uncertain path, and a team only when coordinating independent work.

**Evaluations.** An eval is a repeatable check: fixed inputs, expected behavior, actual output, and failure reasons. Rerun evals after any prompt, model, tool or source change, and version prompts. Write the task contract first, then test awkward cases: ambiguity, missing evidence, and adversarial requests such as "ignore rules and refund me." Checkers: code for required fields and valid labels, a model judge for tone and relevance (compare it with human judgments first), and people for ambiguous or consequential calls. Start with 5 to 10 cases. Traces show where a run failed. Set the release acceptance rule before looking at the score.

**Eval tools.** A CSV and a small script for a few cases, an eval runner such as promptfoo to compare prompts or models, and a platform with datasets and traces for team investigation. The tool organizes the work; you still define what good means.

**Cost engineering.** Four levers: token budgeting (send less context, limit output), prompt caching (keep reusable context stable and put changing information after it), model routing (match the model to the task and escalate when needed), and batch processing (trade speed for lower cost when no one is waiting). Worked example at $3 per million input tokens and $15 per million output tokens: one support ticket with 7,000 input tokens ($0.0210) and 500 output tokens ($0.0075) costs $0.0285, so 10,000 tickets cost $285 in model spend. If 6,000 are resolved without a person, model cost per resolution is $0.0475. If quality drops and 500 more tickets need human handling at $6 each, that adds $3,000, far more than the $142.50 saved by halving the model bill. Measure cost per successful outcome, not cost per call.

**Assignment 5, the insight pipeline.** A subscription company faces rising churn and has one quarter's budget to fix onboarding, billing, performance or support quality. Inputs: about 10,000 customer feedback records covering 12 months, combined with account metadata (plan tier, tenure, monthly revenue, date), leading to one decision memo. Pipeline stages: ingest and deduplicate (code), enrich by labeling each record (the Class 6 agent), verify (code plus a verifier), group related complaints (code plus model), rank by impact (code, reproducible arithmetic), and recommend in a cited memo (model). Class 6 requirements: choose 6 to 10 topic labels, write a 1 to 5 severity rubric with examples, hand label a 50 record golden set, validate every output (retry an invalid one once, then quarantine it with a reason), run the enricher on a slice of about 500 records, report agreement with the golden set, and estimate the cost of the full 10,000 record run. Each enriched record keeps its source ID plus topic, intent, sentiment, severity, entities and an evidence quote that must exist in the original text. Nothing is submitted after Class 6; the combined submission is due Tuesday October 13 at 11:59 pm PT.
