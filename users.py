##############3
# It's all about the people....
# Wed 07 Sep 2016 17:24:37 AEST

class UserManager():
	OPS = list()
	OWNERS = list()

	def add_owner(self, op):
		self.OWNERS.append(op)
		self.set_op(op)

	def get_owners(self):
		return self.OWNERS
	
	def set_ops(self, ops):
		for k,v in ops.items():
			self.set_op(v['id'])

	def set_op(self, op):
		self.OPS.append(op)

	def is_op(self, id):
		return (id in self.OPS)
	

	#def removeop(self, id):


		