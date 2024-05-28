
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot_plugin_alconna import on_alconna, Alconna, Subcommand, Option, Args, Arparma

get_perm = on_alconna(
    Alconna(
        "perm",
        Option(
            "self"
        ),
        Option(
            "user",
            Args["uid", int]
        ),
        Option(
            "group",
            Args["uid", int]
        )
    )
)

@get_perm.handle()
async def _(bot: Bot, event: GroupMessageEvent, result: Arparma):
    if result.find("self"):
        pass