<h1 align="center">Checkpoint 5</h1>
<h2 align="center">Rubens Ballester Lillo</h2>

<h3 align="center">¿Qué son los condicionales en Python?</h3>  

#### Introducción  

Los condicionales son una parte fundamental de la porgramación con Python ya que permite a los programas tomar decisiones basadas en si se cumplen o no una serie de condiciones que nosotros pondremos. En Python los condicionales se implementean a través de la sintaxis: "if", "elif" (else if) y "else".  

#### Sintaxis  

La sintaxis básica de los condicionales es la siguiente:  

```
if condición:
    # Si la condición es verdad se ejecutará el código.

elif otra_condición:
    # Si la condición anterior no se cumple pero esta si, se ejecutará este código.

else:
    # Si ninguna de las condiciones anteriores se cumple se ejecutará este código.

```
- La palabra clave "if" indica el inicio de la estructura condicional. Se evalúa la condición después de if, y si es verdadera, se ejecuta el bloque de código que hayamos creado debajo.
- "elif" se utiliza para verificar condiciones adicionales si la primera condición no es verdadera.
- "else" se utiliza como un condicional final que se ejecuta si ninguna de las condiciones anteriores es verdadera.


> [!IMPORTANT]
> Es importante tener en cuenta que solo if es obligatorio en un condicional. elif y else son opcionales, pero pueden proporcionar lógica adicional a tu programa.

#### Ejemplos de Uso  

Un ejemplo de uso de este tipo de condicionales sería comprobar si un numero es positivo o negativo:  

```
numero = 10

if numero > 0:
    print("El número es positivo")

elif numero < 0:
    print("El número es negativo")

else:
    print("El número es cero")

```

Otro ejemplo sería comprobar si un numero es par o impar: 

```
numero = 15

if numero % 2 == 0:
    print("El numero es par")

else:
    print("El numero es impar")

```

> [!NOTE]
> En este ejemplo, el operador % calcula el resto de la división entre numero y 2. Si el resto es igual a 0, significa que el número es divisible por 2, lo que indica que es par. Si el resto no es igual a 0, el número es impar. El código imprime un mensaje adecuado según el resultado.

#### Conclusión

Los condicionales en Python son una herramienta poderosa que permite que tus programas tomen decisiones basadas en si se cumplen o no ciertas condiciones. Dominar el uso de condicionales te permite escribir código más robusto y funcional.  


<h3 align="center">¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?</h3>  

#### Introducción

Los bucles son estructuras de control que nos permiten repetir un bloque de código varias veces. En Python, existen principalmente dos tipos de bucles: "for" y "while". Cada tipo de bucle tiene su propio propósito y es útil en diferentes situaciones, a continuación detallaremos ambos tipos.

#### Bucle "for"

El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto, o cadena) y ejecutar un bloque de código para cada elemento de la secuencia.

##### Sintaxis:

Su sintaxis comienza con "for" seguido del nombre que queramos dar a los elementos de la secuencia, despues se usa "in" y el nombre de la variable que almacena la secuencia:

```
for elemento in secuencia:
    # Código a ejecutar en cada iteración

```

##### Ejemplo:
```
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

> [!TIP]
> Normalmente cuando tenemos una variable que contiene una lista, tupla, diccionario, etc, definida como en el caso anterior en plural, "frutas", y queremos crear un "for" loop para iterar sobre los elementos que estan dentro de esta variable, se suele usar el nombre en singular "fruta", de forma que quedaría:
> ```for fruta in frutas:```
##### Salida:
```
manzana
banana
cereza
````
> [!NOTE]
> Como podemos observar en la salida, el programa nos imprime cada fruta de la lista frutas.

Otra forma ampliamente utilizada para usar el bucle "for" es hacerlo con la función "range()", esta función nos permite introducirle dos argumentos que serán el numero con el que empieza el rango y el numero siguiente al que queremos que termine el rango, por ejemplo:

##### Ejemplo
```
for i in range(0, 6):
  print(i)
```

##### Salida
```
0
1
2
3
4
5
```
#### Bucle "while"

El bucle while se utiliza para repetir un bloque de código mientras una condición especificada sea verdadera. La condición se evalúa antes de cada iteración y, si es verdadera, se ejecuta el bloque de código.

##### Sintaxis:
```
while condición:
    # Código a ejecutar mientras la condición sea verdadera
```

