# Pedir dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Verificar si el divisor es cero
if num2 != 0:
    division = num1 / num2
    print("El resultado de la división es:", division)
else:
    print("Error: No se puede dividir entre cero.")
