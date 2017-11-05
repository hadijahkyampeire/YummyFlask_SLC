import unittest
from models import User,Category,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("hadijah", "kyampeire", "hadijah315@gmail.com", "omega")


    def test_created_user(self):
        self.assertIsInstance(self.user, User, False)

    def test_add_category_category_added(self):
        self.assertEqual(self.user.add_category("dinner"),
                        True)

    def test_add_category_name_already_exists(self):
        self.user.add_category("dinner")
        self.assertEqual(self.user.add_category("dinner"),
                         False)


    def test_edit_category_not_found(self):
        self.assertEqual(self.user.edit_category("drinks", "others"),
                         False)

    def test_edit_category_successful(self):
        self.user.add_category("Snacks")
        self.assertEqual(self.user.edit_category("dissert","veggies"),False)
        
    def test_delete_category_not_found(self):
        self.assertEqual(self.user.delete_category("deleted"), False)

    def test_delete_category_deleted(self):
        self.user.add_category("breakfast recipes")
        self.assertEqual(self.user.delete_category("breakfast recipes"),
                         True)
        
class Recipe_categoryTest(unittest.TestCase):
    
    def setUp(self):
        self.recipes = Category("lunch")

    def test_add_recipe_added(self):
            self.assertEqual(self.recipes.add_recipe("soup","salt and tomatoes", "tomatoes first"), True)

    def test_add_recipe_exists(self):
        self.recipes.add_recipe("pizza" ,"chapati and meat","chapati comes first")
        self.assertEqual(self.recipes.add_recipe(
            "pizza", "chapati and meat","chapati comes first"), False)

    def test_edit_recipe_not_found(self):
        self.assertEqual(self.recipes.edit_recipe(
            "chicken recipe", "beef recipe"), False)

   
    def test_edit_recipe_edited_succesfully(self):
         self.recipes.add_recipe("pizza","chapati and meat","chapati comes first")
         self.assertEqual(self.recipes.edit_recipe("chicken", "pizza"), False)

    def test_delete_recipe_not_found(self):
          self.assertEqual(self.recipes.delete_recipe(
            "katogo"), False)

    
