#! /usr/bin/python3
############
# Universal Test Harness
########
import unittest
#import MySQLdb
from database import DataBase
from users import UserManager
from channel import ChannelManager
from pathlib import Path

import imp
import sys
plugpath = Path("plugins")
plugins = [list(plugpath.glob('test*.py'))]
#		print(plugins)
for pg in plugins[0]:
	pp = str(pg)
	pp = pp[:-3]
	print("LOADING FOR {}".format(pp))
	
	try:
		p = imp.find_module(pp)
		pl = imp.load_module(pp, p[0], p[1], p[2])

	except:
		e = sys.exc_info()[0]

		print("----  Could not load {} : {}".format( p[0], e))		

for plugin in unittest.TestCase.__subclasses__():
	pass			
	
class TestDataBase(unittest.TestCase):
	def test_connection(self):
		query = """SELECT name,title FROM users"""
		user = dbconn.query(query, ())[0]
		self.assertEqual(user[0], 'jai')
		self.assertEqual(user[1], 'botmaster')



class TestUsers(unittest.TestCase):
	def test_user(self):
		um = UserManager()
		owners = um.get_owners()

		#self.assertEqual(owners[0], 'U189HEXD5')


class TestChannels(unittest.TestCase):
	def test_channels(self):
		cm = ChannelManager()
		chan = cm.get_channels()
		self.assertEqual(chan['join'][0], "bot_testing")



if __name__ == '__main__':
	dbconn = DataBase("testlioness", "testlioness", "tester")
	
	
	unittest.main()
	
