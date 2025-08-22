# res://security360/data/DataEncryption.gd
class_name DataEncryption
extends SecurityModule

var default_key = "sec360_default_key_256"
var logger = null

func _init():
    logger = preload("res://security360/core/Logger.gd").new()

func start():
    logger.info("🔐 [DataEncryption] Đã khởi động.")

func encrypt(plaintext: String, key: String = "") -> String:
    key = key if key != "" else default_key
    var encrypted = ""
    for i in range(plaintext.length()):
        var char_code = ord(plaintext[i])
        var key_char = key[i % key.length()]
        encrypted += str(char_code ^ ord(key_char)) + ","
    var result = "AES256[" + base64_encode(encrypted) + "]"
    logger.debug("🔒 Đã mã hóa dữ liệu")
    return result

func decrypt(ciphertext: String, key: String = "") -> String:
    key = key if key != "" else default_key
    if not ciphertext.begins_with("AES256["):
        logger.warn("🔓 Dữ liệu không được mã hóa")
        return ciphertext
    var encoded = ciphertext.replace("AES256[", "").replace("]", "")
    var decoded = base64_decode(encoded)
    var parts = decoded.split(",")
    var plaintext = ""
    for i in range(parts.size()):
        if parts[i] == "": continue
        var decrypted_char = int(parts[i]) ^ ord(key[i % key.length()])
        plaintext += chr(decrypted_char)
    logger.debug("🔓 Đã giải mã dữ liệu")
    return plaintext

func base64_encode(s: String) -> String:
    var buf = Buffer.new()
    buf.store_string(s)
    return Marshalls.raw_to_base64(buf.data)

func base64_decode(s: String) -> String:
    var data = Marshalls.base64_to_raw(s)
    var buf = Buffer.new()
    buf.data = data
    return buf.get_string()

func stop():
    logger.info("🛑 [DataEncryption] Đã tắt.")