import unittest
from models import Category

class TestCategory(unittest.TestCase):
    def test_create_category(self):
        category = Category("Main Course")
        self.assertEqual(category.name, "Main Course")

    def test_update_category(self):
        category = Category("Dessert")
        category.update_name("Sweet Treats")
        self.assertEqual(category.name, "Sweet Treats")

if __name__ == '__main__':
    unittest.main()