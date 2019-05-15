########
# Base URL storer
######
import os
import sys
from plugins import PluginResponse, Plugin
import requests
import html2text

class store(Plugin):
    def __init__(self, dbconn):
        self.keyword = ("handle","files", "links")
        self.response = PluginResponse()
        self.error = ""
        self.dbconn = dbconn
        self.opt = "files"
        print("Done loading")


    def command(self, args):
        self.response.setText("Nope")
        text = args.text.split()
        userID = args.user["user"]["id"]
        if args.command == "handle":
            if (args.opt == 0):
                self.response.setText("\n\nOpted out - not storing\n\n")
                return self.response; 
            tag = text[0]
            url = text[1]
            fileID = text[-1]
            stored = url
            

            if (tag == 'file_share'):
                try:
                    resp = requests.get(url, headers={"Authorization":"Bearer {}".format(os.environ["BOT_TOKEN"])}, stream=True)
                    resp.raise_for_status()

                    if resp.ok:
                        filedir = "files/" + userID + "/"
                        if not os.path.exists(filedir):
                            os.makedirs(filedir)
                        with open(filedir + fileID , 'wb') as f:
                            for block in resp.iter_content(1024):
                                f.write(block)
                            f.close()

                except Exception as e:
                    self.response.setText("No response! {}".format(e) )
                

            try:
                # replace with function
                self.error = self.dbconn.query("""INSERT INTO `store`(`text`, `tag`, `userID`) VALUES(%s, %s, %s)""", (stored, tag, userID))
                self.response.setText("Added for {}!".format(args.user["user"]["name"]))
            except:
                self.response.setText("Cannot la: {}".format(self.error))

        elif args.command == "files":
                self.error = self.dbconn.query("""SELECT text from `store` WHERE userID = %s AND `tag`=%s""" , (userID,"file_share"))
                resp = ""
                for myfile in self.error:
                    resp += myfile[0] + "\n"
                self.response.setText(resp)
        elif args.command == "links":
                self.error = self.dbconn.query("""SELECT text from `store` WHERE userID = %s AND`tag`=%s""" , (userID,"generic"))
                resp = ""
                for myfile in self.error:
                    resp += " {} \n".format(myfile[0]) 
                self.response.setText(resp)


        return self.response
