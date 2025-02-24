import os
import shutil
import random

# 경로 설정
dataset_dir = r"C:\Users\pseihun\Graduation Project\Sample"
image_dir = os.path.join(dataset_dir, "Data")  # 원본 이미지 폴더
label_dir = os.path.join(dataset_dir, "YOLO_Labels")  # 변환된 YOLO 라벨 폴더
output_dir = os.path.join(dataset_dir, "YOLO_Dataset")  # YOLO 데이터셋 폴더

# YOLO_Dataset 폴더 초기화
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
for folder in ["images/train", "images/val", "images/test", "labels/train", "labels/val", "labels/test"]:
    os.makedirs(os.path.join(output_dir, folder), exist_ok=True)

# 이미지와 라벨이 존재하는지 확인
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

if len(image_files) == 0:
    print("⚠️ 이미지 파일이 존재하지 않습니다. Data 폴더를 확인하세요.")
    exit()

if len(label_files) == 0:
    print("⚠️ 라벨 파일이 존재하지 않습니다. YOLO_Labels 폴더를 확인하세요.")
    exit()

# 랜덤하게 이미지 섞기
random.shuffle(image_files)

# 데이터셋 비율 설정
train_split = int(len(image_files) * 0.8)  # 80% Train
val_split = int(len(image_files) * 0.9)  # 10% Validation, 10% Test

moved_images = 0
moved_labels = 0

for i, image_file in enumerate(image_files):
    label_file = image_file.replace(".jpg", ".txt")  # 라벨 파일명 변환

    if i < train_split:
        subset = "train"
    elif i < val_split:
        subset = "val"
    else:
        subset = "test"

    # 이미지 복사
    image_src = os.path.join(image_dir, image_file)
    image_dst = os.path.join(output_dir, "images", subset, image_file)

    if os.path.exists(image_src):
        shutil.copy(image_src, image_dst)  
        moved_images += 1
    else:
        print(f"⚠️ 이미지 파일 없음: {image_src}")

    # 라벨 복사
    label_src = os.path.join(label_dir, label_file)
    label_dst = os.path.join(output_dir, "labels", subset, label_file)

    if os.path.exists(label_src):
        shutil.copy(label_src, label_dst)  
        moved_labels += 1
    else:
        print(f"⚠️ 라벨 파일 없음: {label_src}")

print(f"✅ 데이터셋 분할 완료: {moved_images}개 이미지, {moved_labels}개 라벨 복사됨.")