from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters import Message, Event
from nonebot.adapters.onebot.v11 import Event
from nonebot_plugin_alconna import UniMessage
from .config import config

matcher = on_command(config.qehelper_command)


@matcher.handle()
async def _(event: Event, argv: Message = CommandArg()) -> None:
    user_id = event.get_user_id()
    if event.get_session_id() == user_id and user_id in config.qrhelper_admin:
        await matcher.finish(await UniMessage().image(
            url=config.qrhelper_get_picurl[int(argv.extract_plain_text()) - 1]
        ).export())
    else:
        await matcher.finish("权限不足")
