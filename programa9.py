# Solicitar tres números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Crear una lista con los números
numeros = [num1, num2, num3]

# Ordenar la lista de mayor a menor
numeros.sort(reverse=True)

# Mostrar los números ordenados
print("Números ordenados de mayor a menor:", numeros)
