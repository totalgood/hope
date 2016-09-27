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
import datetime
import json

import django
# from django.core.wsgi import get_wsgi_application
import chatterbot_app.settings

from hope import __version__
from .constants import DB_PATH
from pugnlp import PrettyDict

from chatterbot import ChatBot
from chatterbot.django_storage import DjangoStorageAdapter

DEFAULT_FILENAME = "newb+english.json"

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_json(filename=DEFAULT_FILENAME, loglevel=logging.INFO, database=DB_PATH):
    full_path = os.path.join(os.path.dirname(os.path.abspath(database)), filename)
    full_path = filename if not os.path.isfile(full_path) else full_path
    with open(full_path) as fin:
        js = json.load(fin)
    js = js.get('export', js)
    print(PrettyDict(js))
    return js


def parse_args(args):
    """Parse command line parameters

    Arguments:
      args (list of str): command line parameters

    Returns:
      argparse.Namespace: object with an attribute for each command line arg
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
        help="Path to sqlite3 database file where new records will be loaded",
        type=str,
        metavar="DB_PATH")
    parser.add_argument(
        '-f',
        '--file',
        '--filename'
        '--json',
        dest="filename",
        default=DEFAULT_FILENAME,
        help="Full path or relative path (to the data/ dir) to a json file containing a ChatBot export",
        type=str,
        metavar="FILENAME")
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
    logger.debug("Loading {} into {}...".format(args.filename, args.database))
    num_statements, num_conversations = load_json(filename=args.filename, loglevel=args.loglevel, database=args.database)
    logger.info("{} statements for {} conversations and {} exports were loaded.".format(
        num_statements, num_conversations, num_exports))


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatterbot_app.settings")
    # application = get_wsgi_application()
    # chatterbot_app.settings.configure()
    django.setup()
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
