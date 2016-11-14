#########
# Jargon test
######

import unittest
from plugins.jargon import jargon

class testjargon(unittest.TestCase):	
	def setUp(self):
		self.j = jargon('')

	def test_get(self):
		self.j.command('foo')



		
