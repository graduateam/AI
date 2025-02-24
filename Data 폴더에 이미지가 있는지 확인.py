import os

image_dir = r"C:\Users\pseihun\Graduation Project\Sample\Data"

# Data 폴더에 있는 이미지 개수 확인
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

print(f"📂 Data 폴더 내 이미지 개수: {len(image_files)}")
print(f"📄 파일 목록 (일부): {image_files[:5] if image_files else '없음'}")