## Objetivo general

El objetivo general de este ejercicio es crear una suite capaz de representar números complejos. Esta suite es capaz de realizar sumas, restas, multiplicaciones y divisiones. Tambiés es capaz de mostrar la representación de números complejos en su forma rectangular y en su forma polar.

## ¿Qué son los números complejos?

Se entiende por números complejos a la combinación de números reales e imaginarios. La parte real puede ser expresada por un número entero o sus decimales, mientras que la parte imaginaria es aquella cuyo cuadrado es negativo. Los números complejos surgen ante la necesidad de abarcar las raíces de los números negativos, cosa que los reales no pueden hacer. Por esta razón, reflejan todas las raíces de los polinomios.

Su uso abarca distintas ramas científicas, que van desde las matemáticas hasta la ingeniería. Los números complejos pueden, además, representar ondas electromagnéticas y corrientes eléctricas, por lo que su uso en el campo de la electrónica o las telecomunicaciones es fundamental.

Su fórmula matemática es: $a + b j$, donde $a$ y $b$ son números reales y la $j$ es el número imaginario. A esta expresión se le conoce como forma rectangular.

La representación polar está dada por una magnitud y un angulo.

[Más información](https://www.ferrovial.com/es/stem/numeros-complejos/)

## Instrucciones para realizar el ejercicio

Crea una rama que tenga tu nombre a partir del repo más actualizado, por ejemplo:

```
git checkout -B estudiante/Nombre_estudiante_Complejos
```

Existen dos carpetas, **complejos** y **tests**. La carpeta de complejos contiene el código para hacer funcionar la suite, está dividia en varios archivos ya que la intención es seprar la funcionalidad y permitir que varios desarrolladores trabajen en conjunto. La carpeta de tests contiene archivos que prueban la funcionalidad del código haciendo uso del módulo *unittest* de python.

El objetivo es hacer pasar todos los tests y, de ser posible, agregar más. Automaticamente algunos tests pasan para darle al alumno un ejemplo de como es el desarrollo, sientete libre de experimentar y agregar cosas. Si utilizas windows puedes correr todos los tests desde la terminal de esta manera:

```
cd 2_NumerosComplejos
python.exe -m unittest
```

También es posible utilizar las herramientas de VSCode para ejecutar los tests, esto puede ayudarte a debugear. Experimenta todo lo que desees y cada que realices un cambio no olvides ejecutar los tests para asegurarte que lo que ya programaste sigue funcionando!. También puedes ejecutar un sólo archivo de tests, por ejemplo:

```
python.exe -m unittest tests.test_crear_metodos
```


A continuación se explica el contenido de cada archivo contenido en *complejos*.


### Estructura

Este archivo contiene la estructura base de un número complejo, contiene el método para crear un número complejo a partir de los parametros real y complejo. Este método debe retornar una lista que contenga dos números, el primer elemento la parte real y el segundo elemento la parte imaginaria:

```
crear_complejo(parte_real,parte_imaginaria)
```

Además *estructura*, debe contener dos métodos más que se llamen *real* e *imaginario* que retornen el valor real e imaginario de un número complejo creado. Por ejemplo:

```
complejo = crear_complejo(4,5)
real(complejo)
> 4
imaginario(complejo)
> 5
```

Finalmente, debe contener dos métodos más llamados *modulo* y *angulo* que retornen el valor los valores redondeados a dos decimales del valor del módulo y el ángulo del número complejo (estos valores son pertenecientes a la forma polar).

```
complejo = crear_complejo(1,1)
modulo(complejo)
> 1.414
angulo(complejo)
> 45.0
```

### Representación 

Los números complejos, al igual que otro tipo de datos necesitan de una representación especial, para eso crearemos dos funciones llamadas **rectangular** y **polar** las cuales se encargarán de mostrar la representación del número complejo de una forma más amigable para el usuario.

```
complejo = crear_complejo(1,1)
rectangular(complejo)
> 1 + 1j 
polar(complejo)
> 1.414 @ 45.0°
```

### Suma

El archivo de suma debe contener un método llamado **suma_complejos(complejo1,complejo2)** el cual toma dos números complejos y suman. El método debe estar limitado a dos números complejos como parametros de entrada. Esta suma debe ser capaz de imprimirse con los métodos de representación.

```
complejo1 = crear_complejo(1,1)
complejo2 = crear_complejo(2,4)

suma = suma_complejos(complejo1,complejo2)
rectangular(suma)
> 3 + 5j
```


### Resta

El archivo de resta debe contener un método llamado **resta_complejos(complejo1,complejo2)** el cual toma dos números complejos y genera un número complejo nuevo. El método debe estar limitado a dos números complejos como parametros de entrada.

### Multiplicación

El archivo de multiplicacion debe contener un método llamado **multiplicacion_complejos(complejo1,complejo2)** el cual toma dos números complejos y genera un número complejo nuevo. El método debe estar limitado a dos números complejos como parametros de entrada.

### División

El archivo de division debe contener un método llamado **division_complejos(complejo1,complejo2)** el cual toma dos números complejos y genera un número complejo nuevo. El método debe estar limitado a dos números complejos como parametros de entrada.


