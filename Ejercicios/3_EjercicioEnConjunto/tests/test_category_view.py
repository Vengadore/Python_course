import unittest
from unittest.mock import patch
from io import StringIO
from views import CategoryView

class TestCategoryView(unittest.TestCase):
    def setUp(self):
        self.category_view = CategoryView()

    def test_display_categories(self):
        expected_output = "Categories:\n- Main Course\n- Dessert\n- Salad\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.category_view.display_categories(['Main Course', 'Dessert', 'Salad'])
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_prompt_category(self):
        expected_output = "Please enter a category: "
        user_input = "Dessert"
        with patch('sys.stdout', new=StringIO()) as fake_out, patch('builtins.input', return_value=user_input):
            category = self.category_view.prompt_category()
            self.assertEqual(fake_out.getvalue(), expected_output)
            self.assertEqual(category, user_input)

if __name__ == '__main__':
    unittest.main()