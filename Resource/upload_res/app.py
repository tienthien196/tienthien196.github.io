# app.py
import json
import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import send_file


app = Flask(__name__)
app.secret_key = 'super-secret-key-for-session'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max upload

# Tạo thư mục nếu chưa có
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

DATA_FILE = 'data.json'

DEFAULT_DATA = {
    "Unity": [
        {
            "name": "Unity Learn",
            "description": "Official Unity learning platform",
            "link": "https://learn.unity.com",
            "tags": "beginner, tutorial",
            "level": "Beginner"
        }
    ],
    "Godot": [
        {
            "name": "Godot Docs",
            "description": "Official documentation for Godot Engine",
            "link": "https://docs.godotengine.org",
            "tags": "documentation, engine",
            "version": "4.2"
        }
    ],
    "Computer Science": [
        {
            "name": "CS50 by Harvard",
            "description": "Free intro to computer science course",
            "link": "https://cs50.harvard.edu",
            "duration": "12 weeks",
            "free": "yes"
        }
    ],
    "Tools Python": [
        {
            "name": "Flask Documentation",
            "description": "Web framework for Python",
            "link": "https://flask.palletsprojects.com",
            "use_case": "web development"
        }
    ]
}

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            flash("Error reading data.json. Loading default data.", "error")
            return DEFAULT_DATA.copy()
    else:
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA.copy()

def save_data(data):
    try:
        # Tạo backup trước khi ghi (tùy chọn)
        if os.path.exists(DATA_FILE):
            os.replace(DATA_FILE, DATA_FILE + '.bak')
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        flash(f"Failed to save data: {str(e)}", "error")
        # Khôi phục backup nếu có
        if os.path.exists(DATA_FILE + '.bak'):
            os.replace(DATA_FILE + '.bak', DATA_FILE)

data_store = load_data()

@app.route('/admin456789')
def index():
    topics = data_store.keys()
    return render_template('index.html', topics=topics)

@app.route('/topic/<topic_name>', methods=['GET', 'POST'])
def topic_detail(topic_name):
    if topic_name not in data_store:
        flash(f"Topic '{topic_name}' does not exist.", "error")
        return redirect(url_for('index'))

    resources = data_store[topic_name]

    if request.method == 'POST':
        # Xử lý thêm tài nguyên mới
        new_resource = {}
        for key in request.form:
            if key.startswith('field_'):
                field_name = key[6:]  # bỏ 'field_'
                value = request.form[key].strip()
                if value:
                    new_resource[field_name] = value

        # Xử lý upload file
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                ext = os.path.splitext(file.filename)[1]
                filename = f"{uuid.uuid4().hex}{ext}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                # Lưu đường dẫn truy cập
                new_resource['file'] = f"/uploads/{filename}"
                new_resource['filename'] = secure_filename(file.filename)

        if 'name' in new_resource and 'link' in new_resource:
            resources.append(new_resource)
            save_data(data_store)
            flash("Resource added successfully!", "success")
        else:
            flash("Name and link are required!", "error")
        return redirect(url_for('topic_detail', topic_name=topic_name))

    return render_template('topic.html', topic=topic_name, resources=resources)

@app.route('/topic/<topic_name>/edit/<int:resource_id>', methods=['GET', 'POST'])
def edit_resource(topic_name, resource_id):
    if topic_name not in data_store or resource_id >= len(data_store[topic_name]):
        flash("Invalid topic or resource.", "error")
        return redirect(url_for('index'))

    resource = data_store[topic_name][resource_id]

    if request.method == 'POST':
        updated_resource = {}
        for key in request.form:
            if key.startswith('field_'):
                field_name = key[6:]
                value = request.form[key].strip()
                if value:
                    updated_resource[field_name] = value

        # Xử lý upload file mới
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                # Xóa file cũ nếu có
                old_file_path = None
                if 'file' in resource:
                    old_file_rel = resource['file']
                    if old_file_rel.startswith('/uploads/'):
                        old_file_rel = old_file_rel[len('/uploads/'):]
                        old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_file_rel)
                if old_file_path and os.path.exists(old_file_path):
                    os.remove(old_file_path)

                # Lưu file mới
                ext = os.path.splitext(file.filename)[1]
                filename = f"{uuid.uuid4().hex}{ext}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                updated_resource['file'] = f"/uploads/{filename}"
                updated_resource['filename'] = secure_filename(file.filename)
            elif 'file' in resource:
                # Giữ nguyên file cũ
                updated_resource['file'] = resource['file']
                if 'filename' in resource:
                    updated_resource['filename'] = resource['filename']

        # Cập nhật lại
        data_store[topic_name][resource_id] = updated_resource
        save_data(data_store)
        flash("Resource updated successfully!", "success")
        return redirect(url_for('topic_detail', topic_name=topic_name))

    return render_template('edit_resource.html', topic=topic_name, resource=resource, resource_id=resource_id)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/topic/<topic_name>/delete/<int:resource_id>')
