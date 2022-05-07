import math
import pygame, sys, time
import Chopsticks_Constants as constants
from pygame.constants import MOUSEBUTTONDOWN
import Chopsticks_Gameplay as game

pygame.init()

def updateGameScreen():
    left_1 = constants.NUMBERS_FONT.render(str(constants.L1), True, constants.BLACK)
    right_1 = constants.NUMBERS_FONT.render(str(constants.R1), True, constants.BLACK)
    left_2 = constants.NUMBERS_FONT.render(str(constants.L2), True, constants.BLACK)
    right_2 = constants.NUMBERS_FONT.render(str(constants.R2), True, constants.BLACK)

    # screen borders
    constants.SCREEN.fill(constants.BACKGROUND)
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [0, constants.HEIGHT/2-35, constants.WIDTH, 1])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [0, constants.HEIGHT/2+35, constants.WIDTH, 1])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2, constants.P1_NAME.get_height() + 5, 1, constants.HEIGHT/2-35-constants.P1_NAME.get_height()-5])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2, constants.HEIGHT/2+35, 1, constants.HEIGHT/2-35 - constants.P2_NAME.get_height() - 5])

    # box holding player 1's name
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2 - constants.P1_NAME.get_width()/2 - 5, constants.P1_NAME.get_height()+5, constants.P1_NAME.get_width() + 10, 1])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2 - constants.P1_NAME.get_width()/2 - 5, 0, 1, constants.P1_NAME.get_height() + 5])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2 + constants.P1_NAME.get_width()/2 + 5, 0, 1, constants.P1_NAME.get_height() + 5])

    # box holding player 2's name
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2 - constants.P2_NAME.get_width()/2 - 5, constants.HEIGHT - constants.P2_NAME.get_height() - 5, constants.P2_NAME.get_width() + 10, 1])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2 - constants.P2_NAME.get_width()/2 - 5, constants.HEIGHT - constants.P2_NAME.get_height() - 5, 1, constants.P2_NAME.get_height() + 5])
    pygame.draw.rect(constants.SCREEN, constants.BLACK, [constants.WIDTH/2 + constants.P2_NAME.get_width()/2 + 5, constants.HEIGHT - constants.P2_NAME.get_height() - 5, 1, constants.P2_NAME.get_height() + 5])

    # puts numbers and name on the screen
    constants.SCREEN.blit(constants.P1_NAME, (constants.WIDTH/2 - constants.P1_NAME.get_rect().width/2, 0))
    constants.SCREEN.blit(constants.P2_NAME, (constants.WIDTH/2 - constants.P2_NAME.get_rect().width/2, constants.HEIGHT - constants.P2_NAME.get_rect().height - 5))
    constants.SCREEN.blit(left_1, ((constants.WIDTH/2 - left_1.get_width())/2, (constants.HEIGHT/2 - 35 - left_1.get_height())/2))
    constants.SCREEN.blit(right_1, (constants.WIDTH/2 + (constants.WIDTH/2 - right_1.get_width())/2, (constants.HEIGHT/2 - 35 - right_1.get_height())/2))
    constants.SCREEN.blit(left_2, ((constants.WIDTH/2 - left_2.get_width())/2, constants.HEIGHT/2 + (constants.HEIGHT/2 + 35 - left_2.get_height())/2))
    constants.SCREEN.blit(right_2, (constants.WIDTH/2 + (constants.WIDTH/2 - right_2.get_width())/2, constants.HEIGHT/2 + (constants.HEIGHT/2 + 35 - right_2.get_height())/2))

def splashScreen():
    # splash screen stuff
    splashScreenTimer = 0
    last_time = time.time()

    while splashScreenTimer < 0: # change back to 100 when done
        dt = time.time() - last_time
        dt *= constants.framerate
        last_time = time.time()

        splashScreenTimer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        constants.SCREEN.fill(constants.BACKGROUND)
        constants.SCREEN.blit(constants.SS_TEXT, ((constants.SCREEN.get_width()/2 - constants.SS_TEXT.get_width()/2, constants.HEIGHT/2 - constants.SS_TEXT.get_height()/2)))

        pygame.display.update()
        pygame.time.delay(10)

