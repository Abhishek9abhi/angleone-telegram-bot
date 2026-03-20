from fastapi import FastAPI
from app.angleone import login_angleone
from app.telegram import send_telegram_message

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Running 🚀"}

@app.get("/test")
def test_all():
    obj, response = login_angleone()

    if obj:
        send_telegram_message("✅ AngleOne Login Successful!")
        return {"status": "AngleOne + Telegram working"}
    else:
        send_telegram_message(f"❌ Login Failed: {response}")
        return {"error": response}