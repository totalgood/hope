#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Score statements stored in Hope's memory"""
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import str

import os
import argparse
import sys
import logging

import django
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from readability import getmeasures
from textstat.textstat import textstat


from hope import __version__
from .constants import DB_PATH

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatterbot_app.settings")
django.setup()

from chatterbot.ext.django_chatterbot.models import Statement, Response, Score  # noqa

DEFAULT_FILENAME = "newb+english.json"

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def score_statements(filename=DEFAULT_FILENAME, loglevel=logging.INFO, database=DB_PATH):
    sia = SentimentIntensityAnalyzer()
    for i, statement in enumerate(Statement.objects.iterator()):
        s = sia.polarity_scores(statement.text)
        score = Score(positive=s['pos'], negative=s['neg'], neutral=s['neu'], compound=s['compound'],
                      intensity=abs(s['compound']))
        words = statement.text.split()
        if len(words) and any(words):
            superficial_measures = getmeasures(words)
            score.flesch = superficial_measures['readability grades']['FleschReadingEase']
            score.kincaid = superficial_measures['readability grades']['Kincaid']
            score.dale_chall = textstat.dale_chall_readability_score(statement.text)
        else:
            score.flesch = 0
            score.kincaid = 0
            score.dale_chall = 0
        score.save()
        statement.score = score
        statement.save()
        print(statement.score)
    return i


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
        help="Full path or relative path (to the data/ dir) to a lexicon file for the VADER algorithm",
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
    num_statements = score_statements(filename=args.filename, loglevel=args.loglevel, database=args.database)

    logger.info("{} statements in DB were scored.".format(num_statements))


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatterbot_app.settings")
    django.setup()
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
