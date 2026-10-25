---
name: stage-7
description: Course notes for stage 7 of the chatbot course (02_web/stage7/app.py and test_chat.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 7 or about 02_web/stage7/app.py and test_chat.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 7: 02_web/stage7/app.py and test_chat.py

## What this stage adds

The loop, the typed input and the appends are removed. A Flask route (one address the server answers), POST /chat, receives the whole history as JSON (text in a fixed format that browsers and servers both read). It adds the system entry, trims, calls the model and returns one reply with the tokens number. The server keeps nothing. test_chat.py is the caller that keeps the list and sends the four fixed turns.

## The predict question

The test client sends the memory turns through the route. Will the memory test pass? What will the server's terminal show?

## What the learner should see

Terminal 1 (python 02_web/stage7/app.py) prints 'Running on http://127.0.0.1:8000' and then one line per request. Terminal 2 (python test_chat.py) prints the four turns and replies with tokens numbers; the memory test passes because the client resends the list. Stop the server with Ctrl+C, which the server itself names.

## Common messages and what they mean

- 'WARNING: This is a development server' is printed on every start, and nothing is wrong when it appears. It says that Flask's own server is for one developer on one laptop; Vercel starts the application its own way.
- 'Address already in use' means a server from earlier is still running; stop it with Ctrl+C in its terminal.
- 'Connection refused' from the test client means the server is not running or the address is not port 8000.
- 'No module named flask' or 'requests' means the virtual environment is not on in that terminal; run source .venv/bin/activate there, then the command again.
- A WSL terminal whose prompt shows a Windows path is on the wrong side; open a new terminal from the window opened in WSL.
