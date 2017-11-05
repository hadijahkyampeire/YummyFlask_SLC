
class User(object):
    """docstring for User_functionalities"""
    """ constructor"""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.categories = {}

    def add_category(self, title):
        """ add category method"""
        if not title in self.categories:
            self.categories[title] = Category(title)
            return True
        return False

    def edit_category(self, title, new_title):
        """ edit category method"""
        if title in self.categories:
            self.categories[new_title] = self.categories.pop(title)
            return True
        return False

    def delete_category(self, title):
        """ delete category method"""
        if title in self.categories:
            self.categories.pop(title)
            return True
        return False


class Category(object):
    """docstring for Category"""

    def __init__(self, title):
        self.title = title
        self.recipes = {}

    def add_recipe(self, title, contents, instructions):
        """ add recipe method"""
        if not title in self.recipes:
            self.recipes[title] = Recipe(title, contents, instructions)
            return True
        return False

    def edit_recipe(self, title, new_title):
        """ edit recipe method"""
        if title in self.recipes:
            self.recipes[new_title] = self.recipes.pop(title)
            return True
        return False

    def delete_recipe(self, title):
        """ delete recipe method"""
        if title in self.recipes:
            self.recipes.pop(title)
            return True
        return False


class Recipe(object):
    """docstring for Recipe"""

    def __init__(self, title, contents, instructions):

        self.title = title
        self.contents = contents
        self.instructions = instructions
