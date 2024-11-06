# Solicitar el número del mes
mes = int(input("Introduce un número entre 1 y 12 para el mes: "))

# Diccionario que asocia cada número de mes con su cantidad de días
dias_por_mes = {
    1: 31,   # Enero
    2: 28,   # Febrero (sin considerar años bisiestos)
    3: 31,   # Marzo
    4: 30,   # Abril
    5: 31,   # Mayo
    6: 30,   # Junio
    7: 31,   # Julio
    8: 31,   # Agosto
    9: 30,   # Septiembre
    10: 31,  # Octubre
    11: 30,  # Noviembre
    12: 31   # Diciembre
}

# Verificar si el número es válido y mostrar el número de días
if 1 <= mes <= 12:
    print("El mes tiene:", dias_por_mes[mes], "días.")
else:
    print("ERROR: número incorrecto.")
