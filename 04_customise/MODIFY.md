# Stage 10: make the chatbot your own

## The Modify menu

Required, in this order:

1. In `app.py`, rewrite the system entry for a purpose of your own: who the assistant is, the facts it may use, and two rules.
2. In `index.html`, change the title and the greeting.
3. In `test_chat.py`, write your own three memory turns: a fact in turn 1, and a question in turn 3 that needs that fact.
4. Run it on your laptop once: `python app.py` in terminal 1, then `python test_chat.py` in terminal 2, both in a terminal whose prompt starts with `(.venv)`.
5. Commit and push. In Vercel, open Settings, then Environment Variables, and change the three LLM values to your OpenRouter block, with a model name ending in `:free`. Press Save, then Redeploy from the Deployments page, as in `03_deploy/README.md`. A free model allows 20 requests a minute and 50 a day on an account with no credits, which is enough for this exercise.
6. Post your link in the class channel with a note of three sentences: what you changed, what you kept, and why the kept lines must not change.

Optional, after the session: a language rule; a larger or smaller KEEP; saving the conversation to a file on your laptop; replacing dropped turns with a summary.

## The reusable-code map

| File | Lines to change | Lines to keep |
|---|---|---|
| app.py | The system entry; the KEEP number | The client lines; the chat route; the trim line; the passphrase check; the refused-request lines; the run lines |
| index.html | The title; the greeting; the style lines | The array; the post; the two appends; the passphrase prompt |
| .env and Vercel's settings | The provider's three values; the passphrase | The names of the four values |
| test_chat.py | The turns | The loop; the post; the appends |
