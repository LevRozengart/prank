from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home_page():
    return {"status": "ok"}

@app.post("/send_message/{message}")
def send_message(message: str):
    with open("message.txt", "w", encoding="utf-8") as file:
        file.write(message)

@app.get("/get_message")
def get_message():
    with open("message.txt", encoding="utf-8") as file:
        s = file.read()
    with open("message.txt", "w", encoding="utf-8") as file:
        pass
    return {"message": s}

