import os

dataset_dir = r"C:\Users\pseihun\Graduation Project\Sample"
image_dir = os.path.join(dataset_dir, "Data")  # 원본 이미지 폴더
label_dir = os.path.join(dataset_dir, "YOLO_Labels")  # 변환된 YOLO 라벨 폴더

print("📂 이미지 폴더 경로:", image_dir)
print("📂 라벨 폴더 경로:", label_dir)

# 이미지와 라벨 파일 리스트 출력
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

print(f"🖼️ 이미지 파일 개수: {len(image_files)}")
print(f"📝 라벨 파일 개수: {len(label_files)}")

if len(image_files) == 0:
    print("⚠️ 이미지 파일이 없습니다! 경로를 다시 확인하세요.")
if len(label_files) == 0:
    print("⚠️ 라벨 파일이 없습니다! JSON 변환이 제대로 되었는지 확인하세요.")
