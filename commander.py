####################
# Command handler for Lioness bot. This is where the heavy lifting happens.
###
from plugins.base import PluginManager, PluginResponse
import re
import sys

class CommandArgs():
	def __init__(self):
		self.user = ''
		self.command = ''
		self.text = ''
		self.chan = ''


class Commander():

	def __init__(self, dbconn, log, prefix):
		self.dbconn = dbconn;
		self.log = log
		
		plugin = PluginManager(dbconn, log, prefix)

		self.commands = plugin.get_plugins()
		self.log.log(2, "COMMANDS: {}".format(self.commands))

	def handle(self, args):
		self.log.log(0, "CHANNEL: " + args.chan)
		response = PluginResponse()
		self.log.log(2,"Message from :{}:{}:{}".format(args.user, args.command, args.text))
	
		#if (args.text is not None):
		#	opts, content = self.parse_opts(args.text)


		#XXX All commands should appear here, and load the builtins first. 
		#Commands should have keywords and "level". 
		#Users should also have "rank"
		self.log.log(2, "Looking for {}".format(args.command))
		
		if (self.commands.get(args.command)):
			cmd = self.commands[args.command]

			if (1 > 0):
				try:
					self.log.log(0, " ({})trying {} with {} ".format(args.chan, args.command, args.text))
					response = cmd.command(args) 
					self.log.log(0, response.getText())
				except:
					e = sys.exc_info()[0]
					self.log.log(0, "Could not perform plugin! {}".format(e))
					response.setText("Error with plugin. Blame {}".format("jai"))
#
#		elif (args.user ):
#			if (args.command == 'die'):
#				self.log.log(0, "{} says die!".format(args.user))
#				_connect = 0
#			elif (args.command == 'hup'):
#				_connect = 2
#			elif (args.command == 'debug' ):
#				try:
#					lev = int(args.text[0])
#					self.log.DEBUG_LEVEL = lev
#					response.setText ("Setting log level to {}".format(lev))
#				except:
#					response.setText("Cannot set level {}".format(lev))
#			else:
#				response.setText("#bot_testing","What you talkin about, Willis?")
		else:
			response.setText("I have no idea what you are asking me to do.")

		response.setChan(args.chan)
		return response

	def parse_opts(self, text):
		self.log.log(2, "Trying to parse")
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
