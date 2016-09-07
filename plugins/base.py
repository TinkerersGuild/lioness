from pathlib import Path
import imp



class PluginResponse(object):
	_text = ''
	def __init__(self):
		pass
	def setText(self, text):
		self._text = text
	def getText(self):
		return self._text

class Plugin(object):
	pass

class PluginManager():
	COMMANDS = dict()

	def __init__(self):
		self.initPlugins()

	def initPlugins(self):
		COMMANDS={}
		self.findPlugins()
		self.registerPlugins();

		

	def findPlugins(self):
		plugpath = Path("plugins")
		plugins = [list(plugpath.glob('*.py'))]
#		print(plugins)
		for pg in plugins[0]:
			pp = str(pg)
			pp = pp[:-3]
			#print("LOOKING FOR {}".format(pp))
			
			if (pp != "plugins/base"):
#				print("--Loading {}".format(pp))
				try:
					p = imp.find_module(pp)

					pl = imp.load_module(pp, p[0], p[1], p[2])
				except:
					pass		
		
	def registerPlugins(self):
		
		for plugin in Plugin.__subclasses__():
			
			obj= plugin()
			print("--Registering {}".format(obj.keyword))
			self.COMMANDS[obj.keyword] = obj

	def getPlugins(self):
		return self.COMMANDS