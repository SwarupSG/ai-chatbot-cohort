# Five modifications to stage 8

Each modification below changes `02_web/stage8/app.py` and is a habit that real applications
keep: measuring cost, bounding cost, checking input, serving a single-turn tool, and not
waiting forever. Do them in order, one at a time; each is between one and eight lines. For
each one, write your prediction before you run, then test with the page at
http://localhost:8000 and with `python test_chat.py` in a second terminal, both with
`(.venv)` in the prompt. The three tests, behaviour, memory and budget, must still pass
after every modification except where the text says otherwise.

The labels named below are the numbered comments in `app.py`, such as `# 6. Call the model`.
The tutor can explain any line; it will not write the change for you.

## 1. Print the tokens number in the server's terminal

What a real application does: it records the tokens of every request, because that is the
bill. Here the record is one printed line.

- Under label 7, after the line that sets `tokens`, add one `print` that prints the words
  `tokens sent:` and the value of `tokens`, in the same form as stage 4.
- Predict: which terminal will show the line, the server's or the test client's, and will
  the page change at all?
- Test: send three turns from the page and watch terminal 1. The number grows with the
  list, as it did in stage 4; the page is unchanged.
- The mistake to expect: putting the `print` above the line that sets `tokens`, which gives
  a `NameError`; the tutor's `/error` reads it with you.

## 2. Cap the reply length with `max_tokens`

What a real application does: it sets a ceiling on every call so that one request cannot
run to the model's maximum, which bounds cost and waiting time, and it uses the same ceiling
to keep answers short.

- Under label 6, inside the `create(` call, add one argument on its own line, `max_tokens`
  set to a small number such as 40, with a comma after it, the way `messages=messages,` is
  written.
- Predict: will the tokens number sent change, or only the reply?
- Test: ask the café a question that needs a long answer. The reply stops before it is
  finished. The tokens number sent is the same as before, because the cap limits the reply,
  not the request. Raise the number until the memory test passes again.
- The mistake to expect: a cap so small that turn 2's reply is cut before it names Sunday,
  so the memory test fails for a reason that has nothing to do with memory. On some free
  models the reply is empty at any small cap and the page shows "null": the model spends
  the whole cap on hidden reasoning before it writes. Test this one on Gemini, where a cap
  of 20 gives a cut reply of about twelve words.

## 3. Refuse a message that is too long before calling the model

What a real application does: it checks input at the boundary before paying for a call. A
public address that forwards anything to a paid model is open to oversized or hostile
input; a length check is the first guard, and a rate limit is the second.

- Under label 4, after the line that reads `history`, read the last entry's content:
  `history[-1]["content"]` is the text the visitor just typed.
- Add a check in the shape of the passphrase check you will meet in stage 9: if the length
  of that text, `len(...)`, is over 300, return a dictionary with a readable reply such as
  "Your message is over 300 characters. Please shorten it." and the tokens value
  `"unknown"`, followed by the status number 400, which means a bad request.
- Predict: what will the page show, and what will the server's log line say instead of
  200?
- Test: paste a long paragraph into the page. The reply is your sentence, the log line ends
  in 400, and the model was never called. A normal message still gets 200.
- The mistake to expect: placing the check under label 5 instead of label 4, after the
  system entry has been added, so that `history[-1]` is still right but the check runs
  later than it needs to. It works, but the point is to refuse before any work is done.

## 4. Add a single-turn route, `POST /summarise`

What a real application does: most single-turn AI tools, summarisers, classifiers,
extractors and rewriters, are a fixed instruction plus one user input, with no history.
The only difference from a chatbot is whether a list is sent.

- Below the chat route, copy labels 4 to 7 as a second function under a new route line,
  `@app.post("/summarise")`, with a new function name.
- Change three things in the copy. First, read `text` from the body instead of `history`.
  Second, build `messages` as two entries: a system entry whose content is "Summarise the
  text you are given in two sentences", and one user entry whose content is the text.
  Third, return the reply under the key `"summary"`.
- Predict: how many entries does this route send to the model, however long the
  conversation on the page has been?
- Test: copy `test_chat.py` to `test_summarise.py`. Change `ADDRESS` to end in
  `/summarise`, replace the loop with one `requests.post` that sends `{"text": ...}` with
  a paragraph of your choice, and print `answer["summary"]`. Then run `test_chat.py` again:
  the chat route still passes, because nothing in it changed.
- The mistake to expect: sending the café's system entry to the new route, which makes the
  summariser refuse any text that is not about the café. Each route has its own
  instruction.

## 5. Set a timeout on the model call

What a real application does: it never waits for a provider without a limit. On Vercel a
function that waits too long is stopped with no message at all; a timeout turns that into a
readable reply.

- Under label 6, inside the `create(` call, add the argument `timeout` set to 20, in
  seconds, on its own line with a comma, like the `max_tokens` line.
- Predict: when the provider is slow, which message will the page show, and from which
  line in `app.py` does it come?
- Test: set the timeout to a very small number such as 0.01 and send one turn. The call
  fails before the provider answers, the `except APIError` block under label 6 catches
  it, and the page shows "The provider refused the request" with the timeout named in the
  text. Set it back to 20; the three tests pass again.
- The mistake to expect: putting `timeout` on the `OpenAI(` client under label 1 instead
  of the call. That also works, and applies to every call; the point here is to see which
  line answers when the wait is too long.

## After the five

Run `python test_chat.py` one last time against the server with all five changes in place.
The memory test passes, the log shows 200 for the four turns, and `app.py` is about fifteen
lines longer than stage 8. Those fifteen lines are the ones a deployed application needs
and the course's stages leave out on purpose: they are habits, not lessons.
