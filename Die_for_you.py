import time
import os
import pygame

pygame.mixer.init()
try:
    pygame.mixer.music.load("Die_for_you.mp3")
except pygame.error:
    print('No se encontró el archivo. Por favor cargar la canción.')

karaoke_data = [
    (171760, "And if the sun grows cold for you along the way"),
    (178170, "And if the stars don't line to light the way"),
    (184550, "And when you fall away and crash back down below"),
    (191040, "I'll search the skies for you and I'll follow"),
    (196450, "I'll be in your afterglow"),
    (200390, "And I'll bring you home")
]

def limpiar_pantalla():
    print("\033[H\033[J", end="")

def centrar_texto(texto):
    tamaño_terminal = os.get_terminal_size().columns
    padding = (tamaño_terminal - len(texto)) // 2
    print("\033[1;35m", end="")
    print(" " * padding, end="", flush=True)

    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(0.1) 
    print("\033[0m")

tiempo_inicio_segundos = 171.0
limpiar_pantalla()
print("\033[1m")
print("¡Preparando...!".center(50))
print("\033[0m")
time.sleep(1.5)

pygame.mixer.music.play(start= tiempo_inicio_segundos)
indice_verso = 0

while indice_verso < len(karaoke_data):
    tiempo_en_ms = (tiempo_inicio_segundos * 1000) + pygame.mixer.music.get_pos()
    tiempo_objetivo, verso = karaoke_data[indice_verso]

    if tiempo_en_ms >= tiempo_objetivo:
        limpiar_pantalla()
        centrar_texto(verso)
        indice_verso += 1
    else:
        time.sleep(0.5)

while pygame.mixer.music.get_busy():
    time.sleep(1.5)
    limpiar_pantalla()
    print("\033[1m")
    print("Gracias por ver 🤠".center(os.get_terminal_size().columns))