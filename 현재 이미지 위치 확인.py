import os

dataset_dir = r"C:\Users\pseihun\Graduation Project\Sample"
image_original_dir = os.path.join(dataset_dir, "Data")  # 원래 이미지 폴더
image_yolo_dir = os.path.join(dataset_dir, "YOLO_Dataset", "images")  # 이동된 이미지 폴더

# 원래 이미지 폴더 확인
original_images = [f for f in os.listdir(image_original_dir) if f.endswith(".jpg")]
yolo_train_images = os.listdir(os.path.join(image_yolo_dir, "train")) if os.path.exists(os.path.join(image_yolo_dir, "train")) else []
yolo_val_images = os.listdir(os.path.join(image_yolo_dir, "val")) if os.path.exists(os.path.join(image_yolo_dir, "val")) else []
yolo_test_images = os.listdir(os.path.join(image_yolo_dir, "test")) if os.path.exists(os.path.join(image_yolo_dir, "test")) else []

print(f"📂 원래 이미지 폴더: {image_original_dir}")
print(f"🖼️ 원래 이미지 개수: {len(original_images)}")

print(f"\n📂 YOLO train 폴더: {image_yolo_dir}/train")
print(f"🖼️ Train 이미지 개수: {len(yolo_train_images)}")

print(f"\n📂 YOLO val 폴더: {image_yolo_dir}/val")
print(f"🖼️ Validation 이미지 개수: {len(yolo_val_images)}")

print(f"\n📂 YOLO test 폴더: {image_yolo_dir}/test")
print(f"🖼️ Test 이미지 개수: {len(yolo_test_images)}")
