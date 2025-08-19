# res://security360/network/Firewall.gd
class_name FirewallManager
extends SecurityModule

var rules = []
var blocked_ips = []
var active_connections = []  # Mô phỏng stateful inspection
var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🔥 [Firewall] Khởi động...")
    _load_default_rules()
    Security360.events.connect("event", self, "_on_event")
    logger.info("✅ [Firewall] Đã đăng ký sự kiện.")

func _load_default_rules():
    add_rule("tcp", 80, "ALLOW", "IN")
    add_rule("tcp", 443, "ALLOW", "IN")
    add_rule("tcp", 22, "ALLOW", "IN")   # SSH
    add_rule("udp", 53, "ALLOW", "IN")   # DNS
    add_rule("any", 0, "BLOCK", "IN")    # Mặc định từ chối

func add_rule(protocol: String, port: int, action: String, direction: String):
    var rule = {
        "protocol": protocol,
        "port": port,
        "action": action,
        "direction": direction
    }
    rules.append(rule)
    logger.debug("➕ [Firewall] Thêm rule: %s %s:%d → %s" % [direction, protocol, port, action])

func block_ip(ip: String):
    if ip not in blocked_ips:
        blocked_ips.append(ip)
        Security360.events.emit("IP_BLOCKED", {"ip": ip, "source": "firewall"})
        logger.warn("🚫 [Firewall] Chặn IP: %s" % ip)

func unblock_ip(ip: String):
    if ip in blocked_ips:
        blocked_ips.erase(ip)
        logger.info("🟢 [Firewall] Bỏ chặn IP: %s" % ip)

func inspect_packet(packet: Dictionary) -> bool:
    # Kiểm tra IP bị chặn
    if packet.ip in blocked_ips:
        logger.warn("⛔ [Firewall] Từ chối gói tin từ IP bị chặn: %s" % packet.ip)
        return false

    # Kiểm tra rule
    for rule in rules:
        if rule.direction != packet.direction:
            continue
        if rule.port != 0 and rule.port != packet.port:
            continue
        if rule.protocol != "any" and rule.protocol != packet.protocol:
            continue

        if rule.action == "ALLOW":
            logger.debug("✅ [Firewall] Cho phép gói tin: %s → %s:%d" % [packet.ip, packet.protocol, packet.port])
            return true
        elif rule.action == "BLOCK":
            logger.warn("❌ [Firewall] Chặn theo rule: %s → %s:%d" % [packet.ip, packet.protocol, packet.port])
            return false

    # Mặc định từ chối (default deny)
    logger.warn("❌ [Firewall] Từ chối theo mặc định: %s → %s:%d" % [packet.ip, packet.protocol, packet.port])
    return false

func _on_event(event_type: String, data: Dictionary):
    match event_type:
        "AUTO_BLOCK_IP":
            block_ip(data.ip)
        "SIMULATE_PACKET":
            var allowed = inspect_packet(data.packet)
            if allowed:
                Security360.events.emit("PACKET_ALLOWED", data.packet)
            else:
                Security360.events.emit("PACKET_DROPPED", data.packet)

func stop():
    logger.info("🛑 [Firewall] Đã tắt.")