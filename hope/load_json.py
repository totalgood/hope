#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Hope chatbot in your terminal (console)"""
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import str

import os
import argparse
import sys
import logging
import json

import django
from pugnlp.util import PrettyDict

from hope import __version__
from .constants import DB_PATH

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatterbot_app.settings")
django.setup()

from chatterbot.ext.django_chatterbot.models import Statement, Response  # noqa

DEFAULT_FILENAME = "newb+english.json"

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_json(filename=DEFAULT_FILENAME, loglevel=logging.INFO, database=DB_PATH):
    full_path = os.path.join(os.path.dirname(os.path.abspath(database)), 'corpora', filename)
    full_path = filename if not os.path.isfile(full_path) else full_path
    with open(full_path) as fin:
        js = json.load(fin)
    logger.debug(str(PrettyDict(js)))
    js = js.get('export', js)
    num_statements = 0
    for prompt_and_response in js:
        print(prompt_and_response)
        prompt, p_created = Statement.objects.get_or_create(text=prompt_and_response[0])
        response, r_created = Statement.objects.get_or_create(text=prompt_and_response[1])
        pair, pair_created = Response.objects.get_or_create(prompt=prompt, response=response)
        pair.occurrence += 1
        num_statements += 2
    return num_statements


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
    logger.info("Loading {} into {}...".format(args.filename, args.database))
    total_statements = Statement.objects.count()
    total_responses = Response.objects.count()
    logger.debug("Before loading json data there were {} statements and {} unique statement-response pairs".format(
        total_statements, total_responses))

    num_statements = load_json(filename=args.filename, loglevel=args.loglevel, database=args.database)

    total_statements = Statement.objects.count()
    total_responses = Response.objects.count()
    logger.debug("After loading json data there were {} statements and {} unique statement-response pairs".format(
        total_statements, total_responses))

    logger.info("{} statements resulting in {} statements and {}  responses in the DB.".format(
        num_statements, total_statements, total_responses))


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatterbot_app.settings")
    django.setup()
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
