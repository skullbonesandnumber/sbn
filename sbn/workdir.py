# This file is placed in the Public Domain.
# pylint: disable=R0903


"working directory"


import os
import pathlib


p = os.path.join


class Workdir:

    """ Workdir """

    wdr  = ""


def long(name) -> str:
    """ expand class name to full qualified name. """
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def pidname(name) -> str:
    """ return path for pidfile. """
    return p(Workdir.wdr, f"{name}.pid")


def skel() -> str:
    """ create necesarry directories, """
    path = pathlib.Path(store())
    path.mkdir(parents=True, exist_ok=True)
    return path


def store(pth="") -> str:
    """ return storage directory, """
    return p(Workdir.wdr, "store", pth)


def strip(pth, nmr=3) -> str:
    """ strip from path. """
    return os.sep.join(pth.split(os.sep)[-nmr:])

def types() -> [str]:
    """ return all types in store. """
    return os.listdir(store())


def __dir__():
    return (
        'Workdir',
        'long',
        'pidname',
        'skel',
        'store',
        'types'
    )
