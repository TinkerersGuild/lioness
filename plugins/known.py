########
# Base URL storer
######
from plugins import PluginResponse, Plugin
import sys

class store(Plugin):
    def __init__(self, dbconn):
        self.keyword = ("known",)
        self.response = PluginResponse()
        self.error = ""
        self.dbconn = dbconn


    def command(self, args):
        self.response.setText("Nope")
        
        text = args.text.split(" ")
        #userID = args.user["user"]["id"]

        #if (text[0] == "update"):
            
        
        try:

            users = self.dbconn.query("SELECT `title`, `name` FROM `users`", [])
            resp = "TISM know the following people obey the TED commandments: \n"
            #print(users)
            for user in users:
                if (user[0]):
                    resp += "{} ".format(user[0])    
                resp += "{} \n".format(user[1])
            self.response.setText(resp)
        except:
            self.response.setText("Cannot la: {}".format(self.error))


        return self.response
