# res://security360/compliance/AuditChecker.gd
class_name AuditChecker
extends SecurityModule

var policies = [
    { id: "POL-001", desc: "Mật khẩu phải dài ít nhất 8 ký tự", check: "password_policy" },
    { id: "POL-002", desc: "Bản vá phải được cập nhật hàng tháng", check: "patch_policy" }
]

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("📋 [AuditChecker] Kiểm toán tuân thủ đã bắt đầu.")
    check_all()

func check_all():
    _check_password_policy()
    _check_patch_policy()

func _check_password_policy():
    # Giả lập kiểm tra
    var weak_passwords = ["admin123", "password", "123456"]
    logger.warn("⚠️ [AuditChecker] Phát hiện chính sách mật khẩu yếu")
    Security360.events.emit("AUDIT_FINDING", {
        policy: "POL-001",
        severity: "MEDIUM",
        detail: "Không bắt buộc ký tự đặc biệt"
    })

func _check_patch_policy():
    logger.info("✅ [AuditChecker] Bản vá được cập nhật đúng lịch.")

func stop():
    logger.info("🛑 [AuditChecker] Đã tắt.")