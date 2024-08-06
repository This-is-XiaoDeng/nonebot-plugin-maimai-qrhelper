from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters import Message, Event
from nonebot_plugin_alconna import UniMessage
import io
from PIL import Image
import httpx
from pyzbar import pyzbar
from .config import config


def check_permission(event: Event) -> bool:
    user_id = event.get_user_id()
    return event.get_session_id() == user_id or config.allow_group_sendqr and user_id in config.qrhelper_admins


matcher = on_command(config.qrhelper_command, rule=check_permission)


@matcher.handle()
async def _(argv: Message = CommandArg()) -> None:
    url = config.qrhelper_get_picurl[int(argv.extract_plain_text()) - 1]
    if not config.send_qr_msg:
        await matcher.finish(await UniMessage().image(url=url).export())
    else:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        image = Image.open(io.BytesIO(response.read()))
        barcode = pyzbar.decode(image)
        await matcher.finish(barcode[0].data.decode('utf-8'))
