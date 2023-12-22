from random import randint, random, choice

import pygame as pg
import win32api
import win32con
import win32gui


def make_glass(background):
    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*background), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def main():

    x = 0.0
    y = 0.0

    random = randint(0,1)

    w, h = pg.display.Info().current_w, pg.display.Info().current_h # //2 dopo current_w/h
    screen = pg.display.set_mode((w, h))    # Altezza schermo

    keys = pg.key.get_pressed()

    pg.display.set_caption("Alessio's program") # Settiamo il titolo della nostra finestra

    background = (255, 255, 255)    # Settiamo il colore dello sfondo (R, G, B)

    make_glass(background)  # Funzione che rende lo sfondo trasparente

    snow1 = pg.transform.scale_by(pg.image.load('snowflake1.svg'), 0.1) # Importiamo il primo fiocco di neve
    snow2 = pg.transform.scale_by(pg.image.load('snowflake2.svg'), 0.1) # Importiamo il primo fiocco di neve

    snowflakes = [{'x': randint(0, w), 'y': randint(0, h)} for _ in range(100)] # Creiamo l' array per i fiocchi di neve

    if random == 0:
        pg.mixer.music.load('Christmas_music2004.ogg')  # Importiamo la musica di natale
        pg.mixer.music.play(-1) # Avvia la riproduzione del brano
    else:
        pg.mixer.music.load('We_Wish_You_a_Merry_Christmas.ogg')  # Importiamo la musica di natale
        pg.mixer.music.play(-1) # Avvia la riproduzione del brano     

    random = randint(0,1)
  

    
    while True:
        
        y = y + 1

        if y == h:
            y = 0.0
        
        screen.fill(background) # Diciamo al programma che vogliamo sovrascrivere il colore       
        screen.blit(snow1, (x , y)) # Diciamo al programma che vogliamo visualizzare il fiocco
            
        # pg.display.flip()
        if random == 0:
            for snowflake in snowflakes:    # Diciamo al programma che vogliamo visualizzare i fiocchi (100 in posizione random)
                screen.blit(snow1, (snowflake['x'], snowflake['y'] + y))
        else:
            for snowflake in snowflakes:    # Diciamo al programma che vogliamo visualizzare i fiocchi (100 in posizione random)
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
