"""Stage 3: a loop without memory forgets the previous turn.

What this stage adds: a loop that takes a typed question each turn. The three
fixed questions are gone; you type the questions yourself.
What it does not add: memory. The list is built again on every turn.
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

# 2. The system entry, unchanged from stage 2.
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

input("Predict first: type the first two memory test turns. What will the model say to turn 2? Write it down, then press Enter. ")

# NEW in stage 3
# 3. One turn per loop: take a typed question; the word quit ends the loop.
while True:
    question = input("You: ")
    if question == "quit":
        break

    # NEW in stage 3
    # 4. Build the list again every turn, so turn 1 is gone on turn 2.
    messages = [system_entry, {"role": "user", "content": question}]
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=messages,
        )
    except APIError as refused:
        print("The provider refused the request:", refused)
        print("Check the three LLM values in .env on your laptop, or in Environment Variables in your Vercel project settings. If the message says rate limit, wait one minute and run again.")
        continue

    # 5. Print the reply.
    reply = response.choices[0].message.content
    print("Bot:", reply)

