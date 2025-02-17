# This file is placed in the Public Domain.


"show uptime/version"


import time


from ..clients import Config
from ..package import STARTTIME
from ..utility import elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))


def ver(event):
    event.reply(f"{Config.name.upper()} {Config.version}")


def __dir__():
    return (
        'upt',
        'ver'
    )
