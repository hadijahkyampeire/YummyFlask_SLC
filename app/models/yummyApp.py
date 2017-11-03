class Yummyapp(object):
	"""docstring for Yummyapp"""
	def __init__(self):
		self.User = {}
	def create_user(self, first_name,last_name,email,password):
		self.FirstName=first_name
		self.LastName=last_name
		self.Email=email
		self.Password=password

	def login(self,email,password):
		self.Email=email
		self.Password=password
	
	def logout():
		pass