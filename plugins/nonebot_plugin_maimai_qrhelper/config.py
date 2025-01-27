from pydantic import BaseModel
from nonebot import get_plugin_config


class Config(BaseModel):
    """Plugin Config Here"""
    qrhelper_get_picurl: list[str]
    qrhelper_admin: list[str]
    qrhelper_command: list[str] = "getqr"
    allow_group_sendqr: bool = False
    send_qr_msg: bool = False


config = get_plugin_config(Config)
