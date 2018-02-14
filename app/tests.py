import unittest
from .models.user import User
from .models.category import Category
from .models.recipe import Recipe

class UserTest(unittest.TestCase):
    """ usertest class setup"""

    def setUp(self):
        self.user = User("hadijah", "kyampeire",
                         "hadijah315@gmail.com", "omega")

    def test_created_user(self):
        """ usertest if user is added"""
        self.assertIsInstance(self.user, User, False)


class CategoryTest(unittest.TestCase):
    """ category test setup"""

    def setUp(self):
        self.title = Category("lunch")
    
    def test_addcategory_added(self):
        """ usertest if category is added"""
        self.assertEqual(self.title.add_category("dinner"),
                         True)

    def test_addcategoryname_exists(self):
        """ usertest if category already exists"""
        self.title.add_category("dinner")
        self.assertEqual(self.title.add_category("dinner"),
                         False)

    def test_editcategory_not_found(self):
        """ usertest if user is added"""
        self.assertEqual(self.title.edit_category("drinks", "others"),
                         False)

    def test_editcategory_successful(self):
        """ usertest if category is added"""
        self.title.add_category("Snacks")
        self.assertEqual(self.title.edit_category("dissert", "veggies"), False)

    def test_deletecategory_not_found(self):
        """ usertest if category to delete is not found"""
        self.assertEqual(self.title.delete_category("deleted"), False)

    def test_deletecategory_deleted(self):
        """ usertest if category is deleted"""
        self.title.add_category("breakfast recipes")
        self.assertEqual(self.title.delete_category("breakfast recipes"),
                         True)
class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.title = Recipe('dissert','contents','instructions')
    def test_addrecipe_added(self):
        """ recipe testadded"""
        self.assertEqual(self.title.add_recipe(
            "soup", "salt and tomatoes", "tomatoes first"), True)

    def test_addrecipe_exists(self):
        """ if recipe already exists"""
        self.title.add_recipe(
            "pizza", "chapati and meat", "chapati comes first")
        self.assertEqual(self.title.add_recipe(
            "pizza", "chapati and meat", "chapati comes first"), True)

    def test_edit_recipe_not_found(self):
        """ recipe edits test"""
        self.title.add_recipe(
            "pizza", "chapati and meat", "chapati comes first")
        self.assertEqual(self.title.edit_recipe(
            "pizza", "beef recipe"), True)

    def test_editrecipe_succesfully(self):
        """ edit successful testing"""
        self.title.add_recipe(
            "pizza", "chapati and meat", "chapati comes first")
        self.assertEqual(self.title.edit_recipe("pizza", "chicken"), True)

    def test_deleterecipe_notfound(self):
        """ delete recipe test"""
        self.assertEqual(self.title.delete_recipe(
            "katogo"), False)