##### Ejemplo:
```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
##### Salida:
```
0
1
2
3
4
```
> [!NOTE]
> Como podemos observar en el ejemplo, definimos "contador = 0" y ejecutamos el loop "while" mientras se de la condición "contador < 5", lo que hace el bucle es que cada vez que se itera imprime el valor almacenado en contador y le suma 1 a ese valor, en el momento en el que la variable contador es mayor o igual que 5, la condición deja de cumplirse y por lo tanto se termina el bucle.

#### ¿Por qué son útiles los bucles?

Los bucles son útiles porque permiten automatizar tareas repetitivas sin tener que escribir código repetitivo manualmente. Al utilizar bucles, puedes reducir la cantidad de código que necesitas escribir y hacer tu código más conciso y legible. Además, los bucles te permiten procesar grandes cantidades de datos de manera eficiente, ya que puedes realizar operaciones en cada elemento de una secuencia sin tener que repetir las mismas instrucciones una y otra vez.

> [!TIP]
> Elige un bucle "for" cuando sepas exactamente cuántas iteraciones necesitas o cuando estés iterando sobre una secuencia conocida. Utiliza un bucle "while" cuando necesites iterar basándote en una condición y no sepas cuántas iteraciones se necesitarán de antemano.

En resumen, los bucles son una herramienta fundamental en la programación que te permite repetir operaciones de manera eficiente y automatizada, lo que hace que tu código sea más eficiente y fácil de mantener.


<h3 align="center">¿Qué es una lista por comprensión en Python?</h3>

#### Introducción

Una lista por comprensión es una característica poderosa y concisa de Python que te permite crear listas de forma reducida y eficiente mediante la aplicación de una expresión a cada elemento de una secuencia o iterador. Las listas por comprensión son una forma legible y compacta de escribir código, lo que las hace muy útiles en la programación diaria.

#### Sintaxis

La sintaxis básica de una lista por comprensión en Python es la siguiente:
```
nueva_lista = [expresion for elemento in secuencia if condicion]
```
- expresion: Una expresión que se aplica a cada elemento de la secuencia.
- elemento: Variable que representa cada elemento de la secuencia.
- secuencia: La secuencia o iterable sobre la cual se va a iterar.
- condicion (opcional): Una condición que filtra los elementos de la secuencia.

#### Ejemplos:

##### Ejemplo 1: Obtener los cuadrados de los primeros 5 numeros.

```
cuadrados = [i**2 for i in range(1, 6)]
# Salida: [1, 4, 9, 16, 25]
```
> [!NOTE]
> En este ejemplo podemos ver como en primer lugar le decimos que cada elemento de la secuencia (i) lo eleve al cuadrado con la expresión "i**2" y despues lo imprimia en un rango entre 1 y 6, ya que recordemos que la función range() itera hasta el numero anterior del que le hemos indicado que finalice.

##### Ejemplo 2: Imprimir los cuadrados solo de los pares.

```
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero**2 for numero in numeros if numero % 2 == 0]
# Salida: [4, 16]
```

> [!NOTE]
> En este ejemplo podemos apreciar también el uso de un condicional dentro de nuestra lista por comprensión, en esta ocasión estamos diciendo que si numero de la lista es par, haga su cuadrado y lo devuelva, de esa forma el resultado es una lista donde encontramos los cuadrados del numero 2 y el numero 4, que son los unicos pares en la lista que hemos introducido.

#### Ventajas de las Listas por Comprensión

- Sintaxis concisa: Las listas por comprensión permiten escribir código de manera más concisa y legible, reduciendo la cantidad de líneas de código necesarias para realizar operaciones comunes en listas.
- Eficiencia: Las listas por comprensión son eficientes tanto en términos de rendimiento como de uso de recursos. En general, son más rápidas que los enfoques tradicionales de bucles for.
- Facilidad de Uso: Las listas por comprensión son fáciles de entender y utilizar, especialmente para aquellos familiarizados con la programación funcional.

#### Conclusión

Las listas por comprensión son una característica extremadamente útil en Python debido a su capacidad para simplificar y acortar el código mientras se mantiene la legibilidad y la eficiencia. Son una herramienta esencial en el kit de herramientas de todo programador de Python. Facilitan la escritura de código más limpio, más eficiente y más legible, lo que conduce a un desarrollo más rápido y menos propenso a errores.
  

<h3 align="center">¿Qué es un argumento en Python?</h3>

#### Introducción

Los argumentos son valores que se pasan a una función cuando se llama. En Python, las funciones pueden aceptar diferentes tipos de argumentos, como valores simples, listas, tuplas, diccionarios y más. Comprender cómo funcionan los argumentos es fundamental para escribir funciones flexibles y reutilizables en Python.

#### Tipos de Argumentos:

En Python, existen principalmente tres tipos de argumentos que se pueden pasar a una función:

1. Argumentos posicionales: Son argumentos que se pasan a una función en el orden en que se definen. El número de argumentos posicionales debe coincidir con el número de parámetros de la función. Popr ejemplo:
   
```
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años.")

saludar("Rubens", 31)
# Salida: Hola, Rubens. Tienes 31 años.
```
2. Argumentos de palabra clave: Son argumentos que se pasan a una función utilizando el nombre del parámetro al que se desea asignar el valor. Esto permite cambiar el orden de los argumentos sin afectar el resultado. Por ejemplo:
```
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años.")

