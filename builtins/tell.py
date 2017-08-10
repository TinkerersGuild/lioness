########
# comms
######
import sys
from plugins import PluginResponse, Plugin

class tell(Plugin):
    def __init__(self, **kwargs):
        self.keyword = ("tell","text")
        self.response = PluginResponse()
        self.error = ""
        self.bot = ""
        self.builtin = 1
        self.level = -1
        self.usage = "nfi"

    def command(self, args):
        self.response.setText(self.usage)
        text = args.text.split(" ")
        target = text[0]
        message = " ".join(text[1:])
        if (self.bot.send_im(target, message)):
            self.response.setText("Told {} about {}".format(target, message))
        else:
            self.response.setText("Could not tell {} about {}".format(target, message))
        
        return self.response
