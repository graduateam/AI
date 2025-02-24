import shutil
import os

# 원래 이미지 폴더로 되돌리기
image_original_dir = r"C:\\Users\\pseihun\\Graduation Project\\Sample\Data"
image_yolo_dir = r"C:\\Users\\pseihun\\Graduation Project\\Sample\\YOLO_Dataset\\images"

# train, val, test 폴더에서 모든 이미지 복구
for subset in ["train", "val", "test"]:
    subset_path = os.path.join(image_yolo_dir, subset)
    if os.path.exists(subset_path):
        for img_file in os.listdir(subset_path):
            shutil.move(os.path.join(subset_path, img_file), os.path.join(image_original_dir, img_file))

print("✅ 모든 이미지를 원래 위치로 복구 완료!")
