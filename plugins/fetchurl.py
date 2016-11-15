########
# Base URL fetcher
######
from plugins.base import PluginResponse, Plugin
import sys
import re
import requests
import html2text

class fetchurl(Plugin):
	def __init__(self, dbconn):
		self.keyword = "fetchurl"
		self.response = PluginResponse()
	
	def command(self, text):
		self.response.setText("Nope")
		
		if re.search("\|", text):
			text = text.split("|")[0]
			text = text + ">"
		url = text[1:-1]

		
		resp = requests.request('GET', url)
		if (resp.status_code == 200):
			txt = html2text.html2text(resp.text).split("\n")
			txt = txt[6:-6]
			if (len(txt) > 15):
				txt = txt[:15]
			
				txt[-1] += "\n(more ...)\n "
			
				
			txt.append("\n" + url)

			txt = "\n".join(txt)
			self.response.setText(txt)
				
		else:

			self.response.setText("I couldn't find that url!")
		return self.response
