from environs import Env
import json





env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # токен бота
GROUPS_ID = env.list("GROUPS_ID")  # 0 - айди группы, 1 - айди канала
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста


with open("data/adminconf.json", "r", encoding="UTF-8") as read_conf:
    ADMIN_CONF = json.load(read_conf)

def edit_data(key, val):
    ADMIN_CONF[key] = val
    with open("data/adminconf.json", "w", encoding="UTF-8") as edit_conf:
        json.dump(ADMIN_CONF, edit_conf, ensure_ascii=False, indent=4)