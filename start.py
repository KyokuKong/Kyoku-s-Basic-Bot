# ./start.py
# 整个项目的核心启动脚本
from Utils.EnvGenerator import env
from bot import start_bot
import threading
from nonebot.log import logger

# 初始化env环境
logger.info("正在初始化.env")
env.load()

# 定义需要作为一个线程启动的函数
logger.info("正在启动Nonebot")
start_bot()
