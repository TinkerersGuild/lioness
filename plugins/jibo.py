from plugins import PluginResponse, Plugin
import sys


class jibo(Plugin):
        def __init__(self, dbconn):
                self.keyword = ("jibo",)
                
        def command(self, args):
                response = PluginResponse()
                response.setText("Why don't you go fuck yourself")
                return response
