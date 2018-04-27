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
        self.keyword = ("password","auth")
        self.response = PluginResponse()
        self.error = ""
        self.bot = ""
        self.builtin = 1
        self.level = -1

        self.usage = """ Set password for the bot. Usage: !password <newpass>, no blank passwords"""



    def command(self, args):
        self.response.setText(self.usage)
        self.bot.log.warning("I think this is: {}".format(args.command))
        if (args.text == ''):
                return self.response

        newpass =  pbkdf2_sha256.hash(args.text)
        
        resp = self.bot.dbconn.query("""UPDATE users SET `password` = %s WHERE userID = %s""", (newpass, args.user["user"]["id"]))
        self.bot.log.warning(resp)

        self.response.setText("Set password")
        
        return self.response
