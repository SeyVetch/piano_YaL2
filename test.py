import pygame.midi
import time
import random

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(1)

def keyPressEvent(self, event):
        if event.key() == Qt.Key_a:
                z=random.randint(64)
                player.note_on(64, 127)
                time.sleep(0.3)
        player.note_off(64, 127)
        time.sleep(0.1)
        if event.key() == Qt.Key_a:
                z=random.randint(65)
                player.note_on(65, 127)
                time.sleep(0.3)
        player.note_off(65, 127)
        time.sleep(0.1)
        
        
