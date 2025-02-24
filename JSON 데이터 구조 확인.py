import json

json_path = "C:\\Users\\pseihun\\Graduation Project\\Sample\\Labeling Data\\Annotation\\blur_sh03_ss014area3_230904_080101_00041.json"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(json.dumps(data, indent=4))