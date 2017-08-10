########
# Base URL storer
######
import sys
from plugins import PluginResponse, Plugin

class hush(Plugin):
    def __init__(self, **kwargs):
        self.keyword = ("hush",)
        self.response = PluginResponse()
        self.error = ""
        self.bot = ""
        self.builtin = 1
        self.level = 50
        STATUS = ("QUIET", "LOUD")


    def command(self, args):
        self.response.setText("Nope")
        verbose = self.bot.verbose
        if (len(args.text) > 0):
            if (args.text == "status"):
            # Oh yay we need a flag to overrise the verbose flag to
            # report the status of hush when we're hushed ...
                self.response.setText("Currently {0}".format(STATUS[self.bot.verbose]))
            elif (args.text[0] == 1) :
                self.bot.verbose = 1
        
        self.response.setText("Set verbose to {0}".format(STATUS[self.bot.verbose]))


        return self.response
