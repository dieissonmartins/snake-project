# Python3 program to

import datetime
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
        class_name = "Main"
        script_name = sys.argv[1]

        # __import__ method used
        # to fetch module
        module = __import__("scripts." + script_name + ".main")

        script = import_module(module)

        # getting attribute by
        # getattr() method
        #script = getattr(module, class_name)
        script.run()

    def data_base(self):
        self.con = con



# object instantiation
execute = index()
