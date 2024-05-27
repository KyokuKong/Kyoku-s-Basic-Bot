# /Tests.py
# 这个测试脚本用于对Bot的函数和连接等进行测试并生成测试日志
import os.path
from Utils.EnvGenerator import env

# .env生成和读取测试
if os.path.exists(".env"):
    print("检测到.env环境配置文件")
    env.load()
    print(env.get("PORT"))
else:
    env.write()