#######
# What do we know?
from plugins.base import PluginResponse, Plugin
import sys

class known(Plugin):
	response = PluginResponse()
	keyword="known"
	tablemap = {}
	tables = list()
	dbconn = ''

	def __init__(self, dbconn):
		self.dbconn = dbconn
		querytext = "SHOW TABLES"
		#print("QUERY: {}".format(querytext))
		qres = self.dbconn.query(querytext, ())
		if qres is not None:

			self.tables.extend([str(x[0]).lower() for x in qres])
			#print("----- {}".format(self.tables))
		

	def command(self, args):
            
		text = args.text
		respstr = "Well, that went horribly wrong"

		tbl = ("name", "users")
		if (len(text) > 1):
			if text[1].lower() in self.tables:
				tbl = ("name", text[1].lower())
			else:
				tbl = list()
		
		if (len(tbl) == 0):
			self.response.setText("I don't know any {}".format(text[1]))
			return self.response

		querytext = "SELECT {} FROM {}"
		#print("QUERY: {}".format(querytext))
		qres = self.dbconn.query(querytext.format(tbl[0], tbl[1]), ())
		if qres is not None:
			respstr = "I know {} {}!\n".format(len(qres), tbl[1])
			for txt in	qres:
				respstr += str(txt[0]) + "\n"

		self.response.setText(respstr)
		return self.response
		
