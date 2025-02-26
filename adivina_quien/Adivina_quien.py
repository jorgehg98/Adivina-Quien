import random
import time

def imprimir_con_retraso(mensaje, retraso=0.5):
    """Imprime un mensaje con un retraso para mejorar la experiencia."""
    time.sleep(retraso)
    print(mensaje)

def juego_adivina_quien():
    intentos = 0
    numero_secreto = random.randint(1, 100)

    print("\033[1;34m¡Bienvenido al juego de Adivina Quién!\033[0m")
    nombre = input("\033[1;33mDime tu nombre: \033[0m")
    
    imprimir_con_retraso(f"\n\033[1;36mHola {nombre}, he pensado un número entre 1 y 100.\033[0m")
    imprimir_con_retraso("Tienes 8 intentos para adivinarlo. ¡Buena suerte!\n")

    while intentos < 8:
        try:
            estimado = int(input("\033[1;32m¿Cuál es el número?: \033[0m"))
            if estimado not in range(1, 101):
                print("\033[1;31m⚠️ El número no está en el rango. Intenta de nuevo.\033[0m")
                continue
        except ValueError:
            print("\033[1;31m⚠️ Entrada inválida. Ingresa un número entre 1 y 100.\033[0m")
            continue

        intentos += 1

        if estimado < numero_secreto:
            imprimir_con_retraso("\033[1;35m🔼 Mi número es más alto.\033[0m")
        elif estimado > numero_secreto:
            imprimir_con_retraso("\033[1;34m🔽 Mi número es más bajo.\033[0m")
        else:
            imprimir_con_retraso(f"\n\033[1;32m🎉 ¡Felicitaciones {nombre}! Adivinaste en {intentos} intentos. 🎉\033[0m")
            break

    if estimado != numero_secreto:
        imprimir_con_retraso(f"\n\033[1;31m😞 Se agotaron los intentos. El número secreto era {numero_secreto}.\033[0m")

if __name__ == "__main__":
    juego_adivina_quien()
