# res://security360/application/SecureCode.gd
class_name SecureCode
extends SecurityModule

var insecure_patterns = {
    "hardcoded_password": r"(password|pass|pwd)[:\s]+['\"][\w@#$%&]+['\"]",
    "insecure_random": r"math\.random\(\)",
    "eval_usage": r"\beval\(",
    "debug_enabled": r"debug[:\s]+true"
}

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🔍 [SecureCode] Kiểm tra mã nguồn đã kích hoạt.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    if event_type == "CODE_SCAN":
        _scan_code(data.source_code, data.file_path)

func _scan_code(source: String, file_path: String):
    for issue in insecure_patterns:
        var pattern = insecure_patterns[issue]
        var regex = RegEx.new()
        regex.compile(pattern)
        var match = regex.search(source)
        if match:
            var alert = {
                "issue": issue,
                "file": file_path,
                "line": _get_line_number(source, match.get_start()),
                "code_snippet": match.get_string()
            }
            logger.warn("⚠️ [SecureCode] Phát hiện mã không an toàn: %s trong %s" % [issue, file_path])
            Security360.events.emit("CODE_VULNERABILITY", alert)

func _get_line_number(source: String, pos: int) -> int:
    var lines = source.left(pos).split("\n")
    return lines.size()

func stop():
    logger.info("🛑 [SecureCode] Đã tắt.")