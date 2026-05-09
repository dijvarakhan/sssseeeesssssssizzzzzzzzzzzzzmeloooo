# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "39772794"))
        self.API_HASH = getenv("API_HASH", "2ee2ed0c08035c3264f864e5e12f37c7")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8227251406:AAHNrusnGZqCiHcGbWOnsEtlP_KkRZ71Oes")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003682183380"))
        self.OWNER_ID = int(getenv("OWNER_ID", "7932897819"))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 50))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "AQJe4noAvAyggCZOI-Rmm6d0SBShUI0h8CbEcIcCQX8Foc3P50B_krkdmZlkhYJHpvk4fq3Bq5Ro9NKv4_PmXBLKhHO5SkNa2noKOjeRaLqNmVBS_myZ6VkrnB4Z9mJmxd0iYrha9GRpUGui6SAuzpQYz7ns9XQtbulfBTE3XWDd3QkRKPD686YSMgYVm55HGwtZm3028u3AqaUEinWVyJtlzlTIm8M90AEk-0j4qhZnJ4ZHUdLEyfYPU_SauaPTce4MnrYRZQK-JGH09qb4FGXK_6626IHR59rvlF_0ssa1K1oP9EptLFIYwiYApJjejDrd158x32qLT55UI__8Y4nQ_XlNhwAAAAHacLhZAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SessizMelodim")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SessizMelodim")

        def parse_bool(key: str, default: bool) -> bool:
            val = getenv(key)
            if val is None:
                return default
            return str(val).lower() in ["true", "1", "yes"]

        self.AUTO_END: bool = parse_bool("AUTO_END", False)
        self.AUTO_LEAVE: bool = parse_bool("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = parse_bool("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/sulfurous").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", self.DEFAULT_THUMB) or self.DEFAULT_THUMB
        self.START_IMG = getenv("START_IMG", self.DEFAULT_THUMB) or self.DEFAULT_THUMB

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
