########
# Passwords
######
import sys
import time
from plugins import PluginResponse, Plugin
import utils
from passlib.hash import pbkdf2_sha256


class password(Plugin):
    def __init__(self, **kwargs):
        self.keyword = ("opt",)
        self.response = PluginResponse()
        self.error = ""
        self.bot = ""
        self.builtin = 1
        self.level = -1

        self.usage = """ Set optin/out for the bot. Usage: !opt [in|out option]"""



    def command(self, args):
        self.response.setText(self.usage)
        str.strip(args.text)
        self.bot.log.warning(len(args.text))
        self.bot.log.warning("Glorp:{}:- ".format(args.text))
        resp = 'No options found'
        if (len (args.text) == 1):
            self.bot.log.warning("Listing")
            resp = self.bot.dbconn.query("""SELECT name FROM options """,())
            for opt in resp:
                self.response.setText("Option: {}".format(opt[0] ))

        else:
            text = str.split(args.text)
            
            if (text[0] == 'in'):
                self.bot.log.warning("Inning")
                resp = self.bot.dbconn.query("""INSERT INTO useropts(userID, optionID) VALUES(%s, (SELECT optionID from options WHERE name=%s)) """, (args.user["user"]["id"],text[1]))
            elif (text[0] == 'out'):
                self.bot.log.warning("outing")
                self.bot.log.warning(" delete: {} {} ".format(args.user["user"]["id"],text[1]))
                resp = self.bot.dbconn.query("""DELETE FROM useropts WHERE userID=%s AND optionID = (SELECT optionID from options WHERE name=%s) """, (args.user["user"]["id"],text[1]))


        self.bot.log.warning(resp)
        
        return self.response
