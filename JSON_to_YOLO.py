import json
import os

# JSON 파일 경로 설정
json_dir = r"C:\Users\pseihun\Graduation Project\Sample\Labeling Data\Annotation"
output_dir = r"C:\Users\pseihun\Graduation Project\Sample\YOLO_Labels"

# YOLO 라벨 저장 폴더 생성
os.makedirs(output_dir, exist_ok=True)

# YOLO 클래스 목록 정의 (사람과 자동차만 포함)
classes = ["person", "car"]

# JSON 파일 리스트 가져오기
json_files = [f for f in os.listdir(json_dir) if f.endswith(".json")]

for json_file in json_files:
    json_path = os.path.join(json_dir, json_file)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 이미지 파일명 및 크기 확인
    image_filename = data["file"]["filename"]
    image_width = data["info"]["width"]
    image_height = data["info"]["height"]

    # YOLO 형식 라벨 파일 저장 경로
    yolo_label_path = os.path.join(output_dir, image_filename.replace(".jpg", ".txt"))

    with open(yolo_label_path, 'w') as label_file:
        for annotation in data["annotations"]:
            object_class = annotation["object super class"]

            # YOLO에서 필요한 클래스(사람, 자동차)만 처리
            if object_class not in classes:
                continue  # 필요 없는 객체는 무시

            class_id = classes.index(object_class)  # YOLO 클래스 ID
            bbox = annotation.get("bbox")  # 바운딩 박스 정보 가져오기

            if bbox:
                x_min, y_min, box_width, box_height = bbox

                # YOLO 형식 변환 (x_center, y_center, width, height)
                x_center = (x_min + box_width / 2) / image_width
                y_center = (y_min + box_height / 2) / image_height
                norm_width = box_width / image_width
                norm_height = box_height / image_height

                # YOLO 형식: class_id x_center y_center width height
                label_file.write(f"{class_id} {x_center} {y_center} {norm_width} {norm_height}\n")

print("YOLO 포맷 변환 완료 ✅")