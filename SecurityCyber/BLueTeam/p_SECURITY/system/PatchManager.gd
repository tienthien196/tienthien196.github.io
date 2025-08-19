# res://security360/system/PatchManager.gd
class_name PatchManager
extends SecurityModule

var known_vulnerabilities = {
    "CVE-2023-1234": { product: "Apache", version: "<2.4.50", patch: "2.4.51" },
    "CVE-2023-5678": { product: "OpenSSL", version: "<1.1.1u", patch: "1.1.1v" }
}

var system_inventory = [
    { name: "Apache", version: "2.4.49", critical: true },
    { name: "OpenSSL", version: "1.1.1t", critical: true }
]

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🧩 [PatchManager] Quản lý bản vá đã khởi động.")
    Security360.events.connect("event", self, "_on_event")
    check_all()

func check_all():
    for system in system_inventory:
        for cve in known_vulnerabilities:
            var vuln = known_vulnerabilities[cve]
            if system.name == vuln.product and _is_vulnerable(system.version, vuln.version):
                logger.critical("🚨 [PatchManager] Hệ thống %s (v%s) bị ảnh hưởng bởi %s" % [system.name, system.version, cve])
                Security360.events.emit("PATCH_REQUIRED", {
                    cve: cve,
                    product: system.name,
                    current: system.version,
                    required: vuln.patch
                })

func _is_vulnerable(current: String, required: String) -> bool:
    # So sánh đơn giản: giả sử "2.4.49" < "2.4.50"
    return current < required.replace("<", "").strip_edges()

func apply_patch(product: String, version: String):
    for system in system_inventory:
        if system.name == product:
            system.version = version
            logger.info("✅ [PatchManager] Đã cập nhật %s lên v%s" % [product, version])
            Security360.events.emit("PATCH_APPLIED", {product: product, version: version})
            return
    logger.warn("❌ [PatchManager] Không tìm thấy sản phẩm: %s" % product)

func _on_event(event_type: String, data: Dictionary):
    if event_type == "VULNERABILITY_FOUND":
        check_all()

func stop():
    logger.info("🛑 [PatchManager] Đã tắt.")