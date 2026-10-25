"""Stage 5: the history has a token budget, and trimming keeps it inside.

What this stage adds: a limit on how many recent entries are kept, and one line
that trims the list to the system entry plus those entries before each call.
Why: the list has a largest size (the context window) and a cost (tokens sent).
Budget test: the tokens number on the last turn stays under 300.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI, APIError

# 1. Connect to the provider.
load_dotenv()
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)

# 2. The system entry, unchanged.
system_entry = {
    "role": "system",
    "content": (
        "You are the assistant of a small café by the sea. "
        "Facts: it opens from 8 in the morning to 6 in the evening from Tuesday to Sunday, "
        "and it is closed on Mondays. It serves coffee, tea and cakes. "
        "Rule 1: answer in at most two sentences. "
        "Rule 2: answer only questions about the café; for anything else, reply exactly: "
        "I can only help with questions about the café."
    ),
}

# NEW in stage 5
# 3. Create the list once, and set how many recent entries are kept.
#    Two entries make one turn: your question and the reply.
history = [system_entry]
KEEP = 2

input("Predict first: KEEP is one turn. Which memory test turn fails first? Write it down, then press Enter. ")

while True:
    question = input("You: ")
    if question == "quit":
        break

    # 4. The typed turn joins the list, then the list is trimmed.
    # NEW in stage 5
    # The system entry is always kept; only the last KEEP entries follow it.
    history.append({"role": "user", "content": question})
    if len(history) > KEEP + 1:
        history = [history[0]] + history[-KEEP:]

    # 5. Send the trimmed list.
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=history,
        )
    except APIError as refused:
        print("The provider refused the request:", refused)
        print("Check the three LLM values in .env on your laptop, or in Environment Variables in your Vercel project settings. If the message says rate limit, wait one minute and run again.")
        history.pop()
        continue

    # 6. The reply joins the list; print it with the number of tokens sent.
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    tokens = response.usage.prompt_tokens if response.usage else "unknown"
    print("Bot:", reply)
    print("tokens sent:", tokens)

