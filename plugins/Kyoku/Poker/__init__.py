from io import BytesIO

from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot_plugin_alconna import on_alconna
from arclet.alconna import Alconna
from Core.Pokercards import poker
import PIL.Image

poker_event = on_alconna(
    Alconna(
        "poker"
    )
)


@poker_event.handle()
async def _(event: GroupMessageEvent):
    # 定义一个转换字典
    converting = {
        "spade": "♠黑桃",
        "heart": "♥红桃",
        "diamond": "♦方片",
        "club": "♣梅花",
        "j": "Jack",
        "q": "Queen",
        "k": "King",
        "joker": "JOKER"
    }
    # 抽取卡片
    card = poker.random_card()
    card_value = card["value"]
    card_shape = card["shape"]
    card_file = card["file"]
    if card_value == "joker":
        card_value = converting[card_value]
        if card_shape in ["heart", "diamond"]:
            card_shape = "RED"
        else:
            card_shape = "BLACK"
    else:
        if card_value in ["j", "q", "k"]:
            card_value = converting[card_value]
        card_shape = converting[card_shape]

    # 组合出卡片名称
    card_name = f"{card_shape} {card_value}"
    # 读取图片
    img = PIL.Image.open(card_file)
    img_arr = BytesIO()
    img.save(img_arr, format='png')

    await poker_event.finish(
        MessageSegment.text("Poker >>>\n\n") +
        MessageSegment.at(event.user_id) +
        MessageSegment.text(f"\n你抽到的扑克牌为......\n{card_name}！") +
        MessageSegment.image(img_arr)
    )
