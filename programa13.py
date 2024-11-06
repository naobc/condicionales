# Solicitar el número del día de la semana
dia = int(input("Introduce un número del 1 al 7 para el día de la semana: "))

# Diccionario que asocia cada número con el día de la semana
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Verificar si el número es válido y mostrar el día correspondiente
if 1 <= dia <= 7:
    print("El día correspondiente es:", dias_semana[dia])
else:
    print("ERROR: número incorrecto.")
