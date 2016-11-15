from pathlib import Path

import imp
import sys


class PluginResponse(object):
	_text = ''
	_chan = ''
	def setChan(self, chan):
		self._chan = chan	
	def setText(self, text):
		self._text = text
	def getText(self):
		return str(self._text)
	def getChan(self):
		return str(self._chan)

class Plugin(object):
	pass

class PluginManager():
	COMMANDS = dict()
	dbconn = ''

	def __init__(self, dbconn, log, prefix):
		self.dbconn = dbconn
		self.log = log
		self.prefix = prefix + "plugins"
		self.init_plugins()
		#print(dbconn)
		

	def init_plugins(self):
		COMMANDS={}
		self.find_plugins()
		self.register_plugins();

		

	def find_plugins(self):
		
		plugpath = Path(self.prefix)
		plugins = [list(plugpath.glob('*.py'))]
#		print(plugins)
		for pg in plugins[0]:
			pp = str(pg)
			pp = pp[:-3]
			self.log.log(0,"LOOKING FOR {}".format(pp))
			
			if (pp != self.prefix+"base"):
#				print("--Loading {}".format(pp))
				try:
					p = imp.find_module(pp)
						
					pl = imp.load_module(pp, p[0], p[1], p[2])
				except:
					e = sys.exc_info()[0]

					#print("----  Could not load: {}".format(e))		
		
	def register_plugins(self):
		
		for plugin in Plugin.__subclasses__():
			#print(plugin)
				
			obj= plugin(self.dbconn)
			#print("--Registering {}".format(obj.keyword))
		
			self.COMMANDS[obj.keyword] = obj
		
	def get_plugins(self):
		return self.COMMANDS
