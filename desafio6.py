# imprime la cant de letras "a" que tiene una cadena de caracteres ingresada por teclado
cadena = input("Ingrese una cadena: ")
cant = 0

for letra in cadena:
    if letra == "a":
        cant = cant + 1
print (cant)