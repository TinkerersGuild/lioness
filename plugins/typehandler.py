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
        self.keyword = ("handle",)
        self.response = PluginResponse()
        self.error = ""
        self.dbconn = dbconn
        self.opt = "files"


    def command(self, args):
        self.response.setText("Nope")
        text = args.text.split()
        userID = args.user["user"]["id"]
        tag = text[0]
        url = text[1]
        fileID = text[-1]
        stored = url
        if (tag == 'file_share'):
            print("File: {0} {1} opts {2} ".format(url, fileID, args.opt))
            if (args.opt == 0):
                print("\n\nOpted out - not storing\n\n")
            else:
                print("\n\nOpted no worries\n\n")
            try:
                resp = requests.get(url, headers={"Authorization":"Bearer {}".format(os.environ["BOT_TOKEN"])}, stream=True)
                resp.raise_for_status()

                if resp.ok:
                    filedir = "files/" + userID + "/"
                    print("File: {0} ".format(filedir, fileID))
                    if not os.path.exists(filedir):
                        os.makedirs(filedir)
                    with open(filedir + fileID , 'wb') as f:
                        for block in resp.iter_content(1024):
                            f.write(block)
                        f.close()
                else:
                    print("Not ok")
                print("saved")

            except Exception as e:
                print("No response! {}".format(e) )
                




        try:
            # replace with function
            self.error = self.dbconn.query("""INSERT INTO `store`(`text`, `tag`, `userID`) VALUES(%s, %s, %s)""", (stored, tag, userID))
            self.response.setText("Added for {}!".format(args.user["user"]["name"]))
        except:
            self.response.setText("Cannot la: {}".format(self.error))


        return self.response
