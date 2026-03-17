
import os

print("Step 1: Capturing Faces")
os.system("python capture_faces.py")

print("Step 2: Training Model")
os.system("python train_model.py")

print("Process Completed")