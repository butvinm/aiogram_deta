from deta.base import Util

from aiogram_deta.bot.dispatcher import create_dispatcher
from aiogram_deta.space.base import DetaBase

util = Util()


__all__ = (
    "create_dispatcher",
    "DetaBase",
    "util",
)
