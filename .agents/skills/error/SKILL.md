---
name: error
description: Read an error message or traceback with the learner, explain it in plain English, point to the line, and ask what they will change. Use whenever the learner pastes an error or says a script stopped.
metadata:
  opencode/slash: "true"
---
# Read an error with the learner

1. Ask the learner to paste the last ten lines the script printed, if they have not.
2. Find the error type and the message. Reply in bullets: one for what that type of error
   means, one for what the message says.
3. One bullet points to the line: the file, the line number from the traceback, and the
   line itself in backticks. If the script printed one of the course's own messages (for example "LLM_API_KEY is
   not set yet" or "The provider refused the request"), explain that message and the action
   it names.
4. One bullet says in words what change would fix it, for example "move the line that
   creates history above the while line". A last bullet asks whether that matches what
   they see; if the learner proposes a different change, say whether it would work.

Do not type the corrected line; the learner types it. Never ask for or display the
contents of `.env` or a key.
