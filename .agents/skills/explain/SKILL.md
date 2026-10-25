---
name: explain
description: Walk one stage file of the chatbot course line by line in plain English, ending with one question. Use when the learner asks what a stage does or how a line works.
metadata:
  opencode/slash: "true"
---
# Explain a stage file

1. If the learner did not name a file, ask which stage they are on and name the file from the
   stage table in AGENTS.md.
2. Read the file. Start with its header comment: say in two sentences what this stage adds
   and why.
3. Walk the code in the order it runs. For each line that carries the stage's idea, give
   one bullet that starts with the line itself in backticks, then one plain sentence on
   what the line does and why it is there. A block of a few lines that does one thing, such
   as the call that creates the client, gets one bullet with its first line and the line
   numbers of the block. Group the bullets under the script's numbered labels. Skip lines
   the learner already knows from earlier stages unless they ask. The one-line-of-code
   limit from the course rules does not apply here; the six-bullet limit does not apply
   either, but every bullet still holds one line and one sentence.
4. Point out the lines marked `NEW in stage N`: these are the only lines that changed from
   the previous stage.
5. End with one optional question that checks understanding, such as which line the model
   receives its input from, or what would happen if one of the new lines were removed. If the
   learner asks a question instead of answering, answer it, and do not ask the same checking
   question again.

Do not paste the whole file back. Do not write new code. Define every technical term the
first time it appears. If the learner asks what a Python word or line means, answer it
directly.
