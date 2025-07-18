from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can lock to "http://localhost:3000"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-reply")
async def generate_reply(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a witty, Gen-Z AI assistant helping craft fun, flirty, or smooth replies for dating/chat conversations."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.9,
        max_tokens=100,
    )

    reply = response.choices[0].message.content.strip()
    return {"reply": reply}
@app.get("/")
def read_root():
    return {"message": "Wingman AI backend is live 🚀"}
