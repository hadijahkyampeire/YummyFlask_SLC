import unittest
from models import User, Category, Recipe


class UserTest(unittest.TestCase):
    """ usertest class setup"""

    def setUp(self):
        self.user = User("hadijah", "kyampeire",
                         "hadijah315@gmail.com", "omega")

    def test_created_user(self):
        """ usertest if user is added"""
        self.assertIsInstance(self.user, User, False)

    def test_addcategory_added(self):
        """ usertest if category is added"""
        self.assertEqual(self.user.add_category("dinner"),
                         True)

    def test_addcategoryname_exists(self):
        """ usertest if category already exists"""
        self.user.add_category("dinner")
        self.assertEqual(self.user.add_category("dinner"),
                         False)

    def test_editcategory_not_found(self):
        """ usertest if user is added"""
        self.assertEqual(self.user.edit_category("drinks", "others"),
                         False)

    def test_editcategory_successful(self):
        """ usertest if category is added"""
        self.user.add_category("Snacks")
        self.assertEqual(self.user.edit_category("dissert", "veggies"), False)

    def test_deletecategory_not_found(self):
        """ usertest if category to delete is not found"""
        self.assertEqual(self.user.delete_category("deleted"), False)

    def test_deletecategory_deleted(self):
        """ usertest if category is deleted"""
        self.user.add_category("breakfast recipes")
        self.assertEqual(self.user.delete_category("breakfast recipes"),
                         True)


class CategoryTest(unittest.TestCase):
    """ category test setup"""

    def setUp(self):
        self.recipes = Category("lunch")

    def test_addrecipe_added(self):
        """ recipe testadded"""
        self.assertEqual(self.recipes.add_recipe(
            "soup", "salt and tomatoes", "tomatoes first"), True)

    def test_addrecipe_exists(self):
        """ if recipe already exists"""
        self.recipes.add_recipe(
            "pizza", "chapati and meat", "chapati comes first")
        self.assertEqual(self.recipes.add_recipe(
            "pizza", "chapati and meat", "chapati comes first"), False)

    def test_edit_recipe_not_found(self):
        """ recipe edits test"""
        self.assertEqual(self.recipes.edit_recipe(
            "chicken recipe", "beef recipe"), False)

    def test_editrecipe_succesfully(self):
        """ edit successful testing"""
        self.recipes.add_recipe(
            "pizza", "chapati and meat", "chapati comes first")
        self.assertEqual(self.recipes.edit_recipe("chicken", "pizza"), False)

    def test_deleterecipe_notfound(self):
        """ delete recipe test"""
        self.assertEqual(self.recipes.delete_recipe(
            "katogo"), False)
