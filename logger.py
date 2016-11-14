##########
# Various lioness utilities
#####

class Logger():
	def __init__(self, level, file):
		self.DEBUGLEVEL = level
		self.file = file

	def log(self,level, message):
		if (level < self.DEBUGLEVEL):
			with open(self.file, "a") as f:
				f.write(str(message)+"\n")