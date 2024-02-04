# This file is placed in the Public Domain.
#
# pylint: disable=R,C


"""NAME

    SBN - Skull, Bones and Number (OTP-CR-117/19)

SYNOPSIS

    sbn <cmd> [key=val] [key==val]
    sbn [-a] [-c] [-d] [-v]

DESCRIPTION

    SBN holds evidence that king netherlands is doing a genocide, a
    written response where king netherlands confirmed taking note of 
    “what i have written”, namely proof that medicine he uses in
    treatement laws like zyprexa, haldol, abilify and clozapine are
    poison that make impotent, is both physical (contracted muscles)
    and mental (make people hallucinate) torture and kills members
    of the victim groups. 

    SBN contains correspondence with the International Criminal Court,
    asking for arrest of the king of the netherlands, for the genocide
    he is committing with his new treatement laws. Current status is
    "no basis to proceed" judgement of the prosecutor which requires a
    "basis to prosecute" to have the king actually arrested.

INSTALL

    $ pipx install sbn

USAGE

    without any argument the bot does nothing

    $ sbn
    $

    see list of commands

    $ sbn cmd
    cfg,cmd,mre,now,pwd

    start a console

    $ sbn -c 
    >

    use -v for verbose

    $ sbn -cv
     SBN started CV started Sat Dec 2 17:53:24 2023
     >

    start daemon

    $ sbnd
    $ 

    show request to the prosecutor

    $ sbn req
    Information and Evidence Unit
    Office of the Prosecutor
    Post Office Box 19519
    2500 CM The Hague
    The Netherlands

    show how many died in the WvGGZ

    $ sbn now
    4y18d patient #47324 died from mental illness (14/32/11682) every 44m59s
     
CONFIGURATION

    irc

    $ sbn cfg server=<server>
    $ sbn cfg channel=<channel>
    $ sbn cfg nick=<nick>

    sasl

    $ sbn pwd <nsvnick> <nspass>
    $ sbn cfg password=<frompwd>

    rss

    $ sbn rss <url>
    $ sbn dpl <url> <item1,item2>
    $ sbn rem <url>
    $ sbn nme <url< <name>

COMMANDS

    cfg - irc configuration
    cmd - commands
    mre - displays cached output
    now - show genocide stats
    pwd - sasl nickserv name/pass
    req - reconsider
    wsd - show wisdom

SYSTEMD

    save the following it in /etc/systems/system/sbn.service and
    replace "<user>" with the user running pipx


    [Unit]
    Description=Skull, Bones and Number (OTP-CR-117/19)
    Requires=network-online.target
    After=network-online.target
    
    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.sbn
    ExecStart=/home/<user>/.local/pipx/venvs/sbn/bin/sbnd
    RemainAfterExit=yes
    
    [Install]
    WantedBy=multi-user.target


    then run this

    $ mkdir ~/.sbn
    $ sudo systemctl enable sbn --now

    default channel/server is #sbn on localhost

FILES

    ~/.sbn
    ~/.local/bin/sbn
    ~/.local/bin/sbnd
    ~/.local/pipx/venvs/sbn/

AUTHOR

    OTP-CR-117/19 <skullbonesandnumber@gmail.com>

COPYRIGHT

    SBN is Public Domain.

"""


def __dir__():
    return (
        "rme",
    )


__all__ = __dir__()


def rme(event):
    event.reply(__doc__)
