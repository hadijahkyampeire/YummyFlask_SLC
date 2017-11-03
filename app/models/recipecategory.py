class Recipe_category(object):
	"""docstring for Recipe_category"""
	def __init__(self, arg):
		self.arg=arg

	def create_category(self, category_name, recipe1,recipe2,recipe3,recipe4):
		self.Recipe_Category = category_name
		self.Item1=recipe1
		self.Item2=recipe2
		self.Item3=recipe3
		self.Item4=recipe4
		
	def remove_category(self, category_name):
		self.Recipe_Category=category_name
		