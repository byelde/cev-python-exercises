import pygame
import emoji
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
print(emoji.emojize('I wanna a churrasco, boy :sad_but_relieved_face:'))