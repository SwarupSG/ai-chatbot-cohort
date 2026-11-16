---
name: stage-5
description: Course notes for stage 5 of the chatbot course (01_base/stage5.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 5 or about 01_base/stage5.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 5: 01_base/stage5.py

## What this stage adds

A constant KEEP sets how many recent entries are kept; each question is one entry and each reply is one entry. One trim line keeps the system entry plus the last KEEP entries before each call. The file sets KEEP = 2.

## Two lines a learner often asks about

- `history[-KEEP:]` is the last KEEP entries of the list, counted from the end; with KEEP at 2 it is the previous reply and the new question, because the trim runs after the new question joins the list.
- `[history[0]] + history[-KEEP:]` joins two lists: the first entry, which is the system entry, and the last KEEP entries, so the system entry is never dropped.

## The predict question

With this KEEP, which memory test turn fails first, or does each turn pass? The file ships with KEEP = 2.

## What the learner should see

The script prints a goal line first, with the value of KEEP in this run: at KEEP = 2 the model receives the system entry, the previous reply and the new question, and turn 2 should fail, or turn 3 if reply 1 repeated Sunday. After turn 3 it prints the value of KEEP again and tells the learner to change KEEP = 2 to KEEP = 6 and run again. At KEEP = 2, turn 2 fails because turn 1 was dropped before turn 2 was sent; sometimes Sunday is still in the list because the first reply repeated it, and then turn 2 passes and turn 3 fails, because the group of three is only in turn 1. At KEEP = 6 all turns pass and the tokens number is highest (about 175 on turn 3). Budget test: the tokens number on the last turn stays under 300.

## Common messages and what they mean

- The system entry is never dropped: the trim keeps history[0].
- Changing KEEP is the only edit in this stage; it is one number on one line.
- 'KEEP must be 1 or more.' means KEEP is 0 or less. At 0 the model would not receive the new question, so the script stops before the first turn.
- 'The model sent no text.' and 'That line was not sent to the model.' mean the same as in stage 4.
