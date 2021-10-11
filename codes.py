
import math as mt


def palindromo(input):
    """
    Ver si un numero entero es palindromo
    """
    var = input
    if var < 0 or int(var/10) == 0:
        return False
    if var == 0:
        return True

    exp = 1
    counter = 0
    valores = []
    while var != 0:

        num = var%10
        valores.append(num)
        var = int((var - num)/10)
        exp *= 10
        counter += 1

    # De izquierda a derecha

    numero_A = valores[0]

    lista_corta_A = valores[1:]
    for i in range(len(lista_corta_A)):
        numero_A = int(str(numero_A) + str(lista_corta_A[i]))


    # Hasta este punto tenemos el numero al revez y el input
    if numero_A == input:
        return True
    if numero_A != input:
        return False

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    la idea es calcular x ^ n
    ==> Voy por sumas sucesivas

    """
    if n > mt.pow(2,31) - 1:
        print(n > mt.pow(2,31) - 1)
        print("Aca")
        return 0

    if n < -mt.pow(2,31):
        print("Aca**")
        return 0

    resultado = 1
    numero = x
    limite = n
    contador = 0
    flag = 0

    if limite < 0:
        limite = limite * (-1)
        flag = 1

    while contador < limite:
        resultado = resultado*numero
        contador += 1

    print("Contador",contador)

    if flag == 0:
        print("Pass")
        return resultado
    if flag == 1:
        print("Pass* neg")
        return 1/resultado

def reverse(x):

    var = x
    flag = 0

    if var < 0:
        var = var*(-1)
        flag = 1

    if int(var/10) == 0:
        if flag == 0:
            return var
        if flag == 1:
            return var*(-1)

    exp = 1
    counter = 0
    valores = []

    while var != 0:
        num = var%10
        valores.append(num)
        var = int((var - num)/10)
        exp *= 10
        counter += 1

    # hasta aca tenemos una lista con todos los numeros

    num_reverse = valores[0]
    lista_corta_A = valores[1:]

    for i in range(len(lista_corta_A)):
        num_reverse = int(str(num_reverse) + str(lista_corta_A[i]))
    print(num_reverse)

    if num_reverse > mt.pow(2,31) - 1:
        return 0

    if num_reverse < (-1)*mt.pow(2,31):
        return 0

    if flag == 0:
        return num_reverse
    if flag == 1:
        return num_reverse* (-1)

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    lista = nums
    flag = 0

    for i in range(len(lista)):
        if lista[i] == target:
            flag = 1
            return i

    if flag == 0:
        for i in range(len(lista)):
            print("target",target)
            print("Numero",i)

            if target <= lista[i]:
                print("***Pass***")
                return i
            if i == len(lista):
                print("Pass*")
                return len(lista)

def maxArea(self, height):

    """
    Container with Most water
    :param self:
    :param height:
    :return: Max area
    """

    distancia = []
    test = height

    print(len(test))

    if len(test) < 2 or len(test) > 10 ** 5:
        return 0

    for barrera in range(len(test)):
        value = max([min([test[barrera], test[k]]) * abs(barrera - k) for k in range(len(test)) if barrera != k])
        distancia.append(value)

    a_max = max(distancia)

    return a_max
