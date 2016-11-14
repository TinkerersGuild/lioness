from database import DataBase
import yaml
import sys

from plugins.base import PluginManager

def load_configs():
	try:
		with  open("conf.yaml", "r") as conf_file:
			conf = yaml.load(conf_file)
	except :
		e = sys.exc_info()[0]

		print("Could not load: {}".format(e))
		conf = dict()
	return conf

config = load_configs()

print(config)
dbconn = DataBase(config['dbname'], config['username'], config['passwd'])
print(dbconn.show_tables())

p = PluginManager(dbconn)
	
TEXTRAS = {'lunch': ("list", "add blowme"),
			'known': ("fish", "users", "restaurants"),
			'jargon': ("foo","meme")}

COMMANDS = p.get_plugins()

for c,k in COMMANDS.items():
	print ("------TESTING {}".format(c))
	args = list()
	args.append(c)
	
	response = k.command(args)
	print(response.getText())
	
	if (len(TEXTRAS.get(c, ())) > 0):
		
		for i in TEXTRAS.get(c):
			args = list()
			args.append(c)
			args.extend( i.split())

			print("\n-\n")
			print(args)

			response = k.command( args )
			print(response.getText())
			
	
	print("\n----\n ")
