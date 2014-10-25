
class A(object):
	"""docstring for A"""
	def __init__(self, arg):
		super(A, self).__init__()
		self.arg = arg
	def call(self):
		print '11'

	def __unicode(self):
		return self.arg
		

a = [A(1),A(2),A(3)]
b = [x.arg for x in a]
print b