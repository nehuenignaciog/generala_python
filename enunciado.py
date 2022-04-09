# Python Inicial [Python]
# Ejercicio integrador

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números
(la función "lista_aleatoria" se creó en los ejercicios de profudización de funciones)

Esa lista de datos generada aleatoriamente se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos de anexo de la clase de funciones en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamda "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para buscar sacar generala.

Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo canto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice


def lista_aleatoria(inicio, fin, cantidad):
    lista_numeros = []
    for i in range(cantidad):
        numero = random.randint(inicio, fin)
        lista_numeros.append(numero)
    return lista_numeros


def contar(lista, numero_contar):
    return lista.count(numero_contar)


def valor_repetido(lista):
    numero_repetido = max(lista, key=lista.count)

    if contar(dados_tirados, numero_repetido) > 1:
        return numero_repetido
    else:
        return 0


def pregunto_jugar(tiradas):
    if tiradas > 0:
        respuesta = str(input("\n¿Quiere volver tirar los dados ? SI / NO\n"))
    else:
        respuesta = str(input("\n¿Quiere tirar los dados ? SI / NO\n"))

    respuesta = respuesta.lower()
    if respuesta == 'si':
        return True
    else:
        return False


# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    jugar = True
    tiradas = 0
    contador_generala = 0
    numero_repetido = 0

    jugar = pregunto_jugar(tiradas)

    while jugar:
        tiradas += 1
        cantidad_dados = 5

        # Muestro el numero de la tirada

        print ("\nNumero de tiradas:", tiradas)

        # Primera tirada
        # Vuelvo ingresar si no sacaron mas de 2 dados iguales

        if contador_generala < 2:

            dados_tirados = lista_aleatoria(1, 6, cantidad_dados)
            print ("Dados Tirados:", dados_tirados)

            numero_repetido = valor_repetido(dados_tirados)
            print ("Numero repetido:", numero_repetido)

            contador_generala = contar(dados_tirados, numero_repetido)
            print ("Cantidad Repeticiones:", contador_generala)

            if contador_generala < 2:
                print ("Ustede necesita al menos dos dados iguales. Vuelva a intentarlo!")

        else:

            cantidad_dados -= contador_generala

            dados_tirados = lista_aleatoria(1, 6, cantidad_dados)
            print ("Dados Tirados:", dados_tirados)

            repeticiones_numero_1 = contar(dados_tirados, numero_repetido)

            # Si coincide el numero, sumo el contador de dados

            if repeticiones_numero_1 >= 1:
                contador_generala += contar(dados_tirados, numero_repetido)
                print ("Estas con suerte! Usted ya tiene {} dados ".format(contador_generala))

            else:
                print ("ops.. vuelve a intentarlo! Usted necesita sacar  el número {}".format(numero_repetido))

        # Cuando completo todos los dados iguales, salgo del programa

        if contador_generala == 5:
            break

        jugar = pregunto_jugar(tiradas)

print ("\nGenerala !!!\nFelicitaciones !\n")
