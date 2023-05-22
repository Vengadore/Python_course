import unittest
from models import Recipe, Ingredient

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.ingredients = [
            Ingredient("Flour", "2 cups"),
            Ingredient("Sugar", "1 cup"),
            Ingredient("Eggs", "2"),
            Ingredient("Milk", "1 cup")
        ]
        self.recipe = Recipe("Cake", self.ingredients, "Mix all ingredients and bake.")

    def test_recipe_attributes(self):
        self.assertEqual(self.recipe.name, "Cake")
        self.assertEqual(self.recipe.ingredients, self.ingredients)
        self.assertEqual(self.recipe.instructions, "Mix all ingredients and bake.")

    def test_add_ingredient(self):
        new_ingredient = Ingredient("Butter", "1/2 cup")
        self.recipe.add_ingredient(new_ingredient)
        self.assertIn(new_ingredient, self.recipe.ingredients)

    def test_remove_ingredient(self):
        ingredient_to_remove = self.ingredients[1]
        self.recipe.remove_ingredient(ingredient_to_remove)
        self.assertNotIn(ingredient_to_remove, self.recipe.ingredients)

if __name__ == '__main__':
    unittest.main()
