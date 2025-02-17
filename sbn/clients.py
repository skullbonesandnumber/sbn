# This file is placed in the Public Domain.


"buffered clients"


import os
import queue
import threading


from .default import Default
from .reactor import Fleet, Reactor
from .threads import launch


class Config(Default):

    init    = ""
    name    = __file__.rsplit(os.sep, maxsplit=2)[-2]
    opts    = Default()
    version = 180


class Client(Reactor):

    def __init__(self):
        Reactor.__init__(self)
        Fleet.add(self)

    def raw(self, txt) -> None:
        raise NotImplementedError("raw")

    def say(self, channel, txt) -> None:
        self.raw(txt)


class Output:

    def __init__(self):
        self.oqueue   = queue.Queue()
        self.running = threading.Event()

    def loop(self) -> None:
        self.running.set()
        while self.running.is_set():
            evt = self.oqueue.get()
            if evt is None:
                self.oqueue.task_done()
                break
            Fleet.display(evt)
            self.oqueue.task_done()

    def oput(self,evt) -> None:
        if not self.running.is_set():
            Fleet.display(evt)
        self.oqueue.put(evt)

    def start(self) -> None:
        if not self.running.is_set():
            self.running.set()
            launch(self.loop)

    def stop(self) -> None:
        self.running.clear()
        self.oqueue.put(None)

    def wait(self) -> None:
        self.oqueue.join()
        self.running.wait()


class Buffered(Client, Output):

    def __init__(self):
        Client.__init__(self)
        Output.__init__(self)

    def raw(self, txt) -> None:
        raise NotImplementedError("raw")

    def start(self) -> None:
        Output.start(self)
        Client.start(self)

    def stop(self) -> None:
        Output.stop(self)
        Client.stop(self)

    def wait(self) -> None:
        Output.wait(self)
        Client.wait(self)


def __dir__():
    return (
        'Cached',
        'Client',
        'Config',
        'Output',
        'debug',
        'output'
    )
