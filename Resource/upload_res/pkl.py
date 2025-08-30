import json
from typing import Any, Dict, List

# Đường dẫn file
FILE_PATH = r"E:\DOCS\NoteBook\Resource\upload_res\data.json"

def load_data() -> Dict[str, List[Dict]]:
    """Tải dữ liệu từ file JSON"""
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ File không tìm thấy: {FILE_PATH}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Lỗi định dạng JSON: {e}")
        exit(1)

def save_data(data: Dict[str, List[Dict]]) -> None:  # ← Sửa ở đây
    """Lưu dữ liệu ngay lập tức vào file gốc"""
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Lỗi khi lưu file: {e}")

def show_categories(categories: List[str]):
    """Hiển thị danh sách category"""
    print("\n📋 Danh sách các topic (category):")
    for idx, cat in enumerate(categories, start=1):
        print(f"  {idx}. {cat}")

def get_user_choice(options: List[str], prompt: str) -> str:
    """Chọn từ danh sách"""
    while True:
        try:
            choice = input(prompt).strip()
            if not choice:
                return ""
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
            else:
                print("❌ Lựa chọn không hợp lệ.")
        except ValueError:
            print("❌ Vui lòng nhập số.")

def display_item(item: Dict[str, Any]):
    """Hiển thị thông tin item"""
    print("\n" + "-" * 50)
    print("🔹 Đang xử lý item:")
    for key, value in item.items():
        if key != "tags":
            print(f"  {key.capitalize()}: {value}")
    if "tags" in item:
        tags = item['tags']
        if isinstance(tags, list):
            tags_str = ', '.join(tags)
        else:
            tags_str = tags
        print(f"  Tags: {tags_str}")
    print("-" * 50)

def main():
    print("🔄 Đang tải dữ liệu...")
    data = load_data()

    categories = list(data.keys())
    if not categories:
        print("❌ Không có dữ liệu để xử lý.")
        return

    # Chọn category nguồn
    show_categories(categories)
    source_cat = get_user_choice(categories, f"\nNhập số để chọn category xử lý (1-{len(categories)}): ")
    if not source_cat:
        print("❌ Không chọn category. Thoát.")
        return

    items = data[source_cat]
    if not items:
        print(f"⚠️  '{source_cat}' trống. Không có gì để xử lý.")
        return

    print(f"\n🔍 Xử lý {len(items)} item trong '{source_cat}'...")

    # Duyệt từng item
    for i, item in enumerate(items[:]):  # dùng bản sao để an toàn
        display_item(item)
        print(f"\n🎯 Item {i+1}/{len(items)} từ '{source_cat}'")

        # ✅ Cập nhật danh sách lựa chọn MỖI LẦN
        current_categories = list(data.keys())
        target_options = current_categories + ["[Tạo mới]", "[Giữ nguyên]", "[Xóa]"]

        choice = get_user_choice(
            target_options,
            "Chọn hành động:\n" +
            "\n".join(f"  {i+1}. {opt}" for i, opt in enumerate(target_options)) +
            f"\nNhập số (Enter để giữ nguyên): "
        )

        if choice == "[Giữ nguyên]":
            continue
        elif choice == "[Xóa]":
            data[source_cat].remove(item)
            save_data(data)
            print("🗑️  Đã xóa item. ✅ Đã cập nhật file.")
        elif choice == "[Tạo mới]":
            new_cat = input("👉 Nhập tên category mới: ").strip()
            if not new_cat:
                print("❌ Tên không hợp lệ, giữ nguyên.")
                continue
            if new_cat not in data:
                data[new_cat] = []
                print(f"🆕 Đã tạo category: '{new_cat}'")
            data[new_cat].append(item)
            data[source_cat].remove(item)
            save_data(data)
            print(f"✅ Đã chuyển đến '{new_cat}'. ✅ Đã cập nhật file.")
        elif choice in current_categories:
            data[choice].append(item)
            data[source_cat].remove(item)
            save_data(data)
            print(f"✅ Đã chuyển đến '{choice}'. ✅ Đã cập nhật file.")
        else:
            print("⚠️  Không xử lý.")

        # Kiểm tra xem có xóa category nguồn nếu rỗng
        if not data[source_cat]:
            confirm = input(f"\n📌 '{source_cat}' đã rỗng. Xóa category này? (y/N): ").strip().lower()
            if confirm == 'y':
                del data[source_cat]
                save_data(data)
                print(f"🗑️  Đã xóa category '{source_cat}'. ✅ Đã cập nhật file.")

    print(f"\n🎉 Hoàn tất! Mọi thay đổi đã được lưu trực tiếp vào file.")
    print(f"📁 File: {FILE_PATH}")

if __name__ == "__main__":
    main()