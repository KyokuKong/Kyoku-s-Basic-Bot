# ./Utils/EnvGenerator.py
# 用于实现一个可以自动生成Env环境配置文件的类
from dotenv import load_dotenv
import os


class EnvGenerator:
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 8080
        self.command_start = ['']
        self.command_sep = ['.']
        self.driver = "~fastapi+~httpx+~websockets"
        self.is_auto_update = True
        self.repo = "https://github.com/KyokuKong/Kyoku-s-Basic-Bot.git"
        if not os.path.exists(".env"):
            self.write()
        pass

    def write(self):
        env_content = f"""# 自动生成的.env文件
HOST={self.host}
PORT={self.port}
COMMAND_START={self.command_start}
COMMAND_SEP={self.command_sep}
DRIVER={self.driver}
IS_AUTO_UPDATE={self.is_auto_update}
REPO={self.repo}
        """
        with open(".env", "w+", encoding="utf-8") as env:
            env.write(env_content)
            env.close()

    def load(self):
        self.host = self.get("HOST")
        self.port = self.get("PORT")
        self.command_start = self.get("COMMAND_START")
        self.command_sep = self.get("COMMAND_SEP")
        self.driver = self.get("DRIVER")
        self.is_auto_update = self.get("IS_AUTO_UPDATE")
        self.repo = self.get("REPO")

    @staticmethod
    def get(key: str):
        load_dotenv(".env")
        res = os.getenv(key)
        if res:
            return res

    def set_host(self, host: str):
        self.host = host

    def set_port(self, port: int):
        # 安全起见
        if 0 <= port <= 65536 and isinstance(port, int):
            self.port = port


# 实现单例
env = EnvGenerator()
