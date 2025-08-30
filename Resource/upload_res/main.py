import csv
import json
import os

# Đường dẫn file CSV đầu vào
input_csv_path = r"E:\DOCS\NoteBook\Resource\upload_res\Book_dsa.csv"

# Đường dẫn file JSON đầu ra
output_json_path = r"E:\DOCS\NoteBook\Resource\upload_res\resources.json"

# Kiểm tra file đầu vào có tồn tại không
if not os.path.exists(input_csv_path):
    print(f"❌ File không tồn tại: {input_csv_path}")
    exit(1)

# Danh sách lưu dữ liệu
data = []

# Đọc file CSV và chuyển đổi
with open(input_csv_path, mode='r', encoding='utf-8') as file:
    # Sử dụng csv.reader để xử lý đúng định dạng (dấu ngoặc kép, khoảng trắng)
    reader = csv.reader(file)
    for row in reader:
        # Loại bỏ khoảng trắng thừa và bỏ qua dòng trống
        if len(row) < 2:
            continue
        
        # Chuẩn hóa các trường
        description = row[0].strip().strip('"')
        link = row[1].strip()
        category = row[2].strip().strip('"') if len(row) > 2 else "General"

        # Thêm vào danh sách
        data.append({
            "name": description,
            "description": description,
            "link": link,
            "tags": category
        })

# Ghi ra file JSON
with open(output_json_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"✅ Chuyển đổi thành công! File JSON đã được lưu tại:\n{output_json_path}")