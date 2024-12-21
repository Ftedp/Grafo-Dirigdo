# GrafoDirigdo
Encuentra el Palindromo más cercano de una palabra dada
Programación 2
Tecnicatura Universitaria en Inteligencia Artificial
2024
GRAFOS - EJERCICIOS PARA ENTREGAR
Problema de aplicación: abba

Dada una cadena de caracteres S la operación reemplaza(a, b) cambia cada una de las ocurrencias del carácter a por el
caracter b. Por ejemplo, si S = abracadabra y aplicamos la operación reemplaza(b, c), obtenemos la cadena resultante:
acracadacra, donde todas las “b” fueron reemplazadas por “c”.
Un palíndromo es una cadena de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda. Algunos
ejemplos de palíndromos son “abba”y “dad”. Esto es importante porque en este ejercicio el objetivo es transformar una
cadena en un palíndromo aplicando la operación de reemplazo.

El grafo de reemplazos:
Dado un número natural n y un alfabeto (conjunto de caracteres), definimos el grafo de reemplazos Gr como un grafo
dirigido Gr = (V, E) de la siguiente manera:
Vértices (V ) Los vértices de Gr son todas las posibles cadenas de caracteres de longitud n. Denotamos esto como
V = {s : len(s) = n}, donde len(s) asegura que todas las cadenas tengan la misma longitud. Por ejemplo, si n = 3,
V podría contener cadenas como “aaa”, “abc”, “bac” y así sucesivamente, hasta cubrir todas las combinaciones
posibles de tres caracteres.
Aristas (E) Dos nodos s y s ′están conectados por una arista si existe una operación reemplaza(a, b) que transforma en s′. 
Formalmente, esto se expresa como E = {(s, s′) : ∃b, c tal que s′ = s.reemplaza(b, c)}. Esto significa que
si puedes convertir una cadena s en otra cadena s ′reemplazando todas las apariciones de un carácter por otro,
entonces hay una conexión directa entre s y s′ en el grafo.
Ejemplo Si n = 2 y consideramos nuestro alfabeto como {a, b} obtendríamos el siguiente grafo:
Sus vértices son “aa”, “ab”, “ba”, y “bb”. Son todas las posibles cadenas de caracteres de longitud 2 que utilizan solo
los carácteres a y b.
Las aristas representarían los posibles reemplazos de un carácter por otro. Por ejemplo:
• Si aplicamos reemplaza(a, b) a “aa” obtenemos “bb” por lo que habría una arista entre “aa”y “bb”.
• De manera similar, aplicando reemplaza(b, a) a “ab” nos da “aa” creando una conexión entre “ab”y “aa”.
• ..............................................................................................................

Programación II – 2024
El grafo tendría la siguiente pinta:
aa bb
ab ba

Tareas a implementar:
Se provee un esqueleto a completar. Sobre ello, realizar las siguientes tareas.
1. Implemente una función es_palindromo que reciba un string y determine si es un palíndromo.
2. Implemente una clase GrafoDirigido que represente grafos dirigidos utilizando un diccionario de nodos a vecinos.
3. Implemente una función generar_G_r que reciba un número positivo n y un alfabeto y genere el grafo de reemplazos
que incluya esa palabra. Pueden ser de utilidad las funciones del módulo itertools1.
4. Implemente una función distancia_a_palindromo que reciba una palabra y el grafo de reemplazos que la contiene
y utilice el grafo de reemplazos para encontrar la mínima cantidad de operaciones de reemplazo que deben utilizarse
para lograr que la palabra sea un palíndromo. Por ejemplo, si la palabra recibida es papeleo, debe devolver 3, porque
puede realizar la secuencia de reemplazos: papeleo −→ papelep −→ pepelep −→ lelelel (y no puede realizarse
con solo dos reemplazos).

Aclaraciones:
Puede suponer que el alfabeto siempre consistirá de letras minúsculas del alfabeto español.
La palabra a evaluar tendrá una longitud de entre 1 y 8 caracteres.
La palabra a evaluar nunca tendrá más de 4 letras distintas.

Entrega y evaluación:
Los estudiantes deben entregar el código completo en los archivos proporcionados. No se deben utilizar archivos
auxiliares ni bibliotecas, salvo las explícitamente sugeridas. El trabajo práctico se evaluará utilizando una serie de
casos de prueba de caja negra, por lo que es fundamental que no cambien los nombres ni las firmas de las funciones
y clases propuestas. Además, se valorará la calidad del código y se realizará una breve defensa del trabajo (junto a la
defensa del TP final).

Trabajo en grupo: Los ejercicios deben resolverse en grupos de 2 o 3 estudiantes (en casos excepcionales se permitirá
entrega individual, pero no se aceptarán grupos de más de 3 estudiantes). Sugerimos conformar el mismo grupo que
resolverá el TP final. Todos los integrantes del grupo deben comprender completamente el contenido presentado en el
trabajo. Esto implica que cada miembro debe ser capaz de explicar, discutir y defender todas las partes del proyecto.
