# ./Tests.py
# 这个测试脚本用于对Bot的函数和连接等进行测试并生成测试日志
# 通过注释对应的函数可以跳过指定测试
import os.path
import time
from functools import wraps

import dotenv

from Utils.EnvGenerator import env
from Utils.Logger import logger


# 计时器函数
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} 使用了{elapsed_time:.4f}s")
        return result
    return wrapper


# Log测试
@timeit
def log_test():
    logger.success("这是一条SUCCESS!")
    logger.fail("这是一条FAIL!")
    logger.info("这是一条INFO!")
    logger.debug("这是一条DEBUG!")
    logger.warning("这是一条WARNING!")
    logger.error("这是一条ERROR!")
    try:
        if os.path.exists("./Logs"):
            logger.debug("Logs文件夹存在。")
        if os.path.exists(f"./Logs/{logger.log_file_name()}"):
            logger.debug("日志文件存在。")
        logger.success("LOG测试通过。")
    except Exception as e:
        logger.error(f"LOG测试失败。{e}")


@timeit
def env_test():
    dotenv.load_dotenv(".env")
    backup_host = os.getenv("HOST")
    backup_port = int(os.getenv("PORT"))
    try:
        env.set_host("1.2.3.4")
        env.set_port(8888)
        env.write()
        env.load()
        if os.getenv("HOST") == "1.2.3.4" and os.getenv("PORT") == "8888":
            logger.success("ENV测试通过。")
    except Exception as e:
        logger.error(f"ENV测试失败。{e}")
    finally:
        env.set_host(backup_host)
        env.set_port(backup_port)
        env.write()
        env.load()


# 执行测试
log_test()
env_test()