def delete_resource(topic_name, resource_id):
    if topic_name in data_store and 0 <= resource_id < len(data_store[topic_name]):
        resource = data_store[topic_name].pop(resource_id)
        # Xóa file vật lý nếu có
        if 'file' in resource:
            file_rel = resource['file']
            if file_rel.startswith('/uploads/'):
                file_rel = file_rel[len('/uploads/'):]
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file_rel)
                if os.path.exists(filepath):
                    os.remove(filepath)
        save_data(data_store)
        flash("Resource deleted.", "success")
    else:
        flash("Invalid resource to delete.", "error")
    return redirect(url_for('topic_detail', topic_name=topic_name))
@app.route('/add_topic', methods=['POST'])
def add_topic():
    new_topic = request.form['topic_name'].strip()
    if not new_topic:
        flash("Topic name cannot be empty.", "error")
    elif new_topic in data_store:
        flash(f"Topic '{new_topic}' already exists.", "error")
    else:
        data_store[new_topic] = []
        save_data(data_store)
        flash(f"Topic '{new_topic}' added successfully!", "success")
    return redirect(url_for('index'))

@app.route('/edit_topic/<old_name>', methods=['GET', 'POST'])
def edit_topic(old_name):
    if old_name not in data_store:
        flash("Topic not found.", "error")
        return redirect(url_for('index'))

    if request.method == 'POST':
        new_name = request.form['new_topic_name'].strip()
        if not new_name:
            flash("Topic name cannot be empty.", "error")
        elif new_name in data_store and new_name != old_name:
            flash(f"Topic '{new_name}' already exists.", "error")
        else:
            data_store[new_name] = data_store.pop(old_name)
            save_data(data_store)
            flash(f"Topic renamed to '{new_name}'.", "success")
            return redirect(url_for('index'))

    return render_template('edit_topic.html', old_name=old_name)

@app.route('/delete_topic/<topic_name>')
def delete_topic(topic_name):
    if topic_name in data_store:
        # Xóa tất cả file trong topic nếu có
        for resource in data_store[topic_name]:
            if 'file' in resource:
                file_path = resource['file']
                if file_path.startswith('/uploads/'):
                    file_rel = file_path[len('/uploads/'):]
                    full_path = os.path.join(app.config['UPLOAD_FOLDER'], file_rel)
                    if os.path.exists(full_path):
                        os.remove(full_path)
        # Xóa topic
        del data_store[topic_name]
        save_data(data_store)
        flash(f"Topic '{topic_name}' and all its resources have been deleted.", "success")
    else:
        flash("Topic not found.", "error")
    return redirect(url_for('index'))

@app.route('/export_data')
def export_data():
    """Xuất toàn bộ dữ liệu ra file JSON để backup"""
    try:
        # Tạo bản sao dữ liệu để xuất
        export_content = data_store.copy()

        # Thêm thông tin metadata (tùy chọn)
        meta = {
            "exported_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_topics": len(export_content),
            "note": "This backup includes all resources and file references."
        }

        # Gộp vào dữ liệu
        data_to_export = {
            "meta": meta,
            "data": export_content
        }

        # Tạo tên file theo ngày
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"backup_resources_{timestamp}.json"
        filepath = os.path.join("/tmp", filename)  # Dùng tạm /tmp (Linux/Mac) hoặc temp

        # Nếu trên Windows, hoặc không có /tmp
        if not os.path.exists("/tmp"):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Lưu file tạm
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data_to_export, f, indent=4, ensure_ascii=False)

        # Trả file về cho người dùng
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/json'
        )
    except Exception as e:
        flash(f"Error exporting data: {str(e)}", "error")
        return redirect(url_for('index'))


@app.route('/download/<filename>')
def download_file(filename):
    """Tải file về với tên gốc đã lưu"""
    # Tìm tên gốc trong toàn bộ dữ liệu
    original_name = None
    for topic_resources in data_store.values():
        for res in topic_resources:
            stored_file = res.get('file', '')
            if stored_file == f'/uploads/{filename}' or stored_file.endswith(f'/{filename}'):
                original_name = res.get('filename', None)
                break
        if original_name:
            break

    # Nếu không tìm thấy tên gốc, dùng tên file
    download_name = original_name or filename

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=download_name)
    else:
        flash("File not found.", "error")
        return redirect(url_for('index'))

# @app.route('/debug')
# def debug_data():
#     return data_store

@app.route('/client')
def client_view():
    """Hiển thị toàn bộ tài nguyên dưới dạng client chỉ đọc"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('client.html', data_store=data_store, now=now)

@app.route('/debug1')
def debug_data():
    return render_template('debug.html', data=data_store)


@app.route('/docs')
def docs():
    query = request.args.get('q', '').strip()
    topics = list(data_store.keys())
    filtered_data = {}

    if query:
        # Tìm kiếm toàn bộ
        for topic, resources in data_store.items():
            matched_resources = []
            for res in resources:
                # Kiểm tra trong name, description, tags, link
                content = f"{res.get('name', '')} {res.get('description', '')} {res.get('tags', '')} {res.get('link', '')}".lower()
                if query.lower() in content:
                    matched_resources.append(res)
            if matched_resources:
                filtered_data[topic] = matched_resources
    else:
        filtered_data = data_store

    return render_template('docs.html',
                         topics=sorted(topics),
                         data=filtered_data,
                         query=query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)