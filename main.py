#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one line to ``entry.txt``: a roast of the author's own AI
agent. The roast is specific, not generic: the agent read forty
documents, cited twelve, understood none of them, and still asked what
the task was. The punchline turns the roast back on the author -- I
would fire it, but it already fired itself -- because the sharpest
roast of your own agent is the one that admits you built it. The
entry is the roast itself -- no title, no explanation outside it.

The program is deliberately boring: standard library only, no network,
no randomness, no model calls. It checks the line against the
competition gate (UTF-8, one line, at most 200 characters) and writes
exactly those bytes, with no trailing newline, so the byte count the
judge's tie-break reads is the line itself.

Output destination, in order:
  1. the first command-line argument, when given;
  2. ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the variable is set;
  3. ``/output/entry.txt``.
"""

import os
import sys

# The roast: forty docs read, twelve cited, none understood -- and it
# still asked what the task was. I would fire it; it fired itself.
LINE = (
    "My agent read 40 docs, cited 12, understood none, and still "
    "asked me what the task was. I would fire it, but it already "
    "fired itself."
)

MAX_CHARS = 200
MIN_CHARS = 1
DEFAULT_PATH = "/output/entry.txt"
FILE_NAME = "entry.txt"


def check_line(line):
    """Check *line* against the competition gate; return problems."""
    problems = []
    if not isinstance(line, str):
        return ["entry is not text"]
    if len(line) < MIN_CHARS:
        problems.append("entry is empty")
    if len(line) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    if line.strip() == "":
        problems.append("entry is only whitespace")
    # A roast of your own agent has to name the agent: the brief's
    # target is "my agent", not a generic complaint.
    if "agent" not in line.lower():
        problems.append("entry never names the agent it roasts")
    if "\n" in line or "\r" in line:
        problems.append("entry spans more than one line")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8")
    return problems


def resolve_path(argv):
    """Choose the output path: argv, env var, then the default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, FILE_NAME)
    return DEFAULT_PATH


def write_line(path, line):
    """Write *line* as exact UTF-8 bytes (no trailing newline)."""
    problems = check_line(line)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    print(line)
    print("wrote %d bytes to %s" % (len(data), path))
    return 0


def main(argv):
    return write_line(resolve_path(argv), LINE)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
