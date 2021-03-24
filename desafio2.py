#comprueba si un num ingresado por teclado es multiplo de 2 , 3 o 5
num = int ( input("Ingrese un numero entero: "))

if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print("Es multiplo de 2 y de 3 y de 5")
elif num % 2 == 0 and num % 3 == 0:
    print("Es multiplo de 2 y de 3")
elif num % 3 == 0 and num % 5 == 0:
    print("Es multiplo de 3 y de 5")
elif num % 2 == 0 and num % 5 == 0:
    print("Es multiplo de 2 y de 5")
elif num % 2 == 0:
    print("Es multiplo de 2")
elif num % 3 == 0:
    print("Es multiplo de 3")
elif num % 5 == 0:
    print("Es multiplo de 5")
else:
    print("No es multiplo de 2, 3 ni 5")