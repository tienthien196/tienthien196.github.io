# res://security360/core/EventManager.gd
class_name EventManager

# Signal để các module kết nối
signal event(type, data)

# Danh sách subscriber (tùy chọn, nếu cần theo dõi)
var subscribers = []

func emit(type: String, data: Dictionary = {}):
    # Phát sự kiện
    emit_signal("event", type, data)

func subscribe(module):
    if not subscribers.has(module):
        subscribers.append(module)

func unsubscribe(module):
    subscribers.erase(module)

# Gọi từ Security360.engine để phân phối
func dispatch(type: String, data: Dictionary):
    emit(type, data)