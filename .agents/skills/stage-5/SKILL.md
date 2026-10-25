---
name: stage-5
description: Course notes for stage 5 of the chatbot course (01_base/stage5.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 5 or about 01_base/stage5.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 5: 01_base/stage5.py

## What this stage adds

A constant KEEP sets how many recent entries are kept; two entries make one turn. One trim line keeps the system entry plus the last KEEP entries before each call. The file sets KEEP = 2.

## The predict question

KEEP is 2, which is one turn. Which memory test turn fails first?

## What the learner should see

At KEEP = 2, turn 2 fails because turn 1 was dropped before turn 2 was sent; sometimes Sunday is still in the list because the first reply repeated it. At KEEP = 6 all turns pass and the tokens number is highest (about 175 on turn 3). Budget test: the tokens number on the last turn stays under 300.

## Common messages and what they mean

- The system entry is never dropped: the trim keeps history[0].
- Changing KEEP is the only edit in this stage; it is one number on one line.
