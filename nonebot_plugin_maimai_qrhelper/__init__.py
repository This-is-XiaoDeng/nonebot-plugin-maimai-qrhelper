from nonebot.plugin import PluginMetadata
from nonebot import require
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-maimai-qrhelper",
    description="",
    usage="",
    config=Config,
)
require("nonebot_plugin_alconna")

from . import __main__
