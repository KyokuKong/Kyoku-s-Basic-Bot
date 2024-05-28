# ./Tests.py
# 这个测试脚本用于对Bot的函数和连接等进行测试并生成测试日志
# 通过注释对应的函数可以跳过指定测试
import os.path
import time
from functools import wraps
from Utils.EnvGenerator import env
from Core.Permission import perms
from nonebot.log import logger


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
    logger.critical("这是一条FAIL!")
    logger.info("这是一条INFO!")
    logger.debug("这是一条DEBUG!")
    logger.warning("这是一条WARNING!")
    logger.error("这是一条ERROR!")


@timeit
def env_test():
    env.load()
    backup_host = os.getenv("HOST")
    backup_port = int(os.getenv("PORT"))
    try:
        env.set_host("1.2.3.4")
        env.set_port(8888)
        env.write()
        env.load()
        if env.get("HOST") == "1.2.3.4" and env.get("PORT") == "8888":
            logger.success("ENV测试通过。")
    except Exception as e:
        logger.error(f"ENV测试失败。{e}")
    finally:
        env.set_host(backup_host)
        env.set_port(backup_port)
        env.write()
        env.load()


@timeit
def perm_test():
    try:
        perms.add_user_perm(123456789, "SUPERUSER")
        perms.add_group_perm(34567890, "SUPERGROUP")
        item1 = perms.is_permission(123456789, 0, 3)
        item2 = perms.is_permission(123456789, 0, 2)
        item3 = perms.is_permission(34567890, 1, 1)
        if item1 and item2 and item3 and item1 is True:
            logger.success("Permssion测试通过。")
    except Exception as e:
        logger.error(f"Permssion测试失败。{e}")
    finally:
        perms.del_user_perm(123456789, "SUPERUSER")
        perms.del_group_perm(34567890, "SUPERGROUP")


# 执行测试
log_test()
env_test()
perm_test()
