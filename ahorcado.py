import os
import time
import random

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-like
        os.system('clear')
#Funciones principales del juego
def victoria_derrota(vida):
    if vida > 0:
        clear_screen()
        print("""888     888 d8b          888                              
888     888 Y8P          888                              
888     888              888                              
Y88b   d88P 888  .d8888b 888888  .d88b.  888d888 888  888 
 Y88b d88P  888 d88P"    888    d88""88b 888P"   888  888 
  Y88o88P   888 888      888    888  888 888     888  888 
   Y888P    888 Y88b.    Y88b.  Y88..88P 888     Y88b 888 
    Y8P     888  "Y8888P  "Y888  "Y88P"  888      "Y88888 
                                                      888 
                                                 Y8b d88P 
                                                  "Y88P" """)
    else:
        clear_screen()
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")        
def pantalla_carga():
    
    print("""
 .d8888b.                            888                  888     888                   888b     d888                            
d88P  Y88b                           888                  888     888                   8888b   d8888                            
888    888                           888                  888     888                   88888b.d88888                            
888        888d888  .d88b.   8888b.  888888  .d88b.   .d88888     88888b.  888  888     888Y88888P888  8888b.  88888b.  888  888 
888        888P"   d8P  Y8b     "88b 888    d8P  Y8b d88" 888     888 "88b 888  888     888 Y888P 888     "88b 888 "88b 888  888 
888    888 888     88888888 .d888888 888    88888888 888  888     888  888 888  888     888  Y8P  888 .d888888 888  888 888  888 
Y88b  d88P 888     Y8b.     888  888 Y88b.  Y8b.     Y88b 888     888 d88P Y88b 888     888   "   888 888  888 888  888 Y88b 888 
 "Y8888P"  888      "Y8888  "Y888888  "Y888  "Y8888   "Y88888     88888P"   "Y88888     888       888 "Y888888 888  888  "Y88888 
                                                                                888                                              
                                                                           Y8b d88P                                              
                                                                            "Y88P"                                               """)
    time.sleep(2)
    print("Cargando...")
    clear_screen()
    print("""
           d8888 888                                              888          
          d88888 888                                              888          
         d88P888 888                                              888          
        d88P 888 88888b.   .d88b.  888d888  .d8888b  8888b.   .d88888  .d88b.  
       d88P  888 888 "88b d88""88b 888P"   d88P"        "88b d88" 888 d88""88b 
      d88P   888 888  888 888  888 888     888      .d888888 888  888 888  888 
     d8888888888 888  888 Y88..88P 888     Y88b.    888  888 Y88b 888 Y88..88P 
    d88P     888 888  888  "Y88P"  888      "Y8888P "Y888888  "Y88888  "Y88P" """)
    time.sleep(2)
    clear_screen()
def animacion(vida):      
    if vida == 5:
        print("""
                                        ________
                                       |/      |
                                       |       0
                                       |      
                                       |      
                                       |     
                                       |
                                      _|___""")
    elif vida == 4:
        print("""
                                        ________
                                       |/      |
                                       |       0
                                       |       |
                                       |      
                                       |     
                                       |
                                      _|___""")
    elif vida == 3:
        print("""
                                        ________
                                       |/      |
                                       |       0
                                       |      ||
                                       |      
                                       |     
                                       |
                                      _|___""")
    elif vida == 2:
        print("""
                                        ________
                                       |/      |
                                       |       0
                                       |      |||
                                       |      
                                       |     
                                       |
                                      _|___""")
    elif vida == 1:
        print("""
                                        ________
                                       |/      |
                                       |       0
                                       |      |||
                                       |      | 
                                       |     
                                       |
                                      _|___""")
    elif vida == 0:
        print("""
                                        ________
                                       |/      |
                                       |       0
                                       |      |||
                                       |      | |
                                       |     
                                       |
                                      _|___""")
