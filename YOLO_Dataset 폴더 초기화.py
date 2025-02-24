import shutil
import os

dataset_dir = r"C:\Users\pseihun\Graduation Project\Sample"
output_dir = os.path.join(dataset_dir, "YOLO_Dataset")

# 기존 YOLO_Dataset 폴더 삭제 (만약 존재하면)
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

# 새롭게 YOLO_Dataset 폴더 생성
for folder in ["images/train", "images/val", "images/test", "labels/train", "labels/val", "labels/test"]:
    os.makedirs(os.path.join(output_dir, folder), exist_ok=True)

print("✅ YOLO_Dataset 폴더 초기화 완료!")
