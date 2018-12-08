import keyboard
import pygame.midi 
import time 
import random 

pygame.midi.init() 
player = pygame.midi.Output(0) 
player.set_instrument(1) 

while True:
    try:
        if keyboard.is_pressed('q'):#if key 'q' is pressed 
            z=random.randint(0, 64) 
            player.note_on(z, 127) 
            time.sleep(0.3) 
            player.note_off(z, 127) 
            time.sleep(0.1) 
        elif keyboard.is_pressed('w'):
            z=random.randint(64, 108)
            player.note_on(z, 127) 
            time.sleep(0.3) 
            player.note_off(z, 127) 
            time.sleep(0.1)
        elif keyboard.is_pressed('a'):
            break
        else:
            pass
    except:
        pass 
        