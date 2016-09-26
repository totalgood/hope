#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Hope chatbot in your terminal (console)"""
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import str

import os
import argparse
import sys
import logging
from termcolor import colored
import getpass
import datetime

import django
# from django.core.wsgi import get_wsgi_application
import chatterbot_app.settings

from hope import __version__
from .constants import DB_PATH

from chatterbot import ChatBot
# from chatterbot.django_storage import DjangoStorageAdapter

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wake_hope(name="Hope", human_name="", loglevel=logging.INFO, database=DB_PATH):
    name = name or 'Hope'
    human_name = human_name or getpass.getuser().title()
    loglevel = loglevel or logging.INFO
    database = database or DB_PATH
    logging.basicConfig(level=loglevel, stream=sys.stdout)
    bot = ChatBot(
        "Terminal",
        storage_adapter="chatterbot.adapters.storage.django_storage.DjangoStorageAdapter",
        logic_adapters=[
            "chatterbot.adapters.logic.MathematicalEvaluation",
            "chatterbot.adapters.logic.TimeLogicAdapter",
            "chatterbot.adapters.logic.ClosestMatchAdapter"
        ],
        input_adapter="chatterbot.adapters.input.TerminalAdapter",
        output_adapter="chatterbot.adapters.output.TerminalAdapter",
        database=database,
    )

    now = datetime.datetime.now()
    today = datetime.datetime(*now.timetuple()[:3])
    noon = datetime.datetime(*now.timetuple()[:3]) + datetime.timedelta(.5)
    # midnight = noon + datetime.timedelta(.5)  # noqa
    early_morn = today + datetime.timedelta(3. / 24.)
    evening = today + datetime.timedelta(18. / 24.)
    tod = 'morning' if early_morn < now < noon else ('afternoon' if noon <= now < evening else 'evening')
    print("Good {}{}.".format(tod, '' if not human_name else ' ' + human_name))

    while True:
        try:
            # TerminalAdapter doesn't require any args
            bot_input = bot.get_response(None)
            print(colored(str(bot_input) + '\r', 'yellow'))

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


def parse_args(args):
    """
    Parse command line parameters

    :param args: command line parameters as list of strings
    :return: command line parameters as :obj:`argparse.Namespace`
    """
    parser = argparse.ArgumentParser(
        description="Simple ChatterBot on stdin and stdout with database at {}".format(DB_PATH))
    parser.add_argument(
        '--version',
        action='version',
        version='hope {ver}'.format(ver=__version__))
    parser.add_argument(
        '-d',
        '--db',
        '--dbpath',
        '--db-path',
        '--database',
        '--database-path',
        dest="database",
        default=DB_PATH,
        help="Path to sqlite3 database file",
        type=str,
        metavar="DB_PATH")
    parser.add_argument(
        '-n',
        '--name',
        '--nick'
        '--nickname',
        dest="name",
        default='hope',
        help="Bot's @name",
        type=str,
        metavar="BOTNAME")
    parser.add_argument(
        '-u',
        '--username',
        '--user-name',
        '--human',
        '--human-name',
        dest="human_name",
        default=None,
        help="Human's @name",
        type=str,
        metavar="USERNAME")
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    args.name = args.name.rstrip(':').lstrip('@')
    logger.debug("Waking {}...".format(args.name))
    wake_hope(name=args.name, loglevel=args.loglevel, database=args.database)
    logger.info("{} is asleep.".format(args.name.title()))


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatterbot_app.settings")
    # application = get_wsgi_application()
    # chatterbot_app.settings.configure()
    django.setup()
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
