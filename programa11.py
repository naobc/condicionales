# Solicitar los datos de la llamada
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana (ejemplo: lunes, domingo): ").lower()
turno = input("Introduce el turno (mañana/tarde): ").lower() if dia != "domingo" else None

# Calcular el costo básico de la llamada según la duración
if duracion <= 5:
    costo_llamada = duracion * 1
elif duracion <= 8:
    costo_llamada = 5 * 1 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo_llamada = 5 * 1 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo_llamada = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

# Calcular el impuesto según el día y el turno
if dia == "domingo":
    impuesto = costo_llamada * 0.03
elif turno == "mañana":
    impuesto = costo_llamada * 0.15
else:  # turno de tarde
    impuesto = costo_llamada * 0.10

# Calcular el costo total
total_pagar = costo_llamada + impuesto

# Mostrar los resultados
print("Costo de la llamada sin impuestos:", round(costo_llamada, 2), "euros")
print("Impuesto aplicado:", round(impuesto, 2), "euros")
print("Total a pagar:", round(total_pagar, 2), "euros")
