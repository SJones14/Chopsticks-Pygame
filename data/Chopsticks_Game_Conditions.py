import pygame
import Chopsticks_Constants as constants
import Chopsticks_Screens as screens
from pygame.constants import MOUSEBUTTONDOWN

# check if there's a winner
def checkWinner():
    if constants.L1 == 0 and constants.R1 == 0:
        constants.SCREEN.blit(constants.P2_WINNER_MESSAGE, (constants.WIDTH/4 - constants.P2_WINNER_MESSAGE.get_rect().width/2, constants.HEIGHT/2 - constants.P2_WINNER_MESSAGE.get_rect().height/2))
        constants.SCREEN.blit(constants.PLAY_AGAIN_MESSAGE, (constants.WIDTH - constants.WIDTH/4 - constants.PLAY_AGAIN_MESSAGE.get_width()/2, constants.HEIGHT/2 - constants.PLAY_AGAIN_MESSAGE.get_height()/2))
        pygame.mixer.Sound.play(constants.WINNER_FX)
        
        # should allow for game to "restart"
        while True:
            mouse = pygame.mouse.get_pos()
            # "No" Button
            if constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.NO_TEXT, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.NO_TEXT.get_width()) / 2, constants.HEIGHT/2 + 45 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.NO_TEXT.get_height()) / 2))
            else:
                constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.NO_TEXT, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.NO_TEXT.get_width()) / 2, constants.HEIGHT/2 + 45 + (constants.SPLIT_BUTTON.get_height() - constants.NO_TEXT.get_height()) / 2))

            # "Yes" Button
            if constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.YES_TEXT, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.YES_TEXT.get_width()) / 2, constants.HEIGHT/2 + 45 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.YES_TEXT.get_height()) / 2))

            else:
                constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.YES_TEXT, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.YES_TEXT.get_width()) / 2, constants.HEIGHT / 2 + 45 + (constants.SPLIT_BUTTON.get_height() - constants.YES_TEXT.get_height()) / 2))


            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                    pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
                    screens.titleScreen()
                if event.type == MOUSEBUTTONDOWN and constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                    pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
                    constants.L1 = 1
                    constants.R1 = 1
                    constants.L2 = 1
                    constants.R2 = 1
                    screens.updateGameScreen()
                    return False

            pygame.display.update()
            pygame.time.delay(10)

    elif constants.L2 == 0 and constants.R2 == 0:
        constants.SCREEN.blit(constants.P1_WINNER_MESSAGE, (constants.WIDTH/4 - constants.P1_WINNER_MESSAGE.get_rect().width/2, constants.HEIGHT/2 - constants.P1_WINNER_MESSAGE.get_rect().height/2))
        constants.SCREEN.blit(constants.PLAY_AGAIN_MESSAGE, (constants.WIDTH - constants.WIDTH/4 - constants.PLAY_AGAIN_MESSAGE.get_width()/2, constants.HEIGHT/2 - constants.PLAY_AGAIN_MESSAGE.get_height()/2))
        pygame.mixer.Sound.play(constants.WINNER_FX)
        
        while True:
            mouse = pygame.mouse.get_pos()
            # "No" Button
            if constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.NO_TEXT, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.NO_TEXT.get_width()) / 2, constants.HEIGHT/2 + 45 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.NO_TEXT.get_height()) / 2))
            else:
                constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.NO_TEXT, (constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.NO_TEXT.get_width()) / 2, constants.HEIGHT/2 + 45 + (constants.SPLIT_BUTTON.get_height() - constants.NO_TEXT.get_height()) / 2))

            # "Yes" Button
            if constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.YES_TEXT, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.YES_TEXT.get_width()) / 2, constants.HEIGHT/2 + 45 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.YES_TEXT.get_height()) / 2))

            else:
                constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2, constants.HEIGHT/2 + 45))
                constants.SCREEN.blit(constants.YES_TEXT, (constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.YES_TEXT.get_width()) / 2, constants.HEIGHT / 2 + 45 + (constants.SPLIT_BUTTON.get_height() - constants.YES_TEXT.get_height()) / 2))


            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH - constants.WIDTH / 4 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                    pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
                    screens.titleScreen()
                if event.type == MOUSEBUTTONDOWN and constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 <= mouse[0] <= constants.WIDTH / 2 + (constants.WIDTH / 4 - constants.HOVER_SPLIT_BUTTON.get_width()) / 2 + constants.HOVER_SPLIT_BUTTON.get_width() and constants.HEIGHT/2 + 45 <= mouse[1] <= constants.HEIGHT/2 + 45 + constants.HOVER_SPLIT_BUTTON.get_height():
                    pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
                    constants.L1 = 1
                    constants.R1 = 1
                    constants.L2 = 1
                    constants.R2 = 1
                    screens.updateGameScreen()
                    return False
            pygame.display.update()
            pygame.time.delay(10)
            
    else:
        return False


