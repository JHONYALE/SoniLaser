# Código explicado sobre la interacción con otras interfaces

# Importar los módulos necesarios
from machine import Pin, PWM
from utime import sleep

# Inicializar PWM (Modulación de Ancho de Pulso) para el zumbador en el pin 22
buzzer = PWM(Pin(22))

# Diccionario que asigna nombres de notas musicales a sus frecuencias correspondientes
tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

# Definir una canción utilizando nombres de notas y silencios ("P" para pausa)
cancion = ["C3", "G3", "C3", "G3", "C3", "G3", "C3", "G3", "AS2", "G3", "AS2", "G3", "AS2", "G3", "AS2", "G3", "A2", "F2", "A2", "F2", "A2", "F2", "F2", "F2",
           "G3", "P", "G3", "G3", "C3", "C3", "G3", "D3", "P", "D3", "P", "D3", "D3", "C3", "F4", "P", "F4", "P", "F4", "P", "D3", "C3", "D3", "D3",
           "F4", "D3", "G4", "D3", "F4", "D3", "P", "D3", "F4", "D3", "G4", "F4", "D3"]

# Función para reproducir un tono único con una frecuencia dada
def reproducir_tono(frecuencia):
    buzzer.duty_u16(3000)  # Establecer el ciclo de trabajo (volumen)
    buzzer.freq(frecuencia)  # Establecer la frecuencia del tono

# Función para detener el zumbador (silencio)
def estar_en_silencio():
    buzzer.duty_u16(0)

# Función para reproducir una secuencia de tonos basada en una canción dada
def reproducir_cancion(micancion):
    while True:  # Repetir indefinidamente
        for i in range(len(micancion)):
            print(micancion[i])  # Imprimir la nota o el silencio actual
            if (micancion[i] == "P"):
                estar_en_silencio()  # Si es un silencio, silenciar el zumbador
            else:
                reproducir_tono(tones[micancion[i]])  # Si es una nota, reproducir el tono correspondiente
            sleep(0.23)  # Pausa entre notas
        estar_en_silencio()  # Silenciar el zumbador al final de la canción

# Llamar a la función reproducir_cancion con la canción definida
reproducir_cancion(cancion)
