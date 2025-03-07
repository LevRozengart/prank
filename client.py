import pyttsx3
import requests
import asyncio
engine = pyttsx3.init()

url = "http://127.0.0.1:8000/get_message"


async def main():
    await asyncio.sleep(10)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        message = data["message"]
    else:
        print("Ошибка:", response.status_code)
    engine.say(message)
    engine.runAndWait()

while True:
    asyncio.run(main())