from os import environ as env
from dotenv import load_dotenv

# Load .env file if present (optional)
load_dotenv()

# ===============================
#   TELEGRAM CONFIGURATION
# ===============================

class Telegram:
    # === DIRECTLY ENTER YOUR VALUES HERE ===
    API_ID = 23166402                     # e.g. 12345678
    API_HASH = "d7aaaa6147e70c3ea89acb7c2dab297a"     # from https://my.telegram.org
    BOT_TOKEN = "8429216785:AAFKLAR1vT2_tKUieo6E07PDRM1P9nk6xtY"     # your bot token from @BotFather
    OWNER_ID = 8453231525                 # your Telegram user ID
    DATABASE_URL = "mongodb+srv://synixcraft0:synixcraft123@cluster0.chrxgp5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"    # or any DB URI (optional)

    # Optional extras
    WORKERS = 6                           # 6 workers = 6 commands at once
    UPDATES_CHANNEL = "Telegram"          # your updates channel (if any)
    SESSION_NAME = "FileStream"           # name of session
    FORCE_SUB_ID = None                   # your channel ID for force-subscribe
    FORCE_SUB = False                     # True/False to enable force sub
    SLEEP_THRESHOLD = 60                  # seconds
    FILE_PIC = "https://graph.org/file/5bb9935be0229adf98b73.jpg"
    START_PIC = "https://graph.org/file/290af25276fa34fa8f0aa.jpg"
    VERIFY_PIC = "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg"
    MULTI_CLIENT = False

    FLOG_CHANNEL = -1003175434313                   # file logs channel ID
    ULOG_CHANNEL = -1002805332537                   # user logs channel ID

    MODE = "primary"                      # or "secondary"
    SECONDARY = MODE.lower() == "secondary"

    # space-separated IDs of authorized users, e.g. "12345 67890"
    AUTH_USERS = [8453231525]

    # === OVERRIDE BY .env IF AVAILABLE ===
    API_ID = int(env.get("API_ID", API_ID))
    API_HASH = str(env.get("API_HASH", API_HASH))
    BOT_TOKEN = str(env.get("BOT_TOKEN", BOT_TOKEN))
    OWNER_ID = int(env.get('OWNER_ID', OWNER_ID))
    WORKERS = int(env.get("WORKERS", WORKERS))
    DATABASE_URL = str(env.get('DATABASE_URL', DATABASE_URL))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', UPDATES_CHANNEL))
    SESSION_NAME = str(env.get('SESSION_NAME', SESSION_NAME))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', FORCE_SUB_ID)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', FORCE_SUB)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", SLEEP_THRESHOLD))
    FILE_PIC = env.get('FILE_PIC', FILE_PIC)
    START_PIC = env.get('START_PIC', START_PIC)
    VERIFY_PIC = env.get('VERIFY_PIC', VERIFY_PIC)
    MULTI_CLIENT = env.get('MULTI_CLIENT', MULTI_CLIENT)
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", FLOG_CHANNEL or 0)) or None
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", ULOG_CHANNEL or 0)) or None
    MODE = env.get("MODE", MODE)
    SECONDARY = MODE.lower() == "secondary"
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", " ".join(map(str, AUTH_USERS)))).split()))


# ===============================
#   SERVER CONFIGURATION
# ===============================

class Server:
    # === DIRECTLY ENTER YOUR VALUES HERE ===
    PORT = 8080
    BIND_ADDRESS = "0.0.0.0"
    PING_INTERVAL = 1200
    HAS_SSL = False
    NO_PORT = False
    FQDN = "yourdomain.com"

    # === OVERRIDE BY .env IF AVAILABLE ===
    PORT = int(env.get("PORT", PORT))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", BIND_ADDRESS))
    PING_INTERVAL = int(env.get("PING_INTERVAL", PING_INTERVAL))
    HAS_SSL = str(env.get("HAS_SSL", str(HAS_SSL)).lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", str(NO_PORT)).lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", FQDN))

    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "",
        FQDN,
        "" if NO_PORT else ":" + str(PORT)
    )
