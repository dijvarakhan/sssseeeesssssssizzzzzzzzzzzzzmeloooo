# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "39772794"))
        self.API_HASH = getenv("API_HASH", "2ee2ed0c08035c3264f864e5e12f37c7")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8227251406:AAGNy_6yQGnmW7JDLaEu5rGveW7dw2eZ9Qo")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003682183380"))
        self.OWNER_ID = int(getenv("OWNER_ID", "7932897819"))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 50))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "AQJe4noAfnPIh8ysCl2UKz5Ppv4B7SzNgKt30WCv8BbOWIalOJ3LY6SGmLehKXkTHK473gwwCtQUfh5hNkud3PuEV-xKaIsZ-fNh0-r7NNd7-FYM4VA0piRBozExR72Cw66fIWWV1rWltb6DZlobahUicpUUGBCB5rhypwf3udFJqDYmm4nfpuMDoZZj801iS8FyKWPpmUyi39yuKuxS9sCAhTE9--7Ej81gVPfM_HUeC9trOPGA09c6583FVzM4PYE1qtNNaLd5af3ca0uTpgeI8lVgHv3MGm1je0NSX81_WaZ9pADxXvVGYnQWnnvyuAtjrQqgZu6gUAHmsF7CZbXtbfySdgAAAAHacLhZAA")
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
            url for url in getenv("COOKIES_URL", "https://batbin.me/algological").split(" ")
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
