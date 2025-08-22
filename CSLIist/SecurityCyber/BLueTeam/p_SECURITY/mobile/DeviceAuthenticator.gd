# res://security360/mobile/DeviceAuthenticator.gd
class_name DeviceAuthenticator
extends SecurityModule

var trusted_devices = ["dev-001", "dev-002"]
var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("📱 [DeviceAuthenticator] Đã khởi động.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    if event_type == "DEVICE_LOGIN":
        _authenticate(data.device_id, data.user)

func _authenticate(device_id: String, user: String):
    if device_id in trusted_devices:
        logger.info("✅ [DeviceAuth] Thiết bị %s được xác thực" % device_id)
        Security360.events.emit("DEVICE_AUTH_SUCCESS", {device: device_id, user: user})
    else:
        logger.warn("❌ [DeviceAuth] Thiết bị lạ: %s" % device_id)
        Security360.events.emit("DEVICE_AUTH_FAIL", {device: device_id, user: user})
        Security360.events.emit("RISKY_LOGIN_ATTEMPT", {device: device_id})

func stop():
    logger.info("🛑 [DeviceAuthenticator] Đã tắt.")