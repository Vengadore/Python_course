# Proyecto: Gestor de Recetas

## Descripción

El Gestor de Recetas es una aplicación de línea de comandos que permite a los usuarios gestionar y organizar su colección de recetas. Proporciona una interfaz intuitiva para realizar diversas operaciones, como agregar, editar, buscar y eliminar recetas, así como crear y gestionar categorías de recetas. La aplicación utiliza un archivo CSV como base de datos para almacenar la información de las recetas.

El proyecto se ha estructurado siguiendo una arquitectura modularizada, con diferentes componentes encargados de diferentes responsabilidades. Los modelos se encargan de representar las entidades principales de la aplicación, como las recetas y las categorías, y proporcionan métodos para manipular y acceder a los datos. Las vistas se encargan de la interacción con el usuario, mostrando las opciones disponibles y permitiendo realizar las operaciones deseadas. Las utilidades proporcionan funciones adicionales para leer y escribir datos en el archivo CSV.

El proyecto también incluye un conjunto completo de pruebas unitarias para asegurar la calidad y el correcto funcionamiento de las diferentes partes de la aplicación. Las pruebas cubren aspectos como la creación de recetas y categorías, la modificación y eliminación de recetas existentes, la visualización de listas y detalles de recetas, y otras operaciones clave.

El equipo de desarrollo consiste en tres personas, quienes trabajarán en el proyecto de forma colaborativa en un repositorio Git. El uso de Git permitirá una gestión eficiente del código fuente y facilitará la colaboración y la resolución de conflictos durante el desarrollo del proyecto.

## Estructura del Proyecto

```markdown
gestor_recetas/
├── README.md
├── main.py
├── models/
│   ├── __init__.py
│   ├── recipe.py
│   └── category.py
├── views/
│   ├── __init__.py
│   ├── recipe_view.py
│   └── category_view.py
├── utils/
│   ├── __init__.py
│   └── csv_handler.py
└── tests/
    ├── __init__.py
    ├── test_recipe.py
    ├── test_category.py
    ├── test_recipe_view.py
    ├── test_csv_storage.py
    └── test_category_view.py
```
Descripción detallada del contenido de las carpetas:

`models/`: Este directorio contiene los modelos de datos relacionados con las recetas y categorías.

- `__init__.py`: Archivo de inicialización del paquete models.

- `recipe.py`: Define la clase Recipe en la cual se deben incluir métodos relacionados con las operaciones específicas de las recetas, como agregar receta, editar receta, eliminar receta, obtener detalles de una receta, etc.

- `category.py`: Define la clase Category en la cual se deben incluir métodos relacionados con las operaciones específicas de las categorías, como crear categoría, editar categoría, eliminar categoría, obtener lista de categorías, etc.

`views/`: Este directorio contiene los controladores y vistas de la aplicación.

- `__init__.py`: Archivo de inicialización del paquete views.

- `recipe_view.py`: Contiene las funciones y métodos relacionados con la visualización de las recetas en la interfaz de usuario, como mostrar lista de recetas, mostrar detalles de una receta, etc.

- `category_view.py`: Contiene las funciones y métodos relacionados con la visualización de las categorías en la interfaz de usuario, como mostrar lista de categorías, mostrar recetas en una categoría específica, etc.

`utils/`: Este directorio contiene utilidades y funciones auxiliares para la aplicación.

- `__init__.py`: Archivo de inicialización del paquete `utils`.

- `csv_handler.py`: Este archivo contiene funciones para leer y escribir datos en el archivo CSV que actúa como base de datos. Incluye las siguientes funciones:

  - `read_recipes_from_csv(file_path: str) -> List[Dict[str, Any]]`: Lee las recetas almacenadas en el archivo CSV y las devuelve como una lista de diccionarios, donde cada diccionario representa una receta con sus atributos.

  - `write_recipes_to_csv(file_path: str, recipes: List[Dict[str, Any]]) -> None`: Escribe una lista de recetas en el archivo CSV. Recibe como parámetros la ruta del archivo CSV y la lista de recetas como diccionarios.

  - `add_recipe_to_csv(file_path: str, recipe: Dict[str, Any]) -> None`: Agrega una nueva receta al archivo CSV existente. Recibe como parámetros la ruta del archivo CSV y la receta como un diccionario.

  - `update_recipe_in_csv(file_path: str, recipe: Dict[str, Any]) -> None`: Actualiza una receta existente en el archivo CSV. Recibe como parámetros la ruta del archivo CSV y la receta actualizada como un diccionario.

  - `delete_recipe_from_csv(file_path: str, recipe_id: int) -> None`: Elimina una receta del archivo CSV según su ID.

Estas utilidades proporcionan funciones para leer y escribir datos en el archivo CSV, así como para agregar, actualizar y eliminar recetas específicas. Permiten una interacción eficiente con la base de datos y aseguran que los cambios se reflejen correctamente en el archivo CSV.

El uso de estas utilidades garantiza que las recetas se guarden y persistan correctamente en el archivo CSV, lo que facilita la gestión y el mantenimiento de la colección de recetas.


`tests/`: Este directorio contiene los archivos de prueba para realizar pruebas unitarias en la lógica y visualización de la aplicación.

