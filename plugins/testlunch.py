import unittest
from database import DataBase
from plugins.lunch import lunch

class testlunch(unittest.TestCase):	
	def setUp(self):
		self.dbconn = DataBase("testlioness", "testlioness", "tester")
		self.l = lunch(self.dbconn)
		
	def test_get(self):
		
		choice = self.l.get_lunches()
		ch = self.l.choose_lunch(1)
		self.assertTrue(ch in choice)
	
	def test_bad_get(self):
		
		choice = self.l.get_lunches()
		ch = self.l.choose_lunch()
		self.assertFalse(ch in choice)

	def test_command(self):
		choice = self.l.get_lunches()
		ch = self.l.command(' ')
		self.assertTrue(ch in choice)

	def test_add(self):
		name = "Testaurant"
		resp = self.l.add_lunch(name)
		self.assertFalse(resp.split()[0] == 'DBI')
		check = self.dbconn.query("SELECT * from `restaurants` WHERE `name`=%s", (name,))
		self.assertFalse(len(check) == 0)