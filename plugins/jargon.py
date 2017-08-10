########
# Fetches jargon file entries
######
from plugins import PluginResponse, Plugin
import sys
import requests
import html2text

MAXLINES = 12

class jargon(Plugin):
        def __init__(self, dbconn):
                self.keyword = ("jargon",)
                self.response = PluginResponse()

        def command(self, args):
                text = args.text
                self.response.setText("Nope")
                if (text !=' '):
                        searchstr = "-".join(text.split())
                

                        cap = searchstr[0].upper()
                        url = "http://www.catb.org/jargon/html/{}/{}.html".format(cap, searchstr)
                        #print(url)
                        resp = requests.get(url)
                        if (resp.status_code == 200):
                        #print(resp)
                                txt = html2text.html2text(resp.text).split("\n")
                                ftxt = ''

                                txt = txt[6:-6]
                                if (len(txt) > MAXLINES):
                                        txt = txt[:MAXLINES]
                        
                                        txt[-1] += "\n(more ...)\n "
                        
                                for i in (txt):
                                        print(".{}.".format(i))
                                        if (i.strip() != ''):
                                                ftxt += i.strip() + "\n"
                                

                                ftxt += ("\n" + url)
                                self.response.setText(ftxt)
                                
                        else:

                                self.response.setText("I couldn't find that url!")
                return self.response
