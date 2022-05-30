# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos Geneticos

Author: David Flores García
        Oscar Josue Jattar Velazquez
        Rogelio Ortega Barrera

Descripción:  Resolver una ecuacion lineal 

"""

import random # Importamos la biblioteca random

class FitnessFunction:# Definimos la clase FitnessFunction

    # Definimos la clase seleccion que tiene como parametros la poblacion
    # cromosomas y generacion
    def seleccion(poblacion, cromosomas, generacion):
        # Definimos una variable puntuacion la cual vamos a ir guardando
        # la calificacion que va a tener cada cromosoma
        puntuacion=[]
        # Con un ciclo for vamos a ir guardando gen por gen de la encuacion
        # en la poblacion
        for gen in poblacion:
            # La ecuacion va a estar definida gen por gen, esto nos genera
            # arreglo por arreglo
            ecuacion=100-abs(30-(gen[0]+2*gen[1]-3*gen[2]+gen[3]+4*gen[4]+gen[5]))
            # Vamos guardando cada puntuacion de la ecuacion
            puntuacion.append(ecuacion)
        # En la variable total, vamos a sumar cada puntuacion obtenida de cada gen
        total=sum(puntuacion)
        # Imprimimos la puntuacion obtenida
        print('Puntuacion de los valores obtenidos: ', total)
        # Generamos una lista zip de puntuacion y la poblacion
        totales=list(zip(puntuacion,poblacion))
        # Decidimos organizar con la funcion sort a totales de manera descendente
        totales.sort(reverse=True)
        # Con el for vamos a ir recorriendo cada total de la lista zip
        for individual in totales:
            # Si el total en la posicion 0 es igual a 100, que es la maxima
            # puntuacion que puede obtener cada gen
            if individual[0]==100:
                # Si individual en la posicion 1 no esta en cromosomas
                if individual[1] not in cromosomas:
                    # vamos agregando
                    cromosomas.append(individual[1])
        # Totales ahora tendra a solo los mejores 4 cromosomomas de la poblacion
        totales=totales[:4]
        #Obtenemos la poblacion y la regresamos en forma de lista
        score, poblacion=zip(*totales)
        return list(poblacion)
    # Definimos la funcion cruza que tiene como parametro poblacion
    def cruza(poblacion):
        # Con random shuffle vamos a desordenar a la poblacion que ya tenemos
        random.shuffle(poblacion)
        # El cromosoma padre va a tener la primera parte de la poblacion
        cromosomaPadre=poblacion[:2]
        # El cromosoma madre va a tener la otra mitad
        cromosomaMadre=poblacion[2:]
        # Creamos una variable hijo que va a tener la cruza 
        hijo=[]
        # Mediante un for vamos a ir recorriendo dependiendo el tamaño del
        # cromosoma padre
        for i in range(len(cromosomaPadre)):
            # Generamos una cruza aleatoria entre 1 y 5
            cruza=random.randint(1,5)
            # papa va a tener al cromosoma padre en la posicion de i en cada
            # recorrido
            papa=[cromosomaPadre[i][:cruza],cromosomaPadre[i][cruza:]]
            # mama va a tener al cromosoma madre en la posicion de i en cada
            # recorrido
            mama=[cromosomaMadre[i][:cruza],cromosomaMadre[i][cruza:]]
            # hijo 1 va a tener a papa en la posicion 0 y le sumamos 
            # a la mama en la posicion 1
            hijo1=papa[0]+mama[1]
            # agregamos del hijo1 al hijo
            hijo.append(hijo1)
            # hijo2 va a tener ahora a mama en la posicion 0 y al papa en la
            # posicion 2
            hijo2=mama[0]+papa[1]
            # Agregamos a hijo el contenido de hijo 2
            hijo.append(hijo2)
        return hijo# Regresamos al hijo
    
    # Generamos a la funcion mutar que recibe como parametro poblacion
    def mutar(poblacion):
        # Definimos una variable cromosomaMutado
        cromosomaMutado=[]
        # Con el for vamos recorriendo cada cromosoma en la poblacion
        for cromosoma in poblacion:
            # En mutacion sitio generamos numeros aleatorios de cada una de los
            # genes
            mutacionSitio=random.randint(0,5)
            # Cromosoma de mutacionSitio sera de numeros aleatorios
            # del 1 al 9
            cromosoma[mutacionSitio]=random.randint(1,9)
            # Agregamos en cromosoma mutado a cada cromosoma
            cromosomaMutado.append(cromosoma)
        return cromosomaMutado# Regresamos al cromosoma mutado
    
    # Definimos a la funcion obtenerCromosoma que tiene como parametros
    # a las generaciones, seleccion, cruza y mutar
    def obtenerCromosoma(generaciones,seleccion,cruza,mutar):
        # En poblacion vamos a generar numeros aleatorios del 1 al 9
        # en el rango de 6 por la cantidad de letras en la ecuacion
        poblacion=[[random.randint(1,9) for i in range(6)] for j in range(6)]
        # Definimos a la variable cromosomas
        cromosomas=[]
        # Con un for recorremos para cada generacion en el rango de generaciones
        for generacion in range(generaciones):
            # Generaciones va a incrementar de uno en uno
            generacion+=1
            # Imprimimos a la generacion
            print('Generacion:', generacion)
            # poblacion es igual a la funcion seleccion
            poblacion=seleccion(poblacion, cromosomas, generacion)
            # hijo cruza es igual a la funcion cruza
            hijoCruza=cruza(poblacion)
            # poblacion es la suma de la poblacion mas el hijoCruza
            poblacion=poblacion+hijoCruza
            # poblacion mutada es igual a la funcion mutar
            poblacionMutada=mutar(poblacion)
            # poblacion es igual a la poblacion mas la poblacion mutada
            poblacion=poblacion+poblacionMutada
        return cromosomas# regresamos a los cromosomas
    # En la variable solucion vamos a pasar a la funcion obtenerCromosoma
    solucion=obtenerCromosoma(1000,seleccion,cruza,mutar)
    print('-----------Posibles soluciones de la ecuacion-----------')
    print(solucion)# Imprimimos la solucion
    print(len(solucion))# Imprimimos el tamaño de la solucion