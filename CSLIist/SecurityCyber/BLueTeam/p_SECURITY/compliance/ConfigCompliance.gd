# res://security360/compliance/ConfigCompliance.gd
class_name ConfigCompliance
extends SecurityModule

var required_configs = {
    "firewall_enabled": true,
    "auto_update": true,
    "encryption_at_rest": true
}

var current_state = {
    "firewall_enabled": true,
    "auto_update": false,
    "encryption_at_rest": true
}

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🔧 [ConfigCompliance] Kiểm tra cấu hình...")
    check_mismatch()

func check_mismatch():
    for key in required_configs:
        if current_state[key] != required_configs[key]:
            logger.warn("⚠️ [ConfigCompliance] Sai lệch cấu hình: %s" % key)
            Security360.events.emit("CONFIG_NON_COMPLIANT", {
                setting: key,
                expected: required_configs[key],
                actual: current_state[key]
            })

func stop():
    logger.info("🛑 [ConfigCompliance] Đã tắt.")