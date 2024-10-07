numero_de_generacion = 1

def poblacion_a_binario(poblacion):
    poblacion_binaria = []
    for i in poblacion:
        binario = bin(i)[2:]
        while len(binario) < 8:
            binario = '0' + binario
        poblacion_binaria.append(binario)
    return poblacion_binaria

def funcion_de_evaluacion(individuo):
    x = int(individuo, 2)
    return x**(2*x) - 1

def cruce(ind1, ind2):
    mitad = len(ind1) // 2 
    individuo_1 = ind1[:mitad] + ind2[mitad:]
    individuo_2 = ind2[:mitad] + ind1[mitad:]
    return individuo_1, individuo_2

def mutacion(individuo):
    if(individuo[len(individuo)-2] == '0'):
        individuo = individuo[:len(individuo)-2] + '1' + individuo[len(individuo)-1]
    else:
        individuo = individuo[:len(individuo)-2] + '0' + individuo[len(individuo)-1]
    return individuo

def generacion(poblacion, generaciones):
    if generaciones == 0:
        return
    global numero_de_generacion
    poblacion_ordenada = sorted(poblacion, reverse=True)
    poblacion_binaria = sorted(poblacion_a_binario(poblacion_ordenada), key=lambda x: funcion_de_evaluacion(x), reverse=True)
    cruces = []
    mutaciones = []
    poblacion_final = []
    funciones_de_evaluacion = []

    for i in poblacion_binaria:
        funciones_de_evaluacion.append(funcion_de_evaluacion(i))

    for i in range(0, len(poblacion_binaria), 2):
        cruce1, cruce2 = cruce(poblacion_binaria[i], poblacion_binaria[i+1])
        cruces.append(cruce1)
        cruces.append(cruce2)

    for i in range(0, len(cruces)):
        mutaciones.append(mutacion(cruces[i]))# mutacion(cruces[i]))

    for i in mutaciones:
        poblacion_final.append(int(i, 2))


    print(f'--------------------------------------------------------Generacion: {numero_de_generacion}---------------------------------------------------------')
    print(f'Poblacion_inicial \t\t\t funcion de evaluacion \t\t\t poblacion binaria \t\t cruce \t\t\t\t mutacion \t\t poblacion_final')
    for i in range(0, len(poblacion_final)):
        print(f'{poblacion_ordenada[i]} \t\t\t {funciones_de_evaluacion[i]} \t\t\t\t {poblacion_binaria[i]} \t\t\t {cruces[i]} \t\t\t {mutaciones[i]} \t\t {poblacion_final[i]}')
    print('\n\n')
    numero_de_generacion += 1


    generacion(poblacion_final, generaciones-1)
poblacion = [9, 7, 4, 3, 1, 6, 13, 10, 5, 12, 8, 11]
generacion(poblacion, 3)


