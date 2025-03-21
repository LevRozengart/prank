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


UPLOAD_DIR = Path("uploads")  # Папка для сохранения файлов
UPLOAD_DIR.mkdir(exist_ok=True)  # Создаём её, если нет


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename  # Путь сохранения

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  # Копируем файл в указанное место

    return {"filename": file.filename, "saved_path": str(file_path)}


UPLOAD_DIR = Path("uploads")  # Папка с загруженными файлами

@app.get("/get_image/{filename}", response_class=FileResponse)
async def get_image(filename: str):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        return {"error": "Файл не найден"}
    return FileResponse(file_path, media_type="image/png")  # Укажи нужный формат