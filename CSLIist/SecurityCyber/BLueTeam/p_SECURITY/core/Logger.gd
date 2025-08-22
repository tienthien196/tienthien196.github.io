# res://security360/core/Logger.gd
class_name SecurityLogger

enum Level { DEBUG, INFO, WARN, ERROR, CRITICAL }

var level_names = ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]

# Có thể bật/tắt theo mức
var min_log_level = Level.INFO

func log(msg: String, level: int = Level.INFO):
    if level < min_log_level:
        return
    var level_str = level_names[level]
    var timestamp = _get_timestamp()
    var formatted = "[%s] [%s] %s" % [timestamp, level_str, msg]
    print(formatted)

func debug(msg: String):
    log(msg, Level.DEBUG)

func info(msg: String):
    log(msg, Level.INFO)

func warn(msg: String):
    log(msg, Level.WARN)

func error(msg: String):
    log(msg, Level.ERROR)

func critical(msg: String):
    log(msg, Level.CRITICAL)

func _get_timestamp() -> String:
    var t = OS.get_datetime()
    return "%04d-%02d-%02d %02d:%02d:%02d" % [
        t.year, t.month, t.day,
        t.hour, t.minute, t.second
    ]