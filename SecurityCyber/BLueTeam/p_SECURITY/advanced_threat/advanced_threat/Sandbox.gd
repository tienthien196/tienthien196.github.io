# res://security360/advanced_threat/Sandbox.gd
class_name Sandbox
extends SecurityModule

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("📦 [Sandbox] Môi trường cách ly đã sẵn sàng.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    if event_type == "EXECUTE_SUSPICIOUS_CODE":
        _emulate_execution(data.code)

func _emulate_execution(code: String):
    if code.find("os.system") != -1 or code.find("subprocess") != -1:
        logger.critical("🚨 [Sandbox] Mã nguy hiểm: thực thi hệ thống")
        Security360.events.emit("BEHAVIORAL_THREAT", {type: "RCE", code_snippet: code.left(50)})
    elif code.find("open('/etc/passwd')") != -1:
        logger.critical("🚨 [Sandbox] Mã nguy hiểm: truy cập file hệ thống")
        Security360.events.emit("BEHAVIORAL_THREAT", {type: "PRIVILEGE_ESCALATION"})

func stop():
    logger.info("🛑 [Sandbox] Đã tắt.")