# figure out how to end title and open this without starting game
def rulesScreen():
    rulesScreen = True
    constants.SCREEN.fill(constants.BACKGROUND)

    # Adds text to rules page
    spacing = 10
    constants.SCREEN.blit(constants.LOGO, (10, spacing))
    constants.SCREEN.blit(constants.LOGO, (constants.WIDTH - 10 - constants.LOGO.get_width(), spacing))
    constants.SCREEN.blit(constants.RULES_TITLE, (constants.WIDTH/2 - constants.RULES_TITLE.get_width()/2, spacing))
    spacing += constants.RULES_TITLE.get_height() + 10

    pygame.draw.circle(constants.SCREEN, constants.BLACK, (10, spacing + constants.RULES_LINE1.get_height()/2), 3)
    constants.SCREEN.blit(constants.RULES_LINE1, (20, spacing))
    spacing += constants.RULES_LINE1.get_height() + 10
    pygame.draw.circle(constants.SCREEN, constants.BLACK, (10, spacing + constants.RULES_LINE2.get_height()/2), 3)
    constants.SCREEN.blit(constants.RULES_LINE2, (20, spacing))
    spacing += constants.RULES_LINE2.get_height() + 10
    constants.SCREEN.blit(constants.RULES_LINE2_2, (10, spacing))
    spacing += constants.RULES_LINE2_2.get_height() + 10
    pygame.draw.circle(constants.SCREEN, constants.BLACK, (10, spacing + constants.RULES_LINE3.get_height()/2), 3)
    constants.SCREEN.blit(constants.RULES_LINE3, (20, spacing))
    spacing += constants.RULES_LINE3.get_height() + 10
    pygame.draw.circle(constants.SCREEN, constants.BLACK, (10, spacing + constants.RULES_LINE4.get_height()/2), 3)
    constants.SCREEN.blit(constants.RULES_LINE4, (20, spacing))
    spacing += constants.RULES_LINE4.get_height() + 10
    constants.SCREEN.blit(constants.RULES_LINE4_2, (10, spacing))
    spacing += constants.RULES_LINE4_2.get_height() + 10
    constants.SCREEN.blit(constants.RULES_LINE4_3, (10, spacing))
    spacing += constants.RULES_LINE4_3.get_height() + 10
    pygame.draw.circle(constants.SCREEN, constants.BLACK, (10, spacing + constants.RULES_LINE5.get_height()/2), 3)
    constants.SCREEN.blit(constants.RULES_LINE5, (20, spacing))
    spacing += constants.RULES_LINE5.get_height() + 10
    pygame.draw.circle(constants.SCREEN, constants.BLACK, (10, spacing + constants.RULES_LINE6.get_height()/2), 3)
    constants.SCREEN.blit(constants.RULES_LINE6, (20, spacing))
    spacing += constants.RULES_LINE6.get_height()
    
    constants.SCREEN.blit(constants.LOGO, (10, spacing))
    constants.SCREEN.blit(constants.LOGO, (constants.WIDTH - 10 - constants.LOGO.get_width(), spacing))
    constants.SCREEN.blit(constants.HTP_TITLE, (constants.WIDTH/2 - constants.HTP_TITLE.get_width()/2, spacing))
    spacing += constants.HTP_TITLE.get_height()

    constants.SCREEN.blit(constants.HTP_LINE1, (10, spacing))
    spacing += constants.HTP_LINE1.get_height() + 10
    constants.SCREEN.blit(constants.HTP_LINE2, (10, spacing))
    spacing += constants.HTP_LINE2.get_height() + 10
    constants.SCREEN.blit(constants.HTP_LINE3, (10, spacing))
    spacing += constants.HTP_LINE3.get_height() + 10
    constants.SCREEN.blit(constants.HTP_LINE3_2, (10, spacing))
    spacing += constants.HTP_LINE3_2.get_height() + 10
    constants.SCREEN.blit(constants.HTP_LINE4, (10, spacing))

    # add loop to keep screen going
    while rulesScreen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == MOUSEBUTTONDOWN and constants.WIDTH-220 <= mouse[0] <= constants.WIDTH-10 and constants.HEIGHT-70 <= mouse[1] <= constants.HEIGHT-10:
                pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
                titleScreen()
            
        mouse = pygame.mouse.get_pos()
        if constants.WIDTH-220 <= mouse[0] <= constants.WIDTH-10 and constants.HEIGHT-70 <= mouse[1] <= constants.HEIGHT-10:
            constants.SCREEN.blit(constants.HOVER_BUTTON, (constants.WIDTH - 220, constants.HEIGHT - 70))
        else:
            constants.SCREEN.blit(constants.BUTTON, (constants.WIDTH - 220, constants.HEIGHT - 70))
        
        constants.SCREEN.blit(constants.BACK, (constants.WIDTH - constants.BUTTON.get_width() + (constants.BUTTON.get_width() - constants.BACK.get_width()) / 2 - 5, constants.HEIGHT - constants.BUTTON.get_height() - (constants.BUTTON.get_height() - constants.BACK.get_height()) / 2 - 5))
        
        pygame.display.update()
        pygame.time.delay(10)

    return False

