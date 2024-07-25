# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26305156"))
    API_HASH = getenv("API_HASH", "9937930c368c669ca905e9a95aa712f0")
    BOT_TOKEN = getenv("BOT_TOKEN", "7007126322:AAHTayEwGCf8DHr7fCwivCJUwN8mWN-xLZ8")
    FSUB = getenv("FSUB", "cinemaworld_update")
    CHID = int(getenv("CHID", "-1002042800413"))
    SUDO = list(map(int, getenv("SUDO", "7040444713").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://by:by@kalki.nqe5pac.mongodb.net/?retryWrites=true&w=majority&appName=kalki")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
