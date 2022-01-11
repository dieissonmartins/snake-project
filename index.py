# Python3 program to

import datetime
from scripts.math import Math
import logging
import sys
from utils.conn import con
from sys import argv


class index:
    # attribute
    today = datetime.datetime.now()
    con = ''

    def __init__(self):
        # start logger infos
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

        logging.info(" ", self.today.strftime("%Y-%m-%d"))

        # connect database
        self.data_base()

        # get params args
        script_name = sys.argv[1]

        teste = 2;

    def data_base(self):
        self.con = con


# object instantiation
execute = index()
