#!/usr/bin/python3

import time
import sys
from slackclient import SlackClient
import re
from database import DataBase
from channel import ChannelManager
from users import UserManager
from commander import Commander, CommandArgs
import yaml
import logger

PREFIX = "/home/solitaire/lioness/"

def load_configs(cfile):
	"""Load the config from the given absolute path file name"""
	try:
		with  open(cfile, "r") as conf_file:
			conf = yaml.load(conf_file)
	except :
		e = sys.exc_info()[0]

		print("Could not load: {}".format(e))
		conf = dict()
	return conf



class Lioness():
	""" Lioness is the main class for loading the configs and handling connections

		__init__(self, config, log) takes a dictionary of configs and a logger object

		"""
	def __init__(self, config, log):
		"""Takes config dict and logger object to initialise """
		self.log = log
		self.status = "ok"
		try:
			token = config['APIKEY'].strip()
			self.sc = SlackClient(token)
		except:
			self.status = "BAD TOKEN"

		self.dbconn = DataBase(config['dbname'], config['username'], config['passwd'])
		self.log.log(0, "DBConn {}".format(self.dbconn))

		tables = self.dbconn.show_tables()
		self.log.log(0, tables)

		self.chanman = ChannelManager()
		self.channels = self.chanman.get_channels()

		self.people = UserManager()
		self.people.set_ops(config['owners'])
		
		self.commander = Commander(self.dbconn, self.log, config['prefix'])
		self.botname = config['botname']
		self.icon = config['icon']
		
		self.log.log(1,"Channels to join:")
		self.log.log(1,self.channels['join'])

		

	def connect_to_server(self):
		
		if (self.sc.rtm_connect()):
			self.ping_owners("Here I am!")
			return 1
		return 0

	def disconnect(self):
		#sc.rtm_disconnect()
		return 1

	def chanpost(self,mychannel, message):
		self.log.log(2, "Chanpost: {} {}".format(mychannel, message))
		resp = self.sc.api_call(
	    	"chat.postMessage", channel=mychannel, text=message,
	    	 username=self.botname, icon_url=self.icon)
		self.log.log(2, resp)
		return resp


	def ping_owners(self,message):
		for op in self.people.get_owners():
			resp = self.sc.api_call("im.open", user = own['id'])
			own['chat'] = resp['channel']['id']
			self.log.log(1, "Pinging owner {}".format(own))
			self.log.log(1,sc.api_call("chat.postMessage", as_user="true:", channel=own['chat'], text=message))


	def add_chans(self,chans):
		for chan in chans['channels']:
			self.chanman.set_lookup(chan['id'], chan['name'])		
		
			self.log.log(3,"{} : {}".format(chan['name'], chan['id']))
			self.channels['known'].append(chan['name'])

			if (chan['name'] in self.channels['join']):

				self.log.log(2, "Found watching channel {}".format(chan['name']))
				self.channels['watching'].append(chan['id'])

		for chan in self.channels['watching']:
			self.log.log(3,"Watching {}".format(chan))			


	def get_timestamp(self,msg):
		if (msg.get('ts')):
			if (float(msg['ts']) > float(self.ts)):
				self.log.log(0, "Setting timestamp {} ".format(msg['ts']))
			return msg['ts']
		else:
			return self.ts

	



	def setup(self):
		chans = self.sc.api_call("channels.list")
		self.add_chans(chans)
		resp = self.chanpost("#bot_testing", "boop")
		
		for k,v in resp.items():
			self.log.log(3,"Key: {} Value: {} \n".format(k, v))
		
		self.ts = resp.get('ts')
		self.log.log(0,"Timestamp: {}".format(self.ts))

		self.log.log(1, "Checking API")
		self.log.log(1, self.sc.api_call("api.test"))
		#DEBUG_LEVEL = 0

	def listen(self):
		_connect = 1
		while(_connect):
			# HUP received, reload the plugins, disconnect from the server and reconnect
			if (_connect == 2):
				self.log.log(0, "++++++++++++ REBOOT OUT OF CHEESE +++++")
				self.disconnect()
				if (self.connect_to_server()):
					#self.plugins = self.reload_plugins()

					_connect = 1
				else:
					_connect = 0
			

			time.sleep(0.5)

			for chan in self.channels['watching']:
				cname = "#"+ self.chanman.get_name(chan)
				resp = self.sc.api_call("channels.history",
					channel=chan, oldest = self.ts 
					)
				
				for msg in resp['messages']:
					self.ts = self.get_timestamp(msg)
					user = msg.get('user')
					txt = msg.get('text', '')
					if (re.match("^<https?://", txt)):
						txt = '!store ' + txt 

					if (re.match('!', txt)):
						self.log.log(2, "COMMAND MESSAGE {}".format(txt))
						txt = txt.split()

						commandargs = CommandArgs()
						
						commandargs.chan = cname
						commandargs.user = user
						commandargs.command = txt[0][1:]
						commandargs.text = ' '
					
						if (len(txt) > 1):
							commandargs.text = ' '.join(txt[1:])
					


						reply = self.commander.handle(commandargs)

						self.chanpost("#bot_testing", reply.getText())


				

			



if __name__ == '__main__':
	
	try:
		conf = load_configs(PREFIX +"conf.yaml")
	except:
		e = sys.exc_info()[0]
		print("Can't load config - have you broken it? {}".format(e))
	
	log = logger.Logger(conf['debug_lvl'], conf['prefix'] + conf['logfile'])
	

	log.log(2,"CONFIGS: {}".format(conf))	
	
	lioness = Lioness(conf, log)	
	if (lioness.connect_to_server()):	
		lioness.setup()	
		lioness.listen()




	
