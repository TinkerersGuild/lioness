########
# Base URL storer
######
import sys
from plugins import PluginResponse, Plugin
import requests
import html2text

class store(Plugin):
    def __init__(self, dbconn):
        self.keyword = ("store",)
        self.response = PluginResponse()
        self.error = ""
        self.dbconn = dbconn


    def command(self, args):
        self.response.setText("Nope")
        text = args.text.split()
        userID = args.user["user"]["id"]
        tag = "generic"


        if (len(text) > 1):
            tag = text[-1]
            stored = " ".join(text[:-1])
        else:
            stored = text[0]
        try:
            # replace with function
            self.error = self.dbconn.query("""INSERT INTO `store`(`text`, `tag`, `userID`) VALUES(%s, %s, %s)""", (stored, tag, userID))
            self.response.setText("Added for {}!".format(args.user["user"]["name"]))
        except:
            self.response.setText("Cannot la: {}".format(self.error))


        return self.response
