from environs import Env
import json
#from utils.db_api import GetData
import utils.db_api.get_data





env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # токен бота
GROUPS_ID = env.list("GROUPS_ID")  # 0 - айди группы, 1 - айди канала
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста



class

def edit_data(key, val):
    ADMIN_CONFS = read_admin_conf()
    ADMIN_CONFS[key] = val
    with open("data/adminconf.json", "w", encoding="UTF-8") as edit_conf:
        json.dump(ADMIN_CONFS, edit_conf, ensure_ascii=False, indent=4)

def read_admin_conf():
    with open("data/adminconf.json", "r", encoding="UTF-8") as read_conf:
         return json.load(read_conf)

def update_user_data():
    result = utils.db_api.get_data.GetData().get_all_data()

ADMIN_CONF = read_admin_conf()
USER_DATA = update_user_data()