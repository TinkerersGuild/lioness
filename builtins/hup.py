########
# comms
######
import sys
from plugins import PluginResponse, Plugin

class hup(Plugin):
    def __init__(self, **kwargs):
        self.keyword = ("hup",)
        self.response = PluginResponse()
        self.error = ""
        self.bot = ""
        self.builtin = 1
        self.level = 98
        self.usage = "nfi"

    def command(self, args):
        self.response.setText("Resetting plugins")
        self.bot.commander.reload_plugins()
        
        
        return self.response
