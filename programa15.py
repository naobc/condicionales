# Solicitar la opción de cada jugador
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Definir las opciones válidas
opciones_validas = ["piedra", "papel", "tijera"]

# Verificar que ambas opciones sean válidas
if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Opción incorrecta")
else:
    # Determinar el resultado del juego
    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "tijera" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra"):
        print("Gana Jugador 1")
    else:
        print("Gana Jugador 2")
