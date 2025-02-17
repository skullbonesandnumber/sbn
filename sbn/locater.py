# This file is placed in the Public Domain.


"find objects"


import os
import time


from .caching import Cache
from .objects import Object, fqn, items, update
from .persist import read
from .workdir import long, skel, store


p = os.path.join


def fns(clz) -> [str]:
    """ return filenames of a type. """
    dname = ''
    pth = store(clz)
    for rootdir, dirs, _files in os.walk(pth, topdown=False):
        if dirs:
            for dname in sorted(dirs):
                if dname.count('-') == 2:
                    ddd = p(rootdir, dname)
                    for fll in os.listdir(ddd):
                        yield p(ddd, fll)


def fntime(daystr) -> int:
    """ return time in second for a path, """
    daystr = daystr.replace('_', ':')
    datestr = ' '.join(daystr.split(os.sep)[-2:])
    if '.' in datestr:
        datestr, rest = datestr.rsplit('.', 1)
    else:
        rest = ''
    timed = time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))
    if rest:
        timed += float('.' + rest)
    return timed


def find(clz, selector=None, deleted=False, matching=False) -> [Object]:
    """ find matching object of a type. """
    skel()
    pth = long(clz)
    res = []
    for fnm in fns(pth):
        obj = Cache.get(fnm)
        if not obj:
            obj = Object()
            read(obj, fnm)
            Cache.add(fnm, obj)
        if not deleted and '__deleted__' in dir(obj) and obj.__deleted__:
            continue
        if selector and not search(obj, selector, matching):
            continue
        res.append((fnm, obj))
    return sorted(res, key=lambda x: fntime(x[0]))


def last(obj, selector=None) -> Object:
    """ update object to last saved version. """
    if selector is None:
        selector = {}
    result = sorted(
                    find(fqn(obj), selector),
                    key=lambda x: fntime(x[0])
                   )
    res = None
    if result:
        inp = result[-1]
        update(obj, inp[-1])
        res = inp[0]
    return res


def search(obj, selector, matching=None) -> bool:
    """ search an object for matching items in the selector. """
    res = False
    if not selector:
        return res
    for key, value in items(selector):
        val = getattr(obj, key, None)
        if not val:
            continue
        if matching and value == val:
            res = True
        elif str(value).lower() in str(val).lower() or value == "match":
            res = True
        else:
            res = False
            break
    return res


def __dir__():
    return (
        'fns',
        'fntime',
        'find',
        'last',
        'search'
    )
