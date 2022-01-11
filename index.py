# Python3 program to

import datetime
from scripts.math import Math
import logging
import sys
from utils.conn import con


class index:
    # attribute
    today = datetime.datetime.now()
    con = ''

    def __init__(self):
        # start logger infos
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

        logging.info(" ", self.today.strftime("%Y-%m-%d"))

        # connect database
        #self.data_base()

    def data_base(self):
        self.con = con


# object instantiation
execute = index()
