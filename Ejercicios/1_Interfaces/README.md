# Instrucciones 

Crear interfaces

Existe un objeto llamado casa, a la casa se le conectan varios dispositivos que tienen diferentes interfaces.
Algunos de estos objetos tienen interfaces parecidas que pueden ser simplificadas en una sola interfaz. La casa permite al usuario interactuar con los objetos creados. También es posible probar los elementos creados haciendo uso directo de su interfaz.

La casa tiene dispositivos mecánicos como:
- Puertas
- Ventanas
- Cajones

Además, tiene elementos eléctricos como electromesticos:
- Focos
- Lavadora
- Televisión
- Licuadora
- Computadora
- Lámpara


Siempre que realices un cambio corre las pruebas para verificar que tus cambios no afectaron al funcionamiento del código.

`python.exe test_interfaces.py`

De ser necesario, actualiza las pruebas para su correcto funcionamiento. Recuerda el ciclo de TDD:

1. Escribe un test que falle
2. Haz que el test pase
3. Refactoriza

Objetivos:

- Comienza habilitando los tests haciendolos funcionar uno por uno, implementa la lógica faltante.
- Crea una interfaz para los elementos mecánicos, que tenga los métodos *abrir* y *cerrar*.
- Crea clases para crear crear televisión, licuadora, lavadora y computadora.
    - La licuadora debe tener un método llamado *seleccionar_velocidad* el cual asigna un nivel de velocidad de 0 a 5, si la licuadora no está encendida, la velocidad es 0, si está encendida esta velocidad puede ser actualizada.
- Agrega las pruebas necesarias para probar la funcionalidad.
- Crea una clase que se llame switch que pueda utilizar la interfaz electrica, los elementos eléctricos pueden tener diferentes switches para encenderlos.