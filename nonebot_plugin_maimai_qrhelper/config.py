from pydantic import BaseModel
from nonebot import get_plugin_config


class Config(BaseModel):
    """Plugin Config Here"""
    qrhelper_get_picurl: list[str]
    qrhelper_admin: list[str]
    qehelper_command: list[str] = "getqr"


config = get_plugin_config(Config)
