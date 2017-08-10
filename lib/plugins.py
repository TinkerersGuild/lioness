from pathlib import Path

import imp
import sys


class PluginResponse(object):
        _text = ''
        _chan = ''
        _user = ''
        def setUser(self, user):
                self._user = user
        def getUser(self):
                return str(self._user)
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
                

class Builtin(object):
        pass

class PluginManager():
        COMMANDS = dict()
        dbconn = ''

        def __init__(self, bot, prefix):
                self.bot = bot
                self.dbconn = bot.dbconn
                self.log = bot.log
                self.paths = (prefix + "/plugins", prefix + "/builtins")
                self.init_plugins()
                #print(dbconn)
                

        def init_plugins(self):
                COMMANDS={}
                for path in self.paths:
                    self.find_plugins(path)
                self.register_plugins();

                

        def find_plugins(self, path):
                
                plugpath = Path(path)
                plugins = [list(plugpath.glob('*.py'))]
#               print(plugins)
                for pg in plugins[0]:
                        pp = str(pg)
                        pp = pp[:-3]
                        self.log.critical("LOOKING FOR {}".format(pp))
                        
                        self.log.warning("--Loading {}".format(pp))
                        try:
                                p = imp.find_module(pp)
                                                
                                pl = imp.load_module(pp, p[0], p[1], p[2])
                        except:
                                e = sys.exc_info()[0]

                                self.log.critical("----  Could not load: {}".format(e))            
                
        def register_plugins(self):
                
                for plugin in Plugin.__subclasses__():
                        #print(plugin)
                                
                        obj= plugin(dbconn = self.dbconn)
                        try:
                            if obj.builtin:
                                obj.bot = self.bot
                        except:
                            obj.level = -1
                            obj.builtin = 0
                            obj.bot = ""
                        #print("--Registering {}".format(obj.keyword))
                        for kw in obj.keyword: 
                            if kw not in self.COMMANDS:
                                self.COMMANDS[kw] = obj
                
        def get_plugins(self):
                return self.COMMANDS
