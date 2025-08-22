# res://security360/application/WAF.gd
class_name WebApplicationFirewall
extends SecurityModule

var signatures = {
    "sql_injection": ["' OR 1=1", "UNION SELECT", "DROP TABLE"],
    "xss": ["<script>", "javascript:", "onload="],
    "rce": ["; ls", "&& dir", "| netstat", "exec("],
    "path_traversal": ["../", "..\\", "%2e%2e/"]
}

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("/WebAPI Firewall] Đã khởi động.")
    Security360.events.connect("event", self, "_on_event")

func _on_event(event_type: String, data: Dictionary):
    if event_type == "HTTP_REQUEST":
        _inspect_request(data.request)

func _inspect_request(request: Dictionary):
    var url = request.get("url", "").to_lower()
    var body = request.get("body", "").to_lower()
    var method = request.get("method", "GET")

    for attack_type in signatures:
        for sig in signatures[attack_type]:
            if url.find(sig.to_lower()) != -1 or body.find(sig.to_lower()) != -1:
                var alert = {
                    "attack": attack_type,
                    "signature": sig,
                    "url": request.url,
                    "ip": request.ip,
                    "method": method
                }
                logger.critical("🚨 [WAF] Phát hiện tấn công %s từ %s" % [attack_type, request.ip])
                Security360.events.emit("WAF_ALERT", alert)
                Security360.events.emit("THREAT_DETECTED", {
                    "type": attack_type,
                    "severity": "HIGH",
                    "ip": request.ip
                })
                return

func stop():
    logger.info("🛑 [WAF] Đã tắt.")