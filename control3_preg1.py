"""
Crear un programa en Python que implemente una función
“digitos(num)”, que devuelva la cantidad de dígitos que tiene
un número ingresado por el usuario. Se recomienda procesar el
número como un String.

"""

def digitos(num):
    cantidad=0
    for digito in num:
        if digito in num:
            cantidad+=1
    return cantidad

#programa principal

numero=input("Ingresa un número por favor: ")
print(f"hay {digitos(numero)} de digitos en el numero {numero}")


        