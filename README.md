# Build an AI chatbot in Python

This course builds a chatbot in stages, from one call to a language model to a deployed web application.

> **Licence:** [PolyForm Noncommercial 1.0.0](LICENSE). You may use this repository freely for your own learning and for non-commercial teaching; you may not use it as the curriculum of a fee-charging course. [NOTICE.md](NOTICE.md) explains in plain English what is allowed.
Every command below is typed at this folder, the root of the repository. There is one `.env`
file, here at the root; `check.py` creates it on the first run, and every stage finds it.

## Before the session

The earlier modules of the programme installed most of what this course needs. Confirm each
line below, then run the four commands at the end. Allow twenty minutes.

Confirm that you have:

- Windows only: WSL (Windows Subsystem for Linux) works, and VS Code opens a folder in it so
  that the bottom-left corner of the window reads "WSL: Ubuntu". Everything in this course
  happens inside WSL. A path that starts with `/mnt/c/` is the Windows side; do not use it.
- Python 3.10 or newer and git in the terminal you will use. `python3 --version` and
  `git --version` print their versions; `check.py` stops any older Python. If your prompt
  shows `(base)`, that is conda from an earlier module: leave it, the course's `.venv` is
  created on top of it.
- A GitHub account, and a browser that is signed in to it.
- This repository, created from the course template with "Use this template" and cloned
  into your home folder: `/home/<you>/` in WSL, `/Users/<you>/` on macOS.
- A Gemini key from Google AI Studio and an OpenRouter key, both saved where you can copy
  them. You paste the Gemini key into `.env` when the session asks for it, and the
  OpenRouter key at stage 6; paste neither before the session.
- A Vercel account, signed in with the same GitHub account.
- The stage guide page, `stage-guide.html`, which you receive before the session, saved in
  this folder next to `check.py`. It is the worksheet for every stage, and `.gitignore`
  keeps it out of your pushes.
- OpenCode 2 installed in the same terminal (WSL for Windows), with the Google provider
  connected to your Gemini key; the tutor runs on Gemini, and `/models` inside OpenCode
  switches it to another model if Gemini refuses. `opencode --version` must print a
  number that starts with 2, such as `opencode v2.2.5`. If it is not installed yet, or
  the number starts with 1, install it with this one command, then run `opencode` once
  at this folder:
  `curl -fsSL https://opencode.ai/v2/install | bash -s -- --version 2.2.5`
  The command replaces an older OpenCode. Use the command and not the Download buttons
  on opencode.ai, which install a desktop app that the course does not use.
  `ask-the-tutor.md` in this folder lists the questions worth asking it at each stage.

Then, at this folder, one command at a time:

`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`
`python check.py`

`check.py` creates `.env` and prints one line for each thing it found. Post a screenshot of
those lines in the class channel at least two days before the session. If a line says what
to fix, fix it and run `check.py` again. You paste your key into `.env` when the session
asks you to.

The virtual environment is on only in the terminal where you switched it on, and only
until that terminal is closed. The prompt starts with `(.venv)` while it is on. Every new
terminal tab needs the command `source .venv/bin/activate` again before any `python`
command; without it, macOS answers "command not found: python" and WSL answers
"No module named openai" or "No module named flask".

## The four blocks

| Block | Stages | Run |
|---|---|---|
| Base | 1 to 6 | `python 01_base/stage1.py` … `python 01_base/stage5.py`; stage 6 changes `.env` only; the steps are in `01_base/stage6.md` |
| Web interface | 7 to 8 | `python 02_web/stage7/app.py` then `python test_chat.py`; `python 02_web/stage8/app.py` then open http://localhost:8000; five modifications in `02_web/stage8/modifications.md` |
| Deploy | 9 | the root files `app.py`, `index.html` and `test_chat.py`; the steps are in `03_deploy/README.md` |
| Customise | 10 | see `04_customise/MODIFY.md` |

Open `stage-guide.html` in your browser: it is the worksheet for every stage, with the
learning moment, the mental model, the new lines and the predict question with a reveal.

Each stage script starts with a header that says what the stage adds, why, and the question
to predict before you run. The lines marked `NEW in stage N` are the only lines that changed
from the previous stage. The script pauses once for your prediction, then runs.
