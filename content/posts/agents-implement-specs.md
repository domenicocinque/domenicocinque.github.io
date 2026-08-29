---
title: Let agents implement specifications rather than infer them
date: Aug, 2026
---

Since AI-assisted coding became mainstream, developers have debated how to work effectively with coding agents. One especially heated topic is how closely programmers should inspect AI-generated code. I believe part of the disagreement comes from a misunderstanding about what we are delegating to the agent.


<blockquote class="twitter-tweet" data-theme="dark"><p lang="en" dir="ltr">Control the ideas, not the code: blog post here <a href="https://t.co/RLjVUvGWVX">https://t.co/RLjVUvGWVX</a></p>&mdash; antirez (@antirez) <a href="https://x.com/antirez/status/2076634907049164891?ref_src=twsrc%5Etfw">July 13, 2026</a></blockquote> <script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>


These discussions often blur two different tasks:

- deciding what the software should do;
- implementing those decisions.

I will refer to the first as *specification*, denoted by $S$. It encompasses the collection of requirements, constraints, assumptions, and design decisions that determine what counts as an acceptable implementation. The second is the actual implementation, denoted by $C$.

A user's prompt $P$ usually does not fully determine $S$:

- some decisions may have been made but left unstated;
- some constraints may remain implicit;
- some decisions may not have been made at all.

This distinction matters: in the first two cases, the agent is trying to recover the user's intent. In the last, it is doing design work on the user's behalf.

We can therefore treat the specification $S$ as a latent (unobserved) variable. Given $P$, many specifications may remain possible. We can represent this uncertainty as $p(S\mid P)$ and, as a conceptual decomposition, see the process as:

$$
P \rightarrow p(S\mid P) \rightarrow C
$$

## The risks of a vague prompt

With a vague prompt, $p(S\mid P)$ is broad, since the prompt is compatible with many specifications. A prompt like `Add caching to the user lookup endpoint` is compatible with a local or shared cache, different TTLs, different invalidation policies, and so on. However, generating an implementation forces the model to commit to specific choices. Those choices will often reflect common patterns from training or conventions in the surrounding code, whether or not they match what the user would have chosen. The result is a plausible interpretation of $P$ that encodes design decisions the user never explicitly made.

The risk here is twofold:

- decisions may be suboptimal because the agent cannot account for task-specific knowledge. For example, the user may know that accounts whose usernames start with `temp_` are temporary and should never be cached;
- we may be unaware of what is happening under the hood.

## The benefits of a clear vision

The situation changes when the user has a clear model of the system they want to build and communicates that model clearly to the agent. The prompt can then encode architectural choices, constraints, invariants, **ideas**, and other important design decisions. As a result, $p(S\mid P)$ becomes more concentrated, and the agent has less freedom to decide what the software should be. Ideally, whatever remains underspecified is also less important. I like thinking of this as gaining control of a powerful (stochastic) racehorse.

This brings us to the infamous question: should we read AI-generated code? I believe it depends:

- When the prompt is vague, reading the generated code means discovering which design decisions the agent made on our behalf.
- When the human largely controls the specification, that function becomes less important because the code implements decisions already made elsewhere.

This reduces the need to read code *in order to discover design decisions*. It does not eliminate the need for review, since security, maintainability, integration, observability, and performance may still require direct inspection.

However, this line of thinking helps us distinguish two distinct failure modes:

- The agent infers the wrong specification.
- The agent implements the specification incorrectly.

Controlling the specification reduces the first kind of failure but does not eliminate the second. Tests, invariants, type systems, static analysis, and other established software engineering practices help address implementation failures.

From this perspective, Antirez's “control the ideas, not the code” sounds much less radical. Given a limited attention budget, human effort often has greater leverage when spent making important decisions explicit, **controlling $S$** rather than **reading $C$**.
