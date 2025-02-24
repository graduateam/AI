import os

data_yaml_path = r"C:\Users\pseihun\Graduation Project\Sample\YOLO_Dataset\data.yaml"

if os.path.exists(data_yaml_path):
    print(f"✅ 'data.yaml' 파일이 존재합니다: {data_yaml_path}")
else:
    print("❌ 'data.yaml' 파일이 존재하지 않습니다. 경로를 다시 확인하세요.")
