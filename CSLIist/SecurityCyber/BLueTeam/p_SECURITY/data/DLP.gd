# res://security360/data/DLP.gd
class_name DLP
extends SecurityModule

var sensitive_patterns = {
    "credit_card": r"(\d{4}[-\s]?){3}\d{4}",
    "ssn": r"\d{3}[-\s]?\d{2}[-\s]?\d{4}",
    "password": r"(password|pass|pwd)[:\s]+[\w@#$%&]+",
    "api_key": r"api[_-]?key[:\s]+[\w\-]+"
}

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🛡️ [DLP] Hệ thống DLP đã khởi động.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    if event_type == "DATA_TRANSFER":
        _scan_data(data.content, data.context)

func _scan_data(content: String, context: Dictionary):
    for type in sensitive_patterns:
        var pattern = sensitive_patterns[type]
        var matches = RegEx.new()
        matches.compile(pattern)
        var match = matches.search(content)
        if match:
            var alert = {
                "type": "DLP_ALERT",
                "sensitive_type": type,
                "snippet": content.substr(match.get_start(), 50),
                "location": context.get("source", "unknown"),
                "time": OS.get_unix_time()
            }
            logger.critical("🚨 [DLP] Phát hiện rò rỉ dữ liệu nhạy cảm: %s" % type)
            Security360.events.emit("DLP_ALERT", alert)
            Security360.events.emit("AUTO_REDACT", {"data": content, "match": match.get_string()})

func stop():
    logger.info("🛑 [DLP] Đã tắt.")