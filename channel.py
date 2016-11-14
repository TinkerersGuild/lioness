#############
# Channel module for tracking which channels to listen in, and 
# channel ops etc.


class ChannelManager():
	lookup = dict()
	revlookup = dict()
	channels = { "join": ("bot_testing",),
			"known": list(),
			"watching": list()
	}
	def __init__(self):
		pass

	def get_channels(self):
		return self.channels;
	
	def set_lookup(self, cid, name):
		self.lookup[cid] = name
		self.revlookup[name] = cid

	def get_name(self, cid):
		return self.lookup.get(cid)
