from models import Recipe, Ingredient, RecipeManager
from views import RecipeView

# Crear una instancia del RecipeManager
recipe_manager = RecipeManager()

# Crear algunas recetas de ejemplo
recipe1 = Recipe("Pizza", ["Harina", "Tomate", "Queso", "Pepperoni"], "Mezcla los ingredientes y hornea.")
recipe2 = Recipe("Ensalada", ["Lechuga", "Tomate", "Aceite de oliva"], "Corta los ingredientes y mézclalos en un recipiente.")

# Agregar las recetas al RecipeManager
recipe_manager.create_recipe(recipe1)
recipe_manager.create_recipe(recipe2)

# Crear una instancia de RecipeView
recipe_view = RecipeView(recipe_manager)

# Mostrar todas las recetas en la consola
recipe_view.display_all_recipes()

# Mostrar los detalles de una receta específica
recipe_view.display_recipe_details(1)

# Crear una nueva receta
new_recipe = Recipe("Pastel de Chocolate", ["Harina", "Cacao en polvo", "Azúcar", "Huevos"], "Mezcla los ingredientes y hornea.")
recipe_view.create_recipe(new_recipe)

# Actualizar una receta existente
updated_recipe = Recipe("Ensalada de Frutas", ["Manzanas", "Naranjas", "Plátanos"], "Corta las frutas y mézclalas en un recipiente.")
recipe_view.update_recipe(2, updated_recipe)

# Eliminar una receta existente
recipe_view.delete_recipe(1)