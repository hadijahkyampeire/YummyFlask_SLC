from app.models.user import User

class Yummyapp(object):
	"""docstring for Yummyapp"""
	def __init__(self):
		self.the_users = {}

	def create_user(self, first_name,last_name,email,password):
		
		if email not in self.the_users:
			new_user = User(first_name,last_name,email,password)
			the_users[email] = new_user
			return new_user

	def login(self,email,password):
		self.Email=email
		self.Password=password
	
	def logout():
		pass

# y = Yummyapp()
# c= y.create_user('a','b','a@a', 'dd')
# print(c.email)
