
import cv2
import os
import pandas as pd
from datetime import datetime
from deepface import DeepFace

dataset = "dataset"
attendance_file = "attendance/attendance.csv"

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

marked = []

while True:

    ret, frame = cam.read() 

    if not ret:
        break

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path=dataset,
            enforce_detection=False
        )

        if len(result) > 0 and len(result[0]) > 0:

            identity = result[0].iloc[0]['identity']

            name = identity.split("\\")[-2]

            if name not in marked:

                marked.append(name)

                time = datetime.now().strftime("%H:%M:%S")

                df = pd.DataFrame([[name, time]], columns=["Name", "Time"])

                df.to_csv(attendance_file,
                          mode='a',
                          header=not os.path.exists(attendance_file),
                          index=False)

                print(name, "attendance marked")

            cv2.putText(frame, name, (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,(0,255,0),2)

    except:
        pass

    cv2.imshow("Smart Attendance", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()