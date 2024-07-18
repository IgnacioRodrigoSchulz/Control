"""
Crear una función recursiva llamada “potencia(num, exp)”, que
reciba un número (num) y un exponente (exp), y calcule su
potencia en base al exponente. NO DEBE UTILIZAR FUNCIONES
PREDEFINIDAS DE PYTHON O LIBRERÍAS para calcular la potencia.

"""
def potencia(num, exp):
    global numero
    if exp>1:
        print(num,"x",numero,"=",numero*num)
        potencia(num*num,exp-1)

#programa principal

numero = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
potencia(numero,exponente)