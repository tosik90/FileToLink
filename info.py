import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TsAll_channel')
API_ID = int(environ.get('API_ID', '21478717'))
API_HASH = environ.get('API_HASH', '8f8629885b7fd647e3a5006fb27c38d6')
BOT_TOKEN = environ.get('BOT_TOKEN', "8020786088:AAFNhL6vHJxEIar-RLR879Hb6NzlA6FoLII")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002339275614'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '
1807895968').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://tosikk:tosikk@tosikk.qn5eb.mongodb.net/?retryWrites=true&w=majority&appName=tosikk")
DATABASE_NAME = environ.get('DATABASE_NAME', "tosikk")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
