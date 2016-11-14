from plugins.base import PluginResponse, Plugin
import sys

from random import randint


class lunch(Plugin):	

	prefixes = (
		"Let's go to ",
		"Why not try ",
		"I feel like "
		)



	def __init__(self, dbconn):
		self.keyword = "lunch"
		self.dbconn = dbconn

	def command(self, text):
		response = PluginResponse()
		response.setText("The usual place")
		

		try:
		
			if (text != ' '):
				
				resp = self.parse_command(text)
				response.setText(resp)
				
			else:
				response.setText(self.choose_lunch())   
		except: 

			e = sys.exc_info()[0]
			response.setText( "NFI {}".format(e))
		return response

	def choose_lunch(self, naked = 0):
		prefix =  self.prefixes[randint(0, len(self.prefixes) -1)]  
		lunches = self.get_lunches()
		lunch = lunches[randint(0,len(lunches) -1)]
		if (naked):
			return lunch

		return prefix + lunch

	def parse_command(self,text):
		resp = ''
			
		if (text[1] == 'list'):
		#	print("listing")
			resp = self.list_lunches()

		elif (text[1] == 'add'):
			rname = " ".join(text[2:])
					
			resp = self.add_lunch()

			
		return resp

	def list_lunches(self):
		#print("still listing")
		
		return "\n".join(self.get_lunches())

	def get_lunches(self):
		#print("getting")
		lunches = list()
		for s in self.dbconn.query("SELECT name FROM restaurants", ()):
			#print(s[0])
			lunches.append(s[0])
		return lunches

	def add_lunch(self, name):
		try:
			self.dbconn.query("""INSERT INTO `restaurants`(`name`) VALUES (%s)""", (name,))
			return "Added {}".format(name)
		except:
			e = sys.exc_info()[0]
			return "DBI {}".format(e)