def split(attacker, attack):
    split = True
    constants.SCREEN.blit(constants.SPILT_TEXT, (constants.WIDTH/4 - constants.SPILT_TEXT.get_width()/2, constants.HEIGHT/2 - constants.SPILT_TEXT.get_height()/2))

    match (attacker):
            case "L1":
                left_1 = constants.NUMBERS_FONT.render(str(constants.L1), True, constants.SELECTED)
                constants.SCREEN.blit(left_1, ((constants.WIDTH/2 - left_1.get_width())/2, (constants.HEIGHT/2-35 - left_1.get_height())/2))
                       
            case "L2":
                left_2 = constants.NUMBERS_FONT.render(str(constants.L2), True, constants.SELECTED)
                constants.SCREEN.blit(left_2, ((constants.WIDTH/2 - left_2.get_width())/2, constants.HEIGHT/2 + (constants.HEIGHT/2+35 - left_2.get_height())/2))
                       
            case "R1":
                right_1 = constants.NUMBERS_FONT.render(str(constants.R1), True, constants.SELECTED)
                constants.SCREEN.blit(right_1, (constants.WIDTH/2 + (constants.WIDTH/2 - right_1.get_width())/2, (constants.HEIGHT/2-35 - right_1.get_height())/2))
                       
            case 'R2':
                right_2 = constants.NUMBERS_FONT.render(str(constants.R2), True, constants.SELECTED)
                constants.SCREEN.blit(right_2, (constants.WIDTH/2 + (constants.WIDTH/2 - right_2.get_width())/2, constants.HEIGHT/2 + (constants.HEIGHT/2+35 - right_2.get_height())/2))


    # split conditions
    # make buttons and object and check the click area with getwidth funciton
    while split == True:

        mouse = pygame.mouse.get_pos()
        match (attack):
            case 4:
                if constants.WIDTH/2 + 255 <= mouse[0] <= constants.WIDTH/2 + 305 and constants.HEIGHT/2-25 <= mouse[1] <= constants.HEIGHT/2+25:
                    constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH/2 + 255, constants.HEIGHT/2-25))
                else:
                    constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH/2 + 255, constants.HEIGHT/2-25))

                if constants.WIDTH/2 + 155 <= mouse[0] <= constants.WIDTH/2 + 205 and constants.HEIGHT/2 - 25 <= mouse[1] <= constants.HEIGHT/2 + 25:
                    constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH/2 + 155, constants.HEIGHT/2-25))
                else:
                    constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH/2 + 155, constants.HEIGHT/2-25))

                if constants.WIDTH/2 + 55 <= mouse[0] <= constants.WIDTH/2 + 105 and constants.HEIGHT/2 - 25 <= mouse[1] <= constants.HEIGHT/2 + 25:
                    constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH/2 + 55, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2))
                else:
                    constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH/2 + 55, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2))
                
                constants.SCREEN.blit(constants.SPLIT_1, (constants.WIDTH/2 + 55 + (constants.HOVER_SPLIT_BUTTON.get_width() - constants.SPLIT_1.get_width())/2, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.SPLIT_1.get_height())/2))
                constants.SCREEN.blit(constants.SPLIT_2, (constants.WIDTH/2 + 155 + (constants.HOVER_SPLIT_BUTTON.get_width() - constants.SPLIT_2.get_width())/2, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.SPLIT_2.get_height())/2))
                constants.SCREEN.blit(constants.SPLIT_3, (constants.WIDTH/2 + 255 + (constants.HOVER_SPLIT_BUTTON.get_width() - constants.SPLIT_3.get_width())/2, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.SPLIT_3.get_height())/2))
            case 3:
                if constants.WIDTH/2 + 155 <= mouse[0] <= constants.WIDTH/2 + 205 and constants.HEIGHT/2 - 25 <= mouse[1] <= constants.HEIGHT/2 + 25:
                    constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH/2 + 155, constants.HEIGHT/2-25))
                else:
                    constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH/2 + 155, constants.HEIGHT/2-25))

                if constants.WIDTH/2 + 55 <= mouse[0] <= constants.WIDTH/2 + 105 and constants.HEIGHT/2 - 25 <= mouse[1] <= constants.HEIGHT/2 + 25:
                    constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH/2 + 55, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2))
                else:
                    constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH/2 + 55, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2))
                
                constants.SCREEN.blit(constants.SPLIT_1, (constants.WIDTH/2 + 55 + (constants.HOVER_SPLIT_BUTTON.get_width() - constants.SPLIT_1.get_width())/2, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.SPLIT_1.get_height())/2))
                constants.SCREEN.blit(constants.SPLIT_2, (constants.WIDTH/2 + 155 + (constants.HOVER_SPLIT_BUTTON.get_width() - constants.SPLIT_2.get_width())/2, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.SPLIT_1.get_height())/2))
            case 2:
                if constants.WIDTH/2 + 55 <= mouse[0] <= constants.WIDTH/2 + 105 and constants.HEIGHT/2 - 25 <= mouse[1] <= constants.HEIGHT/2 + 25:
                    constants.SCREEN.blit(constants.HOVER_SPLIT_BUTTON, (constants.WIDTH/2 + 55, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2))
                else:
                    constants.SCREEN.blit(constants.SPLIT_BUTTON, (constants.WIDTH/2 + 55, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2))
                
                constants.SCREEN.blit(constants.SPLIT_1, (constants.WIDTH/2 + 55 + (constants.HOVER_SPLIT_BUTTON.get_width() - constants.SPLIT_1.get_width())/2, constants.HEIGHT/2 - constants.SPLIT_BUTTON.get_height()/2 + (constants.HOVER_SPLIT_BUTTON.get_height() - constants.SPLIT_1.get_height())/2))
               
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            mouse = pygame.mouse.get_pos()

            # split 1
            if event.type == MOUSEBUTTONDOWN and constants.WIDTH/2 + 55 <= mouse[0] <= constants.WIDTH/2 + 105 and constants.HEIGHT/2-25 <= mouse[1] <= constants.HEIGHT/2+25:
                match (attacker):
                    case "R1":
                        if constants.L1 + 1 < 5:
                            constants.L1 += 1
                            constants.R1 -= 1
                            split = False
                        else: 
                            return False
                    case "L1":
                        if constants.R1 + 1 < 5:
                            constants.R1 += 1
                            constants.L1 -= 1
                            split = False
                        else:
                            return False
                    case "R2":
                        if constants.L2 + 1 < 5:
                            constants.L2 += 1
                            constants.R2 -= 1
                            split = False
                        else:
                            return False
                    case "L2":
                        if constants.R2 + 1 < 5:
                            constants.R2 += 1
                            constants.L2 -= 1
                            split = False
                        else:
                            return False

            # split 2
            if event.type == MOUSEBUTTONDOWN and constants.WIDTH/2 + 155 <= mouse[0] <= constants.WIDTH/2 + 205 and constants.HEIGHT/2-25 <= mouse[1] <= constants.HEIGHT/2+25 and (attack == 3 or attack == 4):
                match (attacker):
                    case "R1":
                        if constants.L1 + 2 < 5:
                            constants.L1 += 2
                            constants.R1 -= 2
                            split = False
                        else: 
                            return False
                    case "L1":
                        if constants.R1 + 1 < 5:
                            constants.R1 += 2
                            constants.L1 -= 2
                            split = False
                        else:
                            return False
                    case "R2":
                        if constants.L2 + 2 < 5:
                            constants.L2 += 2
                            constants.R2 -= 2
                            split = False
                        else:
                            return False
                    case "L2":
                        if constants.R2 + 2 < 5:
                            constants.R2 += 2
                            constants.L2 -= 2
                            split = False
                        else:
                            return False

            # split 3
            if event.type == MOUSEBUTTONDOWN and constants.WIDTH/2 + 255 <= mouse[0] <= constants.WIDTH/2 + 305 and constants.HEIGHT/2-25 <= mouse[1] <= constants.HEIGHT/2+25 and attack == 4:
                match (attacker):
                    case "R1":
                        if constants.L1 + 3 < 5:
                            constants.L1 += 3
                            constants.R1 -= 3
                            split = False
                        else: 
                            return False
                    case "L1":
                        if constants.R1 + 3 < 5:
                            constants.R1 += 3
                            constants.L1 -= 3
                            split = False
                        else:
                            return False
                    case "R2":
                        if constants.L2 + 3 < 5:
                            constants.L2 += 3
                            constants.R2 -= 3
                            split = False
                        else:
                            return False
                    case "L2":
                        if constants.R2 + 3 < 5:
                            constants.R2 += 3
                            constants.L2 -= 3
                            split = False
                        else:
                            return False

        

        pygame.display.update()
        pygame.time.delay(10)
    
    pygame.mixer.Sound.play(constants.BUTTON_CLICK_FX)
    return True