def presentar():
    jugador = input("Seleccione el modo de juego, 1 jugador o 2 jugadores, 1/2: ")
    try:
        jugador = int(jugador)
    except:
        print("Opcion no valida, selecciones 1 o 2")
    while jugador != 1 and jugador != 2:
        jugador = input("Seleccione el modo de juego, 1 jugador o 2 jugadores, 1/2: ")
        try:
            jugador = int(jugador)
        except:
            print("Opcion no valida, selecciones 1 o 2")
    if jugador == 1:
        ahorcado_1p()
    elif jugador ==2:
        ahorcado2()
    else:
        print(":( Ah ocurrido un Error")
def seleccionar_dificultad():
    dificultades = (1,2,3)
    dificultad = input("Selecciones una dificultad 1/2/3: ")
    try: 
        dificultad = int(dificultad)
    except:
        print("Opcion no valida 1/2/3")
    while dificultad not in dificultades:
        dificultad = input("Selecciones una dificultad 1/2/3: ")
        try: 
            dificultad = int(dificultad)
        except:
            print("Opcion no valida 1/2/3")
    return dificultad

#Modos de juego
def ahorcado2():
    palabra = list(input("Ingrese una palabra: ").lower())
    time.sleep(0.5)
    clear_screen()
    longi = len(palabra)
    secreto = list(palabra[0]+("_"*(longi-1)))
    secretonuevo = "".join(secreto)
    print(secretonuevo)
    vidas = 6
    letras_no = []
    while vidas > 0:
        letra = input("Letra: ").lower()
        if letra in palabra:
            for indice, letras in enumerate(palabra):
                if letra == letras:
                    secreto[indice] = palabra[indice]
                    secretonuevo = "".join(secreto)
                    print(secretonuevo)
                else:
                    pass
            if "_" in secreto:
                continue
            else:
                victoria_derrota(vidas)
                break
        else:
            vidas -= 1
            animacion(vidas)
            letras_no.append(letra)
            print(f"Letras que no estan: {letras_no}")
            print(f"Perdiste una vida {vidas}")
        if vidas == 0:
            nueva = "".join(palabra)
            victoria_derrota(vidas)
            print(f"La palabra era: {nueva}")        
def ahorcado_1p():
    palabras_faciles = ["casa", "perro", "gato", "mesa", "sol", "libro", "rueda", "lápiz", "mano", "flor","luna"]
    palabras_intermedias = ["montaña", "escalera", "jardín", "avión", "escuela", "botella", "espejo", "ratón", "teléfono", "ventana","paredes"]
    palabras_dificiles = ["helicóptero", "astronauta", "bibliotecario", "murciélago", "travesura", "circunstancia", "desenlace", "felicidad", "crucigrama", "invernadero", "videojuego"]
    dificultad = seleccionar_dificultad()
    if dificultad == 1:
        palabra = random.choice(palabras_faciles)
    elif dificultad == 2:
        palabra = random.choice(palabras_intermedias)
    elif dificultad == 3:
        palabra = random.choice(palabras_dificiles)
    else:
        print(":( Ah ocurrido un Error")
    time.sleep(0.5)
    clear_screen()
    nueva = "".join(palabra)
    longi = len(palabra)
    secreto = list(palabra[0]+("_"*(longi-1)))
    secretonuevo = "".join(secreto)
    print(secretonuevo)
    vidas = 6
    letras_no = []
    while vidas > 0:
        letra = input("Letra: ").lower()
        if letra in palabra:
            for indice, letras in enumerate(palabra):
                if letra == letras:
                    secreto[indice] = palabra[indice]
                    secretonuevo = "".join(secreto)
                    print(secretonuevo)
                else:
                    pass
            if "_" in secreto:
                continue
            else:
                victoria_derrota(vidas)
                print(f"La palabra era: {nueva}")
                break
        else:
            vidas -= 1
            animacion(vidas)
            letras_no.append(letra)
            print(f"Letras que no estan: {letras_no}")
            print(f"Perdiste una vida {vidas}")
        if vidas == 0:
            victoria_derrota(vidas)
            print(f"La palabra era: {nueva}")

#Funcion principal para jugar
def jugar():
    pantalla_carga()
    presentar()        

#Bucle principal del juego
while True:
    jugador = input("Jugar/Salir: ").lower()
    if "jugar" in jugador or "juga" in jugador:
        jugar()
    elif "salir" in jugador or "sal" in jugador:
        break