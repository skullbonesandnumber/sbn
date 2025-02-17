# This file is placed in the Public Domain.


"locate objects"


import time


from ..locater import find, fntime
from ..objects import fmt
from ..workdir import long, skel, types
from ..utility import elapsed


def fnd(event):
    skel()
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in types()])
        if res:
            event.reply(",".join(res))
        return
    otype = event.args[0]
    clz = long(otype)
    nmr = 0
    for fnm, obj in list(find(clz, event.gets)):
        event.reply(f"{nmr} {fmt(obj)} {elapsed(time.time()-fntime(fnm))}")
        nmr += 1
    if not nmr:
        event.reply("no result")


def __dir__():
    return (
        'fnd',
    )
