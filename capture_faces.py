
import cv2
import os

name = input("Enter student name: ")

folder = "dataset/" + name
os.makedirs(folder, exist_ok=True)

cam = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cam.read()

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite(f"{folder}/{count}.jpg", frame)
        count += 1
        print("Image Saved")

    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()