saludar(edad=31, nombre="Rubens")
# Salida: Hola, Rubens. Tienes 31 años.
```
3. Argumentos predeterminados: Son argumentos que tienen un valor predeterminado en la definición de la función. Si no se pasa ningún valor para estos argumentos al llamar a la función, se utiliza el valor predeterminado. Por ejemplo:
```
def saludar(nombre, edad=31):
    print(f"Hola, {nombre}. Tienes {edad} años.")

saludar("Rubens")
# Salida: Hola, Rubens. Tienes 31 años.
```

#### Conclusión

Los argumentos en Python son fundamentales para la creación de funciones flexibles y reutilizables. Al comprender cómo funcionan los argumentos posicionales, de palabra clave y predeterminados, puedes escribir funciones que sean más fáciles de usar y de mantener. Además, el uso adecuado de los argumentos puede mejorar la claridad y la legibilidad de tu código.


<h3 align="center">¿Qué es una función Lambda en Python?</h3>

#### Introducción

Las funciones lambda, también conocidas como funciones anónimas, son funciones pequeñas y de una sola expresión que se pueden definir de manera concisa en una sola línea de código en Python. Son útiles cuando necesitas una función rápida y simple sin la necesidad de definir una función completa utilizando la palabra clave "def".


#### Caracteristicas principales

- Anonimato: Las funciones lambda son funciones anónimas, lo que significa que no se les asigna un nombre como las funciones definidas con la palabra clave "def".
- Simplicidad: Las funciones lambda son útiles para definir funciones pequeñas y de una sola expresión de manera rápida y concisa.
- Expresiones Únicas: Las funciones lambda están diseñadas para expresiones simples y no admiten múltiples declaraciones o bloques de código.

#### Sintaxis 

La sintaxis básica de una función lambda en Python es la siguiente:
```
lambda argumentos: expresión
```
- lambda: Es la palabra clave que indica que se está creando una función lambda.
- argumentos: Son los parámetros de entrada de la función lambda.
- expresión: Es la operación que la función realiza utilizando los argumentos.

  
#### Ejemplo:
```
cuadrado = lambda x: x ** 2
```
> [!NOTE]
> En este ejemplo, cuadrado es una función lambda que toma un argumento x y devuelve el cuadrado de x.

#### Otro Ejemplo:
```
suma = lambda x, y: x + y
print(suma(3, 5))
# Salida: 8
```
> [!NOTE]
> En este ejemplo, suma es una función que requiere de dos argumentos y luego los suma.

#### Conclusión

Las funciones lambda son una característica poderosa y útil en Python que te permite crear funciones anónimas de manera concisa y eficiente. Son ideales para situaciones donde necesitas una función rápida y simple sin la necesidad de definir una función completa con "def". Al comprender cómo funcionan las funciones lambda, puedes escribir código más limpio y más legible en Python.

<h3 align="center">¿Qué es un paquete pip?</h3>

#### Introducción

En el ecosistema de Python, los paquetes son colecciones de módulos que pueden incluir funciones, clases y variables. Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Es una herramienta esencial para trabajar con bibliotecas de otros desarroladores y para mantener las dependencias de un proyecto de Python.

#### ¿Qué es Pip?

Pip es una herramienta de línea de comandos utilizada para instalar y administrar paquetes de software escritos en Python. Permite buscar, descargar, instalar, actualizar y desinstalar paquetes de Python desde el repositorio de Python Package Index (PyPI) y otros repositorios.

#### Principales características de Pip

- Instalación de Paquetes: Pip facilita la instalación de paquetes de Python con una simple línea de comandos.
- Gestión de Dependencias: Pip maneja automáticamente las dependencias de los paquetes instalados, asegurando que todas las bibliotecas necesarias estén presentes y actualizadas.
- Actualización de Paquetes: Pip permite actualizar los paquetes instalados a sus versiones más recientes.
- Entornos Virtuales: Pip es compatible con la creación y gestión de entornos virtuales, que son entornos de desarrollo aislados que permiten instalar y administrar dependencias de proyectos de Python sin interferir con el sistema global.

#### Algunos Ejemplos Básicos

- Instalación de un Paquete: Para instalar un paquete, simplemente ejecuta el comando "pip install nombre_del_paquete". Por ejemplo, ```pip install requests``` instala el paquete requests utilizado para hacer solicitudes HTTP en Python.
- Actualización de un Paquete: Para actualizar un paquete podemos usar el comando ```pip install --upgrade nomobre_del_paquete```
- Actualización de Pip: Para actualizar Pip a la última versión, puedes usar el comando ```pip install --upgrade pip```
- Desinstalación de un Paquete: Para desinstalar un paquete, ejecuta el comando ```pip uninstall nombre_del_paquete```

#### Conclusión

Pip es una herramienta esencial en el ecosistema de Python que simplifica la instalación y gestión de paquetes de software. Facilita la administración de dependencias de proyectos de Python y permite a los desarrolladores acceder a una amplia variedad de bibliotecas y herramientas de terceros para mejorar la productividad y la funcionalidad de sus proyectos.

