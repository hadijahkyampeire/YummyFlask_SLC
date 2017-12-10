class Recipe(object):
    """docstring for Recipe"""

    def __init__(self, title, contents, instructions):
        self.title = title
        self.contents = contents
        self.instructions = instructions
        self.recipes={}
    def add_recipe(self, title, contents, instructions):
        """ add recipe method"""
        self.recipes[title] = Recipe(title, contents, instructions)
        return True


    def edit_recipe(self, title, new_title):
        """ edit recipe method"""
        
        self.recipes[new_title] = self.recipes.pop(title)
        return True
        

    def delete_recipe(self, title):
        """ delete recipe method"""
        if title in self.recipes:
            self.recipes.pop(title)
            return True
        return False    
    
    