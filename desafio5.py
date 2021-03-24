#dadas 2 cadenas de caracteres imprime la que mas caracteres tiene

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if len(cadena1) > len(cadena2):
    print(cadena1)
elif len(cadena1) < len(cadena2):
    print(cadena2)
else:
    print("Son de igual longitud")

