# Stage 6: the provider is three values in .env

Stage 6 has no script of its own. The lesson is that nothing in the code changes when the
provider changes: you edit three lines in `.env` and run `01_base/stage5.py` again, this time
on an OpenRouter free model. The folder lists `stage1.py` to `stage5.py` for that reason.

## What to do

1. Open `.env` at the root. Put a `#` in front of the three active Gemini lines, and remove
   the `#` from the three OpenRouter lines, so that exactly three lines are without a `#`:

   ```text
   LLM_BASE_URL=https://openrouter.ai/api/v1
   LLM_API_KEY=paste-your-openrouter-key-here
   LLM_MODEL=paste-a-model-name-ending-in-:free
   ```

2. Paste your OpenRouter key after `LLM_API_KEY=`, and after `LLM_MODEL=` type the name of
   a free model from https://openrouter.ai/models, which ends in `:free`. A model that passed
   all three tests when this course was last tested is `recursive/flint-v1.0:free`. Save the
   file.
3. At the root, with `(.venv)` in the prompt, run `python 01_base/stage5.py` again. Type the
   three memory test turns and then the France question, and tick the three tests on the
   stage guide page as before.
4. When the tests are done, put the `#` back in front of the three OpenRouter lines and
   remove it from the three Gemini lines, so that stages 7 to 9 run on Gemini. The
   OpenRouter block stays in the file for stage 10.

## What you should see

Nothing in the code changed, and the same script runs on a different provider. The replies
may differ in tone and speed, the refusal rule may be weaker, and the tokens number may
print as `unknown` if the provider does not return a count.

Free models have conditions: 20 requests a minute and 50 a day on an account that has
bought no credits, model names that are replaced without notice, and some that may train
on your prompts. Do not type personal or client information into a free model.

## If something is wrong

| What you see | What it means | What to do |
|---|---|---|
| "The provider refused the request" with 429 or "rate limit" | The per-minute or per-day free limit | Wait one minute, or choose another `:free` model |
| A message that the model was not found | The name after `LLM_MODEL=` is not exact | Copy the name again from the model list, including `:free` |
| "The provider refused the request" with 401 or "API key" | The OpenRouter key is wrong, or the Gemini lines are still active | Check the three lines without a `#` in `.env` |
| Four active lines, or two | A `#` is missing or one too many | Exactly three lines carry no `#`, all from one block |
