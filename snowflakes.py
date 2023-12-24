from random import randint, random, choice

import pygame as pg
import win32api
import win32con
import win32gui


def make_glass(background): # Funzione che permette di avere lo sfondo trasparente
    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*background), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def main():

    w, h = pg.display.Info().current_w, pg.display.Info().current_h # Assegna la misura dello schermo a w, h
    flags = pg.NOFRAME | pg.SCALED | pg.FULLSCREEN | pg.HWSURFACE | pg.DOUBLEBUF
    mode = pg.display.mode_ok((w, h), flags, 32)
    screen = pg.display.set_mode((w, h), flags, mode)   # Imposta i valori dello schermo nella schermata


    pg.display.set_caption("Snowflakes") # Settiamo il titolo della nostra finestra


    background = (255, 255, 255)    # Settiamo il colore dello sfondo (R, G, B)
    

    snow1 = pg.transform.scale_by(pg.image.load('snowflake1.svg'), 0.1) # Importiamo il primo fiocco di neve
    snow2 = pg.transform.scale_by(pg.image.load('snowflake2.svg'), 0.08) # Importiamo il secondo fiocco di neve


    make_glass(background)  # Richiamiamo la funzione per lo sfondo trasparente

    

    snowflakes = [{'x': randint(0, w),  # Valore casuale asse delle x
                   'y': randint(0, h),  # Valore casuale asse delle y
                   'v': 0.5 + random(), # Velocita casuale del fiocco di neve
                   'f': choice([snow1, snow2])} # Scelta casuale del fiocco di neve
                   for _ in range(50)] # Creiamo l' array che contiene 50 singoli fiocchi di neve


    clock = pg.time.Clock() # Temporizzatore per ottenere un numero di FPS

    if randint(0,1) == 0:
        pg.mixer.music.load('Christmas_music2004.ogg')  # Importiamo la prima musica di natale
        pg.mixer.music.play(-1) # Avvia la riproduzione del primo brano
    else:
        pg.mixer.music.load('We_Wish_You_a_Merry_Christmas.ogg')  # Importiamo la Seconda musica di natale
        pg.mixer.music.play(-1) # Avvia la riproduzione del secondo brano

   
   
    while True: # Ciclo dove avviene il programma
        
        screen.fill(background) # Diciamo al programma che vogliamo sovrascrivere il colore  


        if random() < 0.1:  # Numero casuale di fiocchi che scenderà nuovamente
            flake = choice([snow1, snow2])
            snowflakes.append({'x': randint(0, w),
            'y': -flake.get_height(),
            'v': 0.5 + random(),
            'f': flake})


        snowflakes = [flake for flake in snowflakes if flake['y'] < h]  # Gestione eliminazione fiocchi una  volta arrivati a fondo schermo


        for flake in snowflakes:
            flake['x'] += random() * 0.5 - 0.25 # Assegnata la velocità dell'asse x al signolo fiocco
            flake['y'] += flake['v']    # Assegnata la velocità dell'asse y al singolo fiocco
            screen.blit(flake['f'], (flake['x'], flake['y']))   # Creazione singolo fiocco di neve
        

        pg.display.flip()   # Al posto dell'istruzione update (uso ottimale GPU)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
        

        clock.tick(60)  # Controllo vero e proprio


if __name__ == '__main__':
    pg.init()
    try:
        main()
    except KeyboardInterrupt:
        pass
    pg.quit()
