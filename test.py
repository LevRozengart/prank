import requests
import cv2
cam_port = 0
cam = cv2.VideoCapture(cam_port)
result, image = cam.read()
if result:
    cv2.imwrite("img.png", image)
else:
    print("No image detected. Please! try again")

url = "http://127.0.0.1:8000/upload"
files = {"file": open("img.png", "rb")}
response = requests.post(url, files=files)
print(response.json())