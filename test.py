import keyboard
import pygame.midi 
import time 
import random 

pygame.midi.init() 
player = pygame.midi.Output(0) 
player.set_instrument(1) 

octave = 1
flag = dict()
for i in 'qwertyuiop[]':
    flag[i] = False
note = 'qwertyuiop[]'
octaves = 'zxcvbnm'

while True:
    try: 
        for i in range(7):
            if keyboard.is_pressed(octaves[i]):
                octave = i + 1
        for i in range(12):
            if keyboard.is_pressed(note[i]) and not flag[note[i]]:
                player.note_on(octave*12 + 24 + i, 127) 
                flag[note[i]] = True
        if keyboard.is_pressed('s'):
            z=random.randint(24, 106)
            player.note_on(z, 127) 
            time.sleep(0.3) 
            player.note_off(z, 127) 
            time.sleep(0.1)
        elif keyboard.is_pressed('a'):
            break
        else:
            pass
        for i in range(12):
            if not keyboard.is_pressed(note[i]):
                player.note_off(octave*12 + 24 + i, 127) 
                flag[note[i]] = False
    except:
        pass 
        