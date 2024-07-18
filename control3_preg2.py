"""
Crear un programa en Python que implemente una función
“es_binario(var)”, que permita determinar si un string está
compuesto por una expresión binaria o no, es decir, que
contenga solo unos y ceros. La función debe devolver un True,
si es que es una expresión binaria, o un False, en caso
contrario. NO DEBE UTILIZAR FUNCIONES PREDEFINIDAS DE PYTHON O
LIBRERÍAS para determinar si es binario.

"""
def es_binario(var):
    binario = "0 1"
    for caracteres in var:
        if caracteres in binario:
            return True
        else:
            return False
        
#Programa principal

expresion=input("Ingresa una expresión: ")
print(f"La expresión es {es_binario(expresion)}")
