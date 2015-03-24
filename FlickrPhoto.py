
class Photo(object):
	
	def __init__(self, title, id):
		self.title = title
		self.id = id
		
	def __str__(self):
		return self.title