# faça um programa em Python que aba e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init() #iniciei o uso da biblioteca do pygame
pygame.mixer.music.load('nomedoaquivo.mp3') # não tenho nenhum mp3 baixado
pygame.mixer.music.play()
pygame.event.wait()
