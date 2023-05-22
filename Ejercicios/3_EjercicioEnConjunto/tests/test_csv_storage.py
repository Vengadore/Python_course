import unittest
import os
from models import Recipe
from utils.csv_handler import CSVStorage

class TestCSVStorage(unittest.TestCase):
    def setUp(self):
        self.filename = 'recipes.csv'
        self.storage = CSVStorage(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_recipes(self):
        recipes = [
            Recipe("Cake", ["Flour", "Sugar", "Eggs"], "Mix ingredients and bake."),
            Recipe("Salad", ["Lettuce", "Tomato", "Cucumber"], "Chop ingredients and mix.")
        ]
        self.storage.save_recipes(recipes)
        self.assertTrue(os.path.exists(self.filename))

    def test_load_recipes(self):
        recipes = [
            Recipe("Cake", ["Flour", "Sugar", "Eggs"], "Mix ingredients and bake."),
            Recipe("Salad", ["Lettuce", "Tomato", "Cucumber"], "Chop ingredients and mix.")
        ]
        self.storage.save_recipes(recipes)
        loaded_recipes = self.storage.load_recipes()
        self.assertEqual(len(loaded_recipes), len(recipes))
        for i in range(len(recipes)):
            self.assertEqual(loaded_recipes[i].name, recipes[i].name)
            self.assertEqual(loaded_recipes[i].ingredients, recipes[i].ingredients)
            self.assertEqual(loaded_recipes[i].instructions, recipes[i].instructions)

if __name__ == '__main__':
    unittest.main()