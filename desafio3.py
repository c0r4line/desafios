# devuelve si una letra ingresada por teclado es mayuscula o minuscula
letra = input("Ingrese una letra: ")

if letra >="a" and letra <="z":
    print("Es minuscula")
elif letra >="A" and letra <="Z":
    print("Es mayuscula")
else:
    print("No es una letra")