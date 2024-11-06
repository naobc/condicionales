# Solicitar el número de alumnos
num_alumnos = int(input("Introduce el número de alumnos que irán al viaje: "))

# Calcular el costo por alumno y el costo total
if num_alumnos >= 100:
    costo_por_alumno = 65
    total_a_pagar = num_alumnos * costo_por_alumno
elif 50 <= num_alumnos <= 99:
    costo_por_alumno = 70
    total_a_pagar = num_alumnos * costo_por_alumno
elif 30 <= num_alumnos <= 49:
    costo_por_alumno = 95
    total_a_pagar = num_alumnos * costo_por_alumno
else:
    # Si son menos de 30 alumnos, el costo total es de 4000 euros
    costo_por_alumno = 4000 / num_alumnos
    total_a_pagar = 4000

# Mostrar los resultados
print("El pago total a la compañía de autobuses es de:", total_a_pagar, "euros")
print("Cada alumno debe pagar:", costo_por_alumno, "euros")
