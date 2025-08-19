# res://security360/scenarios/AttackSimulator.gd
class_name AttackSimulator
extends SecurityModule

var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🧪 [AttackSimulator] Kịch bản tấn công đã sẵn sàng.")

func simulate_sql_injection():
    logger.info("💥 [Simulator] Khởi động tấn công SQLi...")
    var request = {
        url: "/login",
        body: "username=admin' OR 1=1--",
        ip: "44.55.66.77",
        method: "POST"
    }
    Security360.events.emit("HTTP_REQUEST", {request: request})

func simulate_brute_force():
    logger.info("💥 [Simulator] Khởi động tấn công Brute Force...")
    for i in range(6):
        var login = {
            username: "admin",
            password: "wrong%d" % i,
            ip: "99.88.77.66",
            time: OS.get_unix_time()
        }
        Security360.events.emit("LOGIN_FAILED", login)

func simulate_malware_upload():
    logger.info("💥 [Simulator] Tải lên mã độc giả lập...")
    var malicious_code = 'X5O!P%@AP[4\\PZX54(P^)7CC)7}$:EICAR-STANDARD-ANTIVIRUS-TEST-FILE'
    Security360.events.emit("FILE_UPLOAD", {
        filename: "eicar.txt",
        file_content: malicious_code
    })

func stop():
    logger.info("🛑 [AttackSimulator] Đã tắt.")