# Pedir una cadena al usuario
cadena = input("Ingresa una cadena: ")

# Comprobar si es una única letra mayúscula
if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print("Es una letra mayúscula")
else:
    print("No es una letra mayúscula")
