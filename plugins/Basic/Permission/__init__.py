from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot_plugin_alconna import on_alconna, Arparma
from arclet.alconna import Alconna, Subcommand, Args, Option
from Core.Permission import perms

get_perm = on_alconna(
    Alconna(
        "perm",
        Subcommand(
            "self"
        ),
        Subcommand(
            "user",
            Args["uid", int]
        ),
        Subcommand(
            "change",
            Args["uid", int],
            Args["perm_name", str]
        ),
        Subcommand(
            "update"
        )
    )
)


@get_perm.handle()
async def _(bot: Bot, event: GroupMessageEvent, result: Arparma):
    if result.find("self"):
        # 获取用户的qq号和所在群的群号
        qqid = event.user_id
        groupid = event.group_id
        # 获取权限值
        user_perm_level = perms.get_permission_by_qqid(qqid)
        group_perm_level = perms.get_permission_by_groupid(groupid)
        # 返回结果
        await get_perm.finish(
            MessageSegment.text(
                f"Permission >>>\n"
                f"\n"
            ) +
            MessageSegment.at(qqid) +
            MessageSegment.text(
                f"\n你的用户权限等级为：{user_perm_level}\n"
                f"你所在的群组的权限等级为：{group_perm_level}"
            )
        )


@get_perm.handle()
async def _(bot: Bot, event: GroupMessageEvent, result: Arparma):
    if result.find("user"):
        if not perms.has_permission(event.user_id, 0, 2):
            await get_perm.finish(MessageSegment.text("你没有权限执行这个命令！"))
        else:
            # 获取命令解析到的参数
            qqid = result.query[int]("user.uid")
            # 获取其权限值
            user_perm_level = perms.get_permission_by_qqid(qqid)
            # 返回结果
            await get_perm.finish(
                MessageSegment.text(
                    f"Permission >>>\n"
                    f"\n"
                ) +
                MessageSegment.at(event.user_id) +
                MessageSegment.text(
                    f"\n你查询的用户 {qqid} 的权限值为 {user_perm_level}"
                )
            )


@get_perm.handle()
async def _(bot: Bot, event: GroupMessageEvent, result: Arparma):
    if result.find("change"):
        if not perms.has_permission(event.user_id, 0, 3):
            await get_perm.finish(MessageSegment.text("你没有权限执行这个命令！"))
        else:
            # 获取命令解析到的参数
            qqid = result.query[int]("change.uid")
            perm_name = result.query[str]("change.perm_name")
            # 添加权限
            perms.add_user_perm(qqid, perm_name)
            # 返回结果
            await get_perm.finish(
                MessageSegment.text(
                    f"Permission >>>\n"
                    f"\n"
                ) +
                MessageSegment.at(event.user_id) +
                MessageSegment.text(
                    f"\n成功为用户 {qqid} 修改了权限 {perm_name}"
                )
            )


@get_perm.handle()
async def _(bot: Bot, event: GroupMessageEvent, result: Arparma):
    if result.find("update"):
        if not perms.has_permission(event.user_id, 0, 3):
            await get_perm.finish(MessageSegment.text("你没有权限执行这个命令！"))
        else:
            perms.update_permission()
            await get_perm.finish(
                MessageSegment.text(
                    f"Permission >>>\n"
                    f"\n"
                ) +
                MessageSegment.at(event.user_id) +
                MessageSegment.text(
                    f"\n成功更新了权限"
                )
            )