- `test_recipe.py`: Este archivo de prueba debería incluir pruebas unitarias para el modelo y la lógica relacionada con las recetas. Algunos ejemplos de pruebas pueden ser:

    - Verificar que una receta se pueda crear correctamente con los atributos correctos.
 
    - Comprobar que se pueda editar una receta y que los cambios se reflejen correctamente.
    
    - Asegurarse de que una receta se pueda eliminar correctamente y que ya no esté presente en la lista de recetas.

    - Validar que se puedan obtener los detalles de una receta correctamente y que los datos sean precisos.

- `test_category.py`: Este archivo de prueba debería incluir pruebas unitarias para el modelo y la lógica relacionada con las categorías. Algunos ejemplos de pruebas pueden ser:

    - Verificar que se pueda crear una categoría correctamente con los atributos adecuados.
    - Comprobar que se pueda editar una categoría y que los cambios se reflejen correctamente.
    - Asegurarse de que una categoría se pueda eliminar correctamente y que ya no esté presente en la lista de categorías.
    - Validar que se puedan obtener las recetas de una categoría correctamente y que los datos sean precisos.

- `test_recipe_view.py`: Este archivo de prueba debería incluir pruebas para la visualización y las operaciones relacionadas con las recetas en la interfaz de usuario. Algunos ejemplos de pruebas pueden ser:

    - Verificar que se pueda mostrar correctamente la lista de recetas.
    - Comprobar que se muestren los detalles de una receta específica de manera precisa.
    - Asegurarse de que se manejen correctamente las operaciones de agregar, editar y eliminar recetas en la interfaz de usuario.

- `test_category_view.py`: Este archivo de prueba debería incluir pruebas para la visualización y las operaciones relacionadas con las categorías en la interfaz de usuario. Algunos ejemplos de pruebas pueden ser:

    - Verificar que se pueda mostrar correctamente la lista de categorías.
    - Comprobar que se muestren las recetas de una categoría específica de manera precisa.
    - Asegurarse de que se manejen correctamente las operaciones de crear, editar y eliminar categorías en la interfaz de usuario.

- `test_csv_handler.py`: Este archivo contiene pruebas para verificar el manejo del archivo CSV y el almacenamiento de las recetas. Incluye las siguientes pruebas:

  - `test_read_recipes_from_csv`: Verifica que se puedan leer las recetas almacenadas en el archivo CSV y se devuelvan correctamente como una lista de diccionarios.
  - `test_write_recipes_to_csv`: Comprueba que las recetas se puedan escribir correctamente en el archivo CSV y que se guarden con la estructura adecuada.
  - `test_add_recipe_to_csv`: Verifica que una nueva receta se pueda agregar correctamente al archivo CSV existente y se guarde correctamente.
  - `test_update_recipe_in_csv`: Comprueba que una receta existente se pueda actualizar correctamente en el archivo CSV y que los cambios se reflejen adecuadamente.
  - `test_delete_recipe_from_csv`: Verifica que una receta se pueda eliminar correctamente del archivo CSV según su ID y que se actualice el archivo correctamente.

Las pruebas unitarias son fundamentales para garantizar el correcto funcionamiento de la aplicación y detectar posibles errores o fallos en la lógica. Cada archivo de prueba debe incluir una variedad de casos de prueba que cubran diferentes escenarios y situaciones para garantizar la calidad del código y su comportamiento esperado.


# Trabajo en equipo

En función de las tareas asignadas a cada programador, a continuación se describen los roles correspondientes a los tres miembros del equipo:

## Programador de Modelos:


- Diseñar y desarrollar los modelos de datos necesarios para representar las recetas y cualquier otra entidad relacionada.
- Definir las relaciones y las estructuras de los modelos para garantizar la coherencia y la integridad de los datos.
- Implementar las funciones y los métodos en los modelos para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos.
- Validar y asegurar la consistencia de los datos almacenados en los modelos.
- Colaborar con los otros programadores para establecer las interfaces y los requisitos de los modelos necesarios para la visualización y el almacenamiento en archivos.

## Programador de Visualización:

- Diseñar y desarrollar la interfaz de usuario para la aplicación del gestor de recetas, en este caso puede ser sólo la representación en la línea de comandos.
- Garantizar la usabilidad, la accesibilidad y la experiencia del usuario en la aplicación.
- Integrar las funcionalidades y los datos de los modelos en la interfaz de usuario.
- Realizar pruebas y depurar problemas relacionados con la visualización y la interacción del usuario.
- Colaborar con los otros programadores para definir las interfaces de los modelos y la forma en que se deben mostrar los datos en la interfaz de usuario.
- Ser capaz de visualizar una sola receta
- Ser capaz de visualizar las recetas contenidas en un archivo CSV.

## Programador de Almacenamiento en Archivos:

- Implementar las funciones y los métodos necesarios para leer y escribir datos en el archivo CSV que actúa como base de datos.
- Garantizar la integridad y la consistencia de los datos almacenados en el archivo CSV.
- Desarrollar las funciones para agregar, actualizar y eliminar recetas en el archivo CSV.
- Realizar pruebas y asegurarse de que el almacenamiento en archivos funcione correctamente.
- Colaborar con los otros programadores para definir las interfaces de los modelos y la forma en que los datos se deben almacenar y recuperar en el archivo CSV.

Estos roles permiten una división clara de responsabilidades dentro del equipo y aseguran que cada miembro se enfoque en su área de especialización. Sin embargo, es importante destacar que la comunicación y la colaboración entre los programadores son fundamentales para garantizar la coherencia y la integración del proyecto en su conjunto.