def titleScreen():
    # title screen stuff
    titleScreen = True
    last_time = time.time()

    while titleScreen:
        dt = time.time() - last_time
        dt *= constants.FRAMERATE
        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        if (clicked and  constants.WIDTH/2-70 <= mouse[0] <= constants.WIDTH/2+70 and constants.HEIGHT/2-20 <= mouse[1] <= constants.HEIGHT/2+20):
            titleScreen = False
            clicked = False
            pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
            game.startGame()

        if (clicked and  constants.WIDTH-220 <= mouse[0] <= constants.WIDTH-10 and constants.HEIGHT-70 <= mouse[1] <= constants.HEIGHT-10):
            pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
            rulesScreen()
            

        if (clicked and  10 <= mouse[0] <= 220 and constants.HEIGHT-70 <= mouse[1] <= constants.HEIGHT-10):
            pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
            pygame.quit()
            sys.exit()
        
        # Background and Logo
        constants.SCREEN.fill(constants.BACKGROUND)
        constants.SCREEN.blit(constants.BACKGROUND_LOGO, (constants.WIDTH / 2 - constants.BACKGROUND_LOGO.get_width() / 2, constants.HEIGHT / 4 + 5 + math.sin(time.time()* 5) * 5 - 25 - (constants.BACKGROUND_LOGO.get_height() - constants.TITLE.get_height()) / 2))

        # title
        constants.SCREEN.blit(constants.TITLE_SHADOW, (constants.WIDTH/2 - constants.TITLE.get_width()/2, constants.HEIGHT/4 + 5 + math.sin(time.time()* 5) * 5 - 25))
        constants.SCREEN.blit(constants.TITLE, (constants.WIDTH/2 - constants.TITLE.get_width()/2, constants.HEIGHT/4 + math.sin(time.time() * 5) * 5 - 25))

        # play button and text
        if constants.WIDTH/2-105 <= mouse[0] <= constants.WIDTH/2+105 and constants.HEIGHT/2-30 <= mouse[1] <= constants.HEIGHT/2+30:
            
            constants.SCREEN.blit(constants.HOVER_BUTTON, (constants.WIDTH/2-105, constants.HEIGHT/2 - 30))
        else:
            constants.SCREEN.blit(constants.BUTTON, (constants.WIDTH/2-105, constants.HEIGHT/2 - 30))

        constants.SCREEN.blit(constants.PLAY, (constants.WIDTH/2-43.5, constants.HEIGHT/2 - 28.5))

        # rules button and text
        if constants.WIDTH-220 <= mouse[0] <= constants.WIDTH-10 and constants.HEIGHT-70 <= mouse[1] <= constants.HEIGHT-10:
            constants.SCREEN.blit(constants.HOVER_BUTTON, (constants.WIDTH - 220, constants.HEIGHT - 70))
        else:
            constants.SCREEN.blit(constants.BUTTON, (constants.WIDTH - 220, constants.HEIGHT - 70)) 

        constants.SCREEN.blit(constants.RULES, (constants.WIDTH - 175.5, constants.HEIGHT - 68.5))

        # quit button and text
        if 10 <= mouse[0] <= 220 and constants.HEIGHT-70 <= mouse[1] <= constants.HEIGHT-10:
            constants.SCREEN.blit(constants.HOVER_BUTTON, (10, constants.HEIGHT - 70)) 
        else:
            constants.SCREEN.blit(constants.BUTTON, (10, constants.HEIGHT - 70)) 

        # another way to center text on the button
        constants.SCREEN.blit(constants.QUIT, (10 + (constants.BUTTON.get_width() - constants.QUIT.get_width()) / 2, (constants.HEIGHT - 70) + (constants.BUTTON.get_height() - constants.QUIT.get_height()) / 2))

        pygame.display.update()
        pygame.time.delay(10)
    
    return True