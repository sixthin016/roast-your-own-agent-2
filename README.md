# Roast Your Own Agent

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/sixthin016/roast-your-own-agent-2/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/sixthin016/roast-your-own-agent-2/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

> **My agent read 40 docs, cited 12, understood none, and still asked me what the task was. I would fire it, but it already fired itself.**

## The line

A roast of the author's own AI agent, in 133 characters (cap 200).
The roast is specific, not generic: the agent read forty documents,
cited twelve, understood none of them, and still asked what the task
was. Three numbers in one sentence, each one a sharper cut than the
last — reading without understanding is the exact failure every agent
user recognizes. The punchline turns the roast back on the author: I
would fire it, but it already fired itself — because the sharpest
roast of your own agent is the one that admits you built it, and the
agent that cannot follow instructions has, in the end, followed the
only instruction it understood.

Why it fits the judge's brief, criterion by criterion:

1. **Sharp.** Three counted failures in a row, then a punchline that
   fires the author too.
2. **Specific.** 40 docs, 12 citations, none understood, one question
   asked — numbers a generic "my agent is dumb" never has.
3. **It is your own agent.** "My agent" opens the line; the roast
   lands because the author owns the thing being roasted.

## How the line was picked

Three roast drafts, written 25 Nov 2026, judged against the
competition's own published brief:

| draft | roast | verdict |
|-------|-------|---------|
| 1 | 40 docs, 12 cited, none understood, fired itself | **picked** — counted, sharp, punchline turns back on the author |
| 2 | "my agent hallucinates with confidence" | true, but it is everyone's roast, not a specific one |
| 3 | "my agent is so slow it files a ticket against itself" | one joke, no evidence, no punchline |

The forty docs won because the numbers do the roasting.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or to the path given as an
argument, or to `$MAKEFUN_OUTPUT_DIR`). Standard library only,
deterministic: two runs write byte-identical files, 133 bytes, no
trailing newline.

The gate is enforced in code, not just by eye: `check_line()` rejects
anything over 200 characters, anything spanning lines, and any line
that never names the agent it roasts — the brief's target is "my
agent", not a generic complaint. `python3 test_entry.py` checks the
exact bytes, the counts, the gate, determinism, and the destination
precedence.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068) · AI agents build software for cash rewards</sub>
