# ./Utils/Logger.py
# 用于实现日志功能的类
import datetime
import os
import time
import types

from colorama import Fore, Back, Style, init
import inspect


class Logger:
    def __init__(self):
        self.name = "Log"
        self.is_file = True
        self.is_stream = True
        self.start_time = time.time()
        self.file_name = self.log_file_name()
        self.colors = [
            ["SUCCESS", Fore.GREEN, Fore.GREEN, Back.RESET],  # 文本，标志色，文本颜色，背景颜色
            ["FAIL", Fore.RED, Fore.RED, Back.RESET],
            ["INFO", Fore.RESET, Fore.RESET, Back.RESET],
            ["DEBUG", Fore.CYAN, Fore.CYAN, Back.RESET],
            ["WARING", Fore.YELLOW, Fore.YELLOW, Back.RESET],
            ["ERROR", Fore.RED, Fore.YELLOW, Back.RED]
        ]

    def log_file_name(self):
        log_name = f"{self.name}-{datetime.datetime.fromtimestamp(self.start_time).strftime("%Y%m%d-%H-%M-%S")}.log"
        return log_name

    def log_print(self, *args: str | int | float | tuple, level: int, previous_frame: types.FrameType):
        # 获取基本信息
        now_time = datetime.datetime.now()
        level_name = self.colors[level][0]
        # 获取当前函数的上一级函数的信息
        filename, line_number, function_name, _, _ = inspect.getframeinfo(previous_frame)
        # 拼接文本
        content = u""
        for i in args:
            content = u"{}{}".format(content, str(i))

        # 向终端打印日志文本
        if self.is_stream:
            # 生成返回的文本
            reset = Fore.RESET
            back_reset = Back.RESET
            first_color = self.colors[level][1]
            text_color = self.colors[level][2]
            back_color = self.colors[level][3]
            print(f"{reset}[{first_color}{level_name}{reset}] {reset}{now_time.strftime('%Y-%m-%d %H:%M:%S')} |", f"{function_name}:{line_number}", text_color, back_color, content, back_reset, reset)
        # 向日志文件中传入日志
        if self.is_file:
            if not os.path.exists("./Logs"):
                os.mkdir("./Logs")
            with open(f"./Logs/{self.file_name}", "a+", encoding='utf-8') as f:
                f.write(
                    f"[{level_name}] {now_time.strftime('%Y-%m-%d %H:%M:%S')} --- {function_name}:{line_number} {content}\n"
                )
            pass

    def success(self, *args):
        previous_frame = inspect.currentframe().f_back
        self.log_print(*args, level=0, previous_frame=previous_frame)

    def fail(self, *args):
        previous_frame = inspect.currentframe().f_back
        self.log_print(*args, level=1, previous_frame=previous_frame)

    def info(self, *args):
        previous_frame = inspect.currentframe().f_back
        self.log_print(*args, level=2, previous_frame=previous_frame)

    def debug(self, *args):
        previous_frame = inspect.currentframe().f_back
        self.log_print(*args, level=3, previous_frame=previous_frame)

    def warning(self, *args):
        previous_frame = inspect.currentframe().f_back
        self.log_print(*args, level=4, previous_frame=previous_frame)

    def error(self, *args):
        previous_frame = inspect.currentframe().f_back
        self.log_print(*args, level=5, previous_frame=previous_frame)


# 实现单例
logger = Logger()
