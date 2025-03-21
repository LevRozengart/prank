from fastapi import FastAPI, File, UploadFile
from pathlib import Path
import shutil
from fastapi.responses import FileResponse

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


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename  # Определяем путь файла

    if file_path.exists():
        file_path.unlink()  # Удаляем старый файл, если он уже есть

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "saved_path": str(file_path)}


UPLOAD_DIR = Path("uploads")  # Папка с загруженными файлами

@app.get("/get_image/{filename}", response_class=FileResponse)
async def get_image(filename: str):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        return {"error": "Файл не найден"}
    return FileResponse(file_path, media_type="image/png")  # Укажи нужный формат