# This file is placed in the Public Domain.
# pylint: disable=R0912


"command"


import inspect
import typing


from .default import Default
from .package import Table, gettable


class Commands:

    """ Commands """

    cmds = {}
    names = gettable()

    @staticmethod
    def add(func, mod=None):
        """ add function. """
        Commands.cmds[func.__name__] = func
        if mod:
            Commands.names[func.__name__] = mod.__name__

    @staticmethod
    def get(cmd) -> typing.Callable:
        """ return command. """
        return Commands.cmds.get(cmd, None)

    @staticmethod
    def getname(cmd) -> None:
        """ return name of module containing the command. """
        return Commands.names.get(cmd)

    @staticmethod
    def scan(mod) -> None:
        """ scan modules for command. """
        for key, cmdz in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmdz.__code__.co_varnames:
                Commands.add(cmdz, mod)


def command(evt) -> None:
    """ command callback. """
    parse(evt)
    func = Commands.get(evt.cmd)
    if not func:
        mname = Commands.names.get(evt.cmd)
        if mname:
            mod = Table.load(mname)
            Commands.scan(mod)
            func = Commands.get(evt.cmd)
    if not func:
        evt.ready()
        return
    func(evt)
    evt.display()


def parse(obj, txt=None) -> None:
    """ parse text for commands. """
    if txt is None:
        if "txt" in dir(obj):
            txt = obj.txt
        else:
            txt = ""
    args = []
    obj.args    = []
    obj.cmd     = ""
    obj.gets    = Default()
    obj.index   = None
    obj.mod     = ""
    obj.opts    = ""
    obj.result  = {}
    obj.sets    = Default()
    obj.txt     = txt or ""
    obj.otxt    = obj.txt
    _nr = -1
    for spli in obj.otxt.split():
        if spli.startswith("-"):
            try:
                obj.index = int(spli[1:])
            except ValueError:
                obj.opts += spli[1:]
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            setattr(obj.gets, key, value)
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                if obj.mod:
                    obj.mod += f",{value}"
                else:
                    obj.mod = value
                continue
            setattr(obj.sets, key, value)
            continue
        _nr += 1
        if _nr == 0:
            obj.cmd = spli
            continue
        args.append(spli)
    if args:
        obj.args = args
        obj.txt  = obj.cmd or ""
        obj.rest = " ".join(obj.args)
        obj.txt  = obj.cmd + " " + obj.rest
    else:
        obj.txt = obj.cmd or ""


def __dir__():
    return (
        'Commands',
        'command',
        'cmd',
        'parse'
    )
