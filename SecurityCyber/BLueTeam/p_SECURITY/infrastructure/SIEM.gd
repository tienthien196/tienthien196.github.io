# res://security360/infrastructure/SIEM.gd
class_name SIEM
extends SecurityModule

var logs = []
var correlation_rules = {}
var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()
    _load_correlation_rules()

func _load_correlation_rules():
    correlation_rules = {
        "brute_force": {
            "events": ["LOGIN_FAILED"],
            "count": 5,
            "window": 60,  # trong 60 giây
            "alert": "BRUTE_FORCE_DETECTED"
        },
        "sql_injection": {
            "events": ["WAF_ALERT"],
            "filter": {"attack": "sql_injection"},
            "alert": "SQLI_ATTACK"
        }
    }

func start():
    logger.info("📊 [SIEM] Hệ thống SIEM đã khởi động.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    # Ghi log
    _log_event(event_type, data)
    # Phân tích tức thì
    _analyze_immediate(event_type, data)
    # Kiểm tra correlation
    _check_correlation(event_type, data)

func _log_event(type: String, data: Dictionary):
    var entry = {
        "timestamp": OS.get_unix_time(),
        "type": type,
        "data": data
    }
    logs.append(entry)
    logger.debug("📝 [SIEM] Ghi sự kiện: %s" % type)

func _analyze_immediate(event_type: String, data: Dictionary):
    match event_type:
        "WAF_ALERT":
            logger.critical("🚨 [SIEM] PHÁT HIỆN TẤN CÔNG WEB: %s từ IP %s" % [data.attack, data.ip])
            Security360.events.emit("THREAT_DETECTED", {
                "type": "WEB_ATTACK",
                "severity": "HIGH",
                "ip": data.ip,
                "payload": data.signature
            })
        "MALWARE_DETECTED":
            logger.critical("🦠 [SIEM] PHÁT HIỆN MÃ ĐỘC: %s trên %s" % [data.file, data.host])
            Security360.events.emit("AUTO_QUARANTINE", data)

func _check_correlation(event_type: String, data: Dictionary):
    # Ví dụ đơn giản: đếm LOGIN_FAILED
    if event_type == "LOGIN_FAILED":
        var recent = _get_events_in_last("LOGIN_FAILED", 60)
        if recent.size() >= 5:
            logger.critical("🚨 [SIEM] PHÁT HIỆN BRUTE FORCE: %d lần đăng nhập thất bại" % recent.size())
            Security360.events.emit("BRUTE_FORCE_ALERT", {
                "ip": data.ip,
                "count": recent.size(),
                "window": 60
            })
            Security360.events.emit("AUTO_BLOCK_IP", {"ip": data.ip})

func _get_events_in_last(event_type: String, seconds: int) -> Array:
    var now = OS.get_unix_time()
    var result = []
    for log in logs:
        if log.type == event_type and log.timestamp >= now - seconds:
            result.append(log)
    return result

func get_logs():
    return logs.duplicate(true)  # trả bản sao

func stop():
    logger.info("🛑 [SIEM] Đã tắt.")