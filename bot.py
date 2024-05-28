# ./bot.py
# 标准的Nonebot启动程序
import nonebot
from nonebot.adapters.onebot.v11.adapter import Adapter
from Utils.EnvGenerator import env


def start_bot():
    # 初始化 NoneBot
    nonebot.init()

    # 注册适配器
    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    # 在这里加载插件
    nonebot.load_plugins("Plugins")  # 本地插件
    nonebot.load_plugins("Plugins/Basic")
    nonebot.run()
