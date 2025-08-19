# res://security360/infrastructure/ThreatIntelligence.gd
class_name ThreatIntelligence
extends SecurityModule

var malicious_ips = [
    "44.55.66.77",
    "99.88.77.66",
    "10.0.0.100"  # kẻ tấn công giả lập
]

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("📡 [ThreatIntelligence] Cơ sở dữ liệu mối đe dọa đã tải.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    if event_type == "NETWORK_CONNECTION" and data.ip in malicious_ips:
        logger.critical("🚨 [TI] Kết nối từ IP độc hại: %s" % data.ip)
        Security360.events.emit("MALICIOUS_IP_DETECTED", {ip: data.ip})
        Security360.events.emit("AUTO_BLOCK_IP", {ip: data.ip})

func is_malicious(ip: String) -> bool:
    return ip in malicious_ips

func stop():
    logger.info("🛑 [ThreatIntelligence] Đã tắt.")