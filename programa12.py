# Solicitar el número del dado
numero = int(input("Introduce el resultado del dado (1-6): "))

# Diccionario que asocia cada número con su cara opuesta en letras
caras_opuestas = {
    1: "seis",
    2: "cinco",
    3: "cuatro",
    4: "tres",
    5: "dos",
    6: "uno"
}

# Verificar si el número es válido y mostrar el resultado
if 1 <= numero <= 6:
    print("La cara opuesta es:", caras_opuestas[numero])
else:
    print("ERROR: número incorrecto.")
