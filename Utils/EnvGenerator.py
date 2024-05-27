# ./Utils/EnvGenerator.py
# 用于实现一个可以自动生成Env环境配置文件的类
from dotenv import load_dotenv
import os


class EnvGenerator:
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 8080
        self.command_start = '""'
        self.command_sep = '"."'
        self.driver = "DRIVER=~fastapi+~httpx+~websockets"
        pass

    def write(self):
        env_content = f"""
HOST={self.host}
PORT={self.port}
COMMAND_START=[{self.command_start}]
COMMAND_SEP=[{self.command_sep}]
DRIVER={self.driver}
        """
        with open(".env", "w+", encoding="utf-8") as env:
            env.write(env_content)
            env.close()

    @staticmethod
    def load():
        load_dotenv(".env")

    @staticmethod
    def get(key: str):
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
