import pygame
import Chopsticks_Screens as screens
from pygame import mixer

# initializing the constructor
pygame.init()
mixer.init()

# Title and Icon
pygame.display.set_caption("Chopsticks")
icon = pygame.image.load('Graphics/Chopsticks_Icon.png')
pygame.display.set_icon(icon)
mixer.music.load("Sounds/Background_Music.mp3")
mixer.music.set_volume(.25)
mixer.music.play(-1)

# Render Splash Screen
screens.splashScreen()

# Render Title Screen
screens.titleScreen()