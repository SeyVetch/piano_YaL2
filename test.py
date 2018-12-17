import keyboard
import pygame.midi 
import time 
import random 

pygame.midi.init() 
player = pygame.midi.Output(0) 
player.set_instrument(1) 

octave = 1
flag = dict()
note = 'qwertyuiop[]'
for i in note:
    flag[i] = False
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
            player.note_on(62, 127) 
            time.sleep(0.1) 
            player.note_off(62, 127) 
            time.sleep(0.01)
            player.note_on(62, 127) 
            time.sleep(0.1) 
            player.note_off(62, 127) 
            time.sleep(0.11)
            player.note_on(74, 127) 
            time.sleep(0.1) 
            player.note_off(74, 127) 
            time.sleep(0.22)
            player.note_on(67, 127) 
            time.sleep(0.1) 
            player.note_off(67, 127) 
            time.sleep(0.11)
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
        