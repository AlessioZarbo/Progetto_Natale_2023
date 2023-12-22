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

    x = 0.0
    y = 0.0

    random = randint(0,1)   # Variabile che gestisce gli eventi casuali

    w, h = pg.display.Info().current_w, pg.display.Info().current_h # Variabili che prendono le misure dello schermo
    screen = pg.display.set_mode((w, h))    # Impostata la grandezza dello schermo

    pg.display.set_caption("Alessio's program") # Settiamo il titolo della nostra finestra

    background = (255, 255, 255)    # Settiamo il colore dello sfondo (R, G, B)

    make_glass(background)  # Richiamiamo la funzione per lo sfondo trasparente

    snow1 = pg.transform.scale_by(pg.image.load('snowflake1.svg'), 0.1) # Importiamo il primo fiocco di neve
    snow2 = pg.transform.scale_by(pg.image.load('snowflake2.svg'), 0.1) # Importiamo il secondo fiocco di neve

    snowflakes = [{'x': randint(0, w), 'y': randint(0, h)} for _ in range(100)] # Creiamo l' array che contiene 100 posizioni casuali (x, y)

    if random == 0:
        pg.mixer.music.load('Christmas_music2004.ogg')  # Importiamo la prima musica di natale
        pg.mixer.music.play(-1) # Avvia la riproduzione del primo brano
    else:
        pg.mixer.music.load('We_Wish_You_a_Merry_Christmas.ogg')  # Importiamo la seconda musica di natale
        pg.mixer.music.play(-1) # Avvia la riproduzione del secondo brano     

    random = randint(0,1)
   
    while True: # Ciclo dove avviene il programma
        
        y = y + 1   # Variabile y che incrementa ogni ciclo permettendo di far muovere l'immagine

        if y == h:  # Se y raggiunge il valore massimo si riazzeraq
            y = 0.0
        
        screen.fill(background) # Diciamo al programma che vogliamo sovrascrivere il colore  
             
        # screen.blit(snow1, (x , y)) # Diciamo al programma che vogliamo visualizzare il fiocco
            
        # pg.display.flip()
        if random == 0:
            for snowflake in snowflakes:    # Per ogni posizione x, y random (100 posizioni totali), la associ al fiocco di neve 1
                screen.blit(snow1, (snowflake['x'], snowflake['y'] + y))
        else:
            for snowflake in snowflakes:     # Per ogni posizione x, y random (100 posizioni totali), la associ al fiocco di neve 2
                screen.blit(snow2, (snowflake['x'], snowflake['y'] + y))


        pg.display.update() # Diciamo al programma che deve aggiornare

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return


if __name__ == '__main__':
    pg.init()
    try:
        main()
    except KeyboardInterrupt:
        pass
    pg.quit()
