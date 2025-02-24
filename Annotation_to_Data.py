import os
import shutil

# 이미지가 현재 존재하는 폴더
annotation_dir = r"C:\Users\pseihun\Graduation Project\Sample\Data\Annotation"
# 이미지가 최종적으로 있어야 할 폴더
image_dir = r"C:\Users\pseihun\Graduation Project\Sample\Data"

# Annotation 폴더 내부 파일 확인 및 이동
moved_files = 0
for file in os.listdir(annotation_dir):
    if file.endswith(".jpg"):
        src_path = os.path.join(annotation_dir, file)
        dst_path = os.path.join(image_dir, file)
        shutil.move(src_path, dst_path)
        moved_files += 1

print(f"✅ {moved_files}개 이미지를 Annotation 폴더에서 Data 폴더로 이동 완료!")
