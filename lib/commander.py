####################
# Command handler for Lioness bot. This is where the heavy lifting happens.
###
from plugins import PluginManager, PluginResponse
import re
import sys

class CommandArgs():
    def __init__(self):
        self.user = ''
        self.command = ''
        self.text = ''
        self.chan = ''
        

class Commander():

    def __init__(self, bot, prefix, enable_plugins):
        self.dbconn = bot.dbconn;
        self.log = bot.log
        self.bot = bot
        self.enable_plugins = enable_plugins
        plugin = PluginManager(bot, prefix)
        self.commands = plugin.get_plugins()
        self.log.warning("COMMANDS: {}".format(self.commands))

    def handle(self, args):
        self.log.critical( "CHANNEL: " + args.chan)
        response = PluginResponse()
        #self.log.warning("Message from :{}:{}:{}".format(args.user, args.command, args.text))
    
        self.log.warning( "Looking for {}".format(args.command))
        
        if (self.commands.get(args.command)):
            cmd = self.commands[args.command]
            
            if (cmd.builtin or self.enable_plugins):
                if (self.auth_user(args.user["user"]["id"], cmd.level)):


                    self.bot.log.critical("Authed  {0} for {1}".format(args.user["user"]["name"], args.command))
                    try:
                        self.log.critical( " ({})trying {} with {} ".format(args.chan, args.command, args.text))
                        response = cmd.command(args) 
                        response.setUser(args.user["user"]["id"])
                        self.log.warning( response.getText())
                    except:
                        e = " {} : {}".format( sys.exc_info()[0],  sys.exc_info()[1])
                        
                        self.log.critical( "Could not perform plugin! {}".format(e))
                        response.setText("Error with plugin. Blame {}".format("jai"))
                else:
                    response.setText("Forbidden to you!")
            else:
                response.setText("Unable to comply")
        else:
            response.setText("I have no idea what you are asking me to do.")

        response.setChan(args.chan)
        return response

    def auth_user(self, userID, level):
        if (self.bot.people.get_user_level(userID) > level):
            return 1
        return 0

    def parse_opts(self, text):
        self.log.warning( "Trying to parse")
        opts = dict()
        content = ''
        key = ''

        if (len(text) == 0):
            return (opts, content)

        for token in text.split():
            if re.match("-", token):
                key = token
                while (key[0] == "-"):
                    key = key[1:]

            else:
                if (key != ''):
                    opts[key] = token
                    key = ''
                else:
                    content += str(token) + " "

        return(opts, content)
