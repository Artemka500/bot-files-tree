import psutil
import time

from bot.database.sqlite3 import db

class Format:
    def sizeof_fmt(num: int, suffix="B"):
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, "Yi", suffix)

    def timeof_fmt(seconds: int):
        periods = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
        result = ""
        for period_name, period_seconds in periods:
            if seconds >= period_seconds:
                period_value, seconds = divmod(seconds, period_seconds)
                result += f"{int(period_value)} {period_name} "
        return result

class GetText:
    def start():
        text = "👋 <b>Привет! Я пример Telegram-бота, созданного с использованием библиотеки aiogram.\n"
        text += "Я демонстрирую правильную иерархию и архитектуру ботов.\n\n"
        text += "📂 Моя структура включает:</b>\n"
        text += "1️⃣ Четкое разделение хендлеров (обработчиков команд).\n"
        text += "2️⃣ Логику, отделенную от представления.\n"
        text += "3️⃣ Поддержку модульности и масштабируемости.\n\n"
        text += "<i>*Для примера, напишите любую команду, и я отвечу!</i>"
        return text
    
    def help():
        text = "ℹ️ <b>Я демонстрационный бот.</b>\n\n"
        text += "Вот что я умею:\n"
        text += "- Ответ на команду /start\n"
        text += "- Ответ на команду /help\n\n"
        text += "🎓 Используйте этот пример как основу для создания ваших ботов!"
        return text
    
    def admin_info(bot_info: dict):
        botStartTime = db.get_latest_log_entry(
            conditions={
                "action": "run"
            }
        )['created_at']
        cpu_usage = psutil.cpu_percent()
        total, used, free, disk = psutil.disk_usage("/")
        swap = psutil.swap_memory()
        memory = psutil.virtual_memory()
        boot_time = psutil.boot_time()
        print(bot_info['username'])
        
        text = f"\n\n<b>⌬─────「 Stats @{bot_info['username']} 」─────⌬</b>\n\n"
        text += f"<b>╭🖥️ **CPU Usage »**</b>  __{cpu_usage}%__\n"
        text += f"<b>├💾 **RAM Usage »**</b>  __{memory.percent}%__\n"
        text += f"<b>╰🗃️ **DISK Usage »**</b>  __{disk}%__\n\n"
        text += f"<b>╭📤Upload:</b> {Format.sizeof_fmt(psutil.net_io_counters().bytes_sent)}\n"
        text += f"<b>╰📥Download:</b> {Format.sizeof_fmt(psutil.net_io_counters().bytes_recv)}\n\n\n"
        text += f"<b>Memory Total:</b> {Format.sizeof_fmt(memory.total)}\n"
        text += f"<b>Memory Free:</b> {Format.sizeof_fmt(memory.available)}\n"
        text += f"<b>Memory Used:</b> {Format.sizeof_fmt(memory.used)}\n"
        text += f"<b>SWAP Total:</b> {Format.sizeof_fmt(swap.total)} | <b>SWAP Usage:</b> {swap.percent}%\n\n"
        text += f"<b>Total Disk Space:</b> {Format.sizeof_fmt(total)}\n"
        text += f"<b>Used:</b> {Format.sizeof_fmt(used)} | <b>Free:</b> {Format.sizeof_fmt(free)}\n\n"
        text += f"<b>Physical Cores:</b> {psutil.cpu_count(logical=False)}\n"
        text += f"<b>Total Cores:</b> {psutil.cpu_count(logical=True)}\n\n"
        text += f"🤖<b>Bot Uptime:</b> {Format.timeof_fmt(time.time() - botStartTime)}\n"
        text += f"⏲️<b>OS Uptime:</b> {Format.timeof_fmt(time.time() - boot_time)}\n"
        return text
