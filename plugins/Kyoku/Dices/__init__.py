from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot_plugin_alconna import on_alconna, Arparma
from arclet.alconna import Alconna, Args, Option
from typing import Optional
import random

random_dice = on_alconna(
    Alconna(
        "random",
        Args["max", [int, float]],
        Option(
            "--min|-m",
            Args["min", [int, float]]
        )
    )
)
dice = on_alconna(
    Alconna(
        "dice",
        Args["faces", Optional[int]]
    )
)
dice.shortcut("dice(\\d+)", {"args": ["{0}"]})
dice.shortcut("d(\\d+)", {"args": ["{0}"]})


@random_dice.handle()
async def _(event: GroupMessageEvent, result: Arparma):
    rmax = result.query[[int, float]]("max")
    rmin = 0
    if result.find("min"):
        rmin = result.query[[int, float]]("min")
    # 数值安全检测
    if not rmax > rmin:
        await random_dice.finish(
            MessageSegment.text("Dice >>>\n\n") +
            MessageSegment.at(event.user_id) +
            MessageSegment.text("\n传入的随机值上下限不合理！")
        )
        return
    # 数值安全，启动随机数
    print(type(rmax), type(rmin))
    # 整数处理
    if isinstance(rmax, int) and isinstance(rmin, int):
        result = random.randint(rmin, rmax)
        await random_dice.finish(
            MessageSegment.text("Dice >>>\n\n") +
            MessageSegment.at(event.user_id) +
            MessageSegment.text(f"\n随机结果：{result}")
        )
    # 浮点数处理
    # 获取输入的rmax和rmin中的最大小数位数，然后生成随机数并保留最大的小数位数
    else:
        # 获取两个数值的小数位数
        dotmax = str(rmax)
        dotmin = str(rmin)
        dotmax = dotmax.split(".")
        dotmin = dotmin.split(".")
        dotmax = len(dotmax[1]) if len(dotmax) > 1 else 0
        dotmin = len(dotmin[1]) if len(dotmin) > 1 else 0
        lenmax = max(dotmax, dotmin)
        # 生成随机数
        result = random.uniform(rmin, rmax)
        # 格式化随机数
        result = round(result, lenmax)
        await random_dice.finish(
            MessageSegment.text("Dice >>>\n\n") +
            MessageSegment.at(event.user_id) +
            MessageSegment.text(f"\n随机结果：{result}")
        )


@dice.handle()
async def _(event: GroupMessageEvent, result: Arparma):
    faces = result.query[int]("faces") if result.query[int]("faces") else 6
    result = random.randint(1, faces)
    await random_dice.finish(
        MessageSegment.text("Dice >>>\n\n") +
        MessageSegment.at(event.user_id) +
        MessageSegment.text(f"\n随机结果：{result}")
    )
