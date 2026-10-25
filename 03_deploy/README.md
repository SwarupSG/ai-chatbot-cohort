# Stage 9: deploy to Vercel

Stage 9 is the three files at the root of this repository: `app.py`, `index.html` and
`test_chat.py`. They sit at the root because Vercel runs the root. `app.py` is stage 8 plus
the passphrase check, and `index.html` is stage 8 plus the passphrase prompt; the lines
marked `NEW in stage 9` are the only lines that changed. Every message or error page you
can meet on the way is listed in the table "If something is wrong" at the end of this page;
look there first.

## Why Vercel needs its own copy of the four values

Your `.env` file is listed in `.gitignore`, so it was never uploaded to GitHub, and Vercel
builds from GitHub. On Vercel, the same line `os.getenv("LLM_API_KEY")` reads the project's
own environment settings instead of `.env`. The code does not change; the place the values
are read from does. Until you enter the four values there, the deployed program cannot start, or cannot
answer, and the fix table at the end of this page names each case.

## Part 1: run it on your laptop first (5 minutes)

1. Open `.env` at the root and change its last line, `APP_PASSWORD=choose-a-word`, to a
   word of your choice, for example `APP_PASSWORD=seaside`. Save the file.
2. Terminal 1, at the root. Check that the prompt starts with `(.venv)`; if it does not,
   run `source .venv/bin/activate` first. Then run `python app.py`. Open
   http://localhost:8000 in the browser, enter your passphrase when the page asks, and
   send one message. Stop the server with Ctrl+C.
3. Terminal 2, at the root: `git status`. The file `.env` must not be in the list. If it is,
   stop: the `.gitignore` line is missing, and the next step would upload your key.
4. `git add .` then `git commit -m "chatbot with passphrase"` then `git push`.

## Part 2: put it on Vercel (10 minutes)

The labels below are the ones on the Vercel website in October 2026.

1. Sign in at https://vercel.com with the GitHub account you used for the repository.
2. Press **Add New**, then **Project**. In the list of your GitHub repositories, find the one
   you created from the course template and press **Import**.
3. On the import screen, leave the framework as Vercel detected it (Flask) and leave the
   root directory as it is. Do not press Deploy yet.
4. Open the section **Environment Variables** on the same screen. For each of the four
   values below, type the name in the **Key** box and the value in the **Value** box, then
   press **Add**. Copy the values from your own `.env`; type the names exactly as shown,
   with the underscores and in capitals.

   | Key | Value |
   |---|---|
   | `LLM_BASE_URL` | the address line from the active block of your `.env` |
   | `LLM_API_KEY` | your key from the same block |
   | `LLM_MODEL` | the model name from the same block |
   | `APP_PASSWORD` | the word you chose in Part 1 |

5. Press **Deploy**. The build takes about one to three minutes. When it finishes, Vercel
   shows a preview and a **Visit** button.
6. Press **Visit**. The page asks for your passphrase; enter it and type the three memory
   turns. The first reply takes a few seconds longer than the others, because Vercel starts
   the program for the first request. If instead you see "This page is unavailable" with
   the code FUNCTION_INVOCATION_FAILED, one of the three LLM values did not reach Vercel:
   go to the next section.
7. Copy the link from the browser's address bar. It is the project's own link, in the form
   `https://<project-name>.vercel.app`. Post that link, and your passphrase, in the class
   channel. Do not post the longer link with random letters in it: that one is a single
   deployment, and visitors who are not signed in to Vercel cannot open it.
8. In `test_chat.py`, change `ADDRESS` to your link followed by `/chat`, and `PASSPHRASE`
   to the word you chose in Part 1. Run `python test_chat.py` at the root, in a terminal
   whose prompt starts with `(.venv)`.

## If you added the values after the first deploy

This is also the section for the error page "This page is unavailable,
FUNCTION_INVOCATION_FAILED": the program stopped because a value is missing on Vercel.

1. Open your project on Vercel, press **Settings**, then **Environment Variables** in the
   left menu, and add or edit the values as in Part 2, step 4. Press **Save**.
2. Press **Deployments** at the top, open the menu with three dots on the most recent
   deployment, and press **Redeploy**. A changed value is read only by a new deployment.
3. If you need the program's own error text, open the deployment and press **Logs**. On
   the free plan the log is kept for one hour, so look soon after the error.

## If something is wrong

| What you see | What it means | What to do |
|---|---|---|
| `command not found: python` (macOS) or `No module named flask` (WSL) | The virtual environment is not on in this terminal | Run `source .venv/bin/activate`, then the command again |
| The build fails | `requirements.txt` is missing or misspelled | Fix it, commit, push; Vercel builds again |
| Every reply is "APP_PASSWORD is not set on this server." | The value is missing in Vercel's settings | Add `APP_PASSWORD` in Settings, Environment Variables, then Redeploy |
| Every reply starts "The provider refused the request" | One of the three LLM values is wrong in Vercel's settings | Check the three names and values against your `.env`, then Redeploy |
| Every reply is "The passphrase is wrong." | The passphrase sent does not match `APP_PASSWORD` on the server | Compare three places and make them the same: the value on Vercel, the word the page asked for, and `PASSPHRASE` in `test_chat.py` |
| The page does not ask for a passphrase | An old build is open | Refresh after the new build finishes |
| A page that says "This page is unavailable" with a code like FUNCTION_INVOCATION_FAILED | One of the three LLM values is missing, so the program stopped at the line that creates the client | Add the missing value in Settings, Environment Variables, then Redeploy |
| `test_chat.py` says Connection refused | `ADDRESS` still points to localhost | Change it to your link followed by `/chat` |

After the session, revoke both keys on the providers' pages and create new ones when you
next need them.
