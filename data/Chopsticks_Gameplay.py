import pygame
import Chopsticks_Screens as screens
import Chopsticks_Constants as constants
import Chopsticks_Game_Conditions as conditions
from pygame.constants import MOUSEBUTTONDOWN

def startGame():
    # game starts
    game_over = False
    attack = 0
    attacker = ""
    constants.R1 = 1
    constants.R2 = 1
    constants.L1 = 1
    constants.L2 = 1

    while game_over == False:
        # render game screen
        screens.updateGameScreen()

        selected = False
        move = False

        # player 1's turn
        while selected == False or move == False:
            constants.SCREEN.blit(constants.P1_TURN, (constants.WIDTH/2 - constants.P1_TURN.get_width()/2, constants.HEIGHT/2 - constants.P1_TURN.get_height()/2))

            selected = False
            while selected == False:
                for ev in pygame.event.get():
                    
                    mouse = pygame.mouse.get_pos()

                    if ev.type == pygame.QUIT:
                        pygame.quit()

                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and 0 <= mouse[1] <= constants.HEIGHT/2-35 and constants.L1 > 0:
                        left_1 = constants.NUMBERS_FONT.render(str(constants.L1), True, constants.SELECTED)
                        constants.SCREEN.blit(left_1, ((constants.WIDTH/2 - left_1.get_width())/2, (constants.HEIGHT/2-35 - left_1.get_height())/2))
                        attack = constants.L1
                        attacker = "L1"
                        selected = True
                        move = False

                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2+1 <= mouse[0] <= constants.WIDTH and 0 <= mouse[1] <= constants.HEIGHT/2-35 and constants.R1 > 0:
                        right_1 = constants.NUMBERS_FONT.render(str(constants.R1), True, constants.SELECTED)
                        constants.SCREEN.blit(right_1, (constants.WIDTH/2 + (constants.WIDTH/2 - right_1.get_width())/2, (constants.HEIGHT/2-35 - right_1.get_height())/2))
                        attack = constants.R1
                        attacker = "R1"
                        selected = True
                        move = False

                pygame.display.update()
                pygame.time.delay(10)

            move = False
            while move == False:
                for ev in pygame.event.get():
                    
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                    
                    mouse = pygame.mouse.get_pos()

                    # deselect choice
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and 0 <= mouse[1] <= constants.HEIGHT/2-35 and attacker == "L1":
                        selected = False
                        screens.updateGameScreen()
                        move = True
                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2 <= mouse[0] <= constants.WIDTH and 0 <= mouse[1] <= constants.HEIGHT/2-35 and attacker == "R1":
                        selected = False
                        screens.updateGameScreen()
                        move = True

                    # split choices
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and 0 <= mouse[1] <= constants.HEIGHT/2-35 and attacker == "R1" and constants.L1 < 4 and constants.R1 > 1:
                        screens.updateGameScreen()
                        move = conditions.split(attacker, attack)
                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2 <= mouse[0] <= constants.WIDTH and 0 <= mouse[1] <= constants.HEIGHT/2-35 and attacker == "L1" and constants.R1 < 4 and constants.L1 > 1:
                       screens.updateGameScreen()
                       move = conditions.split(attacker, attack)

                    # attack choices
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and constants.HEIGHT/2+35 <= mouse[1] <= constants.HEIGHT:
                        constants.L2 += attack
                        if constants.L2 >= 5:
                            constants.L2 = 0
                        move = True
                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2+1 <= mouse[0] <= constants.WIDTH and constants.HEIGHT/2+35 <= mouse[1] <= constants.HEIGHT:
                        constants.R2 += attack
                        if constants.R2 >= 5:
                            constants.R2 = 0
                        move = True

                pygame.display.update()
                pygame.time.delay(10)


        # update game screen
        screens.updateGameScreen()

        selected = False
        move = False

        # check if there's a winner
        game_over = conditions.checkWinner()

        if game_over:
            selected = True
            move = True
        

        # player 2's turn
        while selected == False or move == False:
            constants.SCREEN.blit(constants.P2_TURN, (constants.WIDTH/2 - constants.P2_TURN.get_rect().width/2, constants.HEIGHT/2 - constants.P2_TURN.get_height()/2))

            while selected == False:
                for ev in pygame.event.get():
                    
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                    
                    mouse = pygame.mouse.get_pos()
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and mouse[1] > constants.HEIGHT/2+35 and constants.L2 > 0:
                        left_2 = constants.NUMBERS_FONT.render(str(constants.L2), True, constants.SELECTED)
                        constants.SCREEN.blit(left_2, ((constants.WIDTH/2 - left_2.get_width())/2, constants.HEIGHT/2 + (constants.HEIGHT/2+35 - left_2.get_height())/2))
                        attack = constants.L2
                        attacker = "L2"
                        selected = True
                        move = False

                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2+1 <= mouse[0] <= constants.WIDTH and mouse[1] > constants.HEIGHT/2+35 and constants.R2 > 0:
                        right_2 = constants.NUMBERS_FONT.render(str(constants.R2), True, constants.SELECTED)
                        constants.SCREEN.blit(right_2, (constants.WIDTH/2 + (constants.WIDTH/2 - right_2.get_width())/2, constants.HEIGHT/2 + (constants.HEIGHT/2+35 - right_2.get_height())/2))
                        attack = constants.R2
                        attacker = "R2"
                        selected = True
                        move = False
                
                pygame.display.update()
                pygame.time.delay(10)

            while move == False:
                for ev in pygame.event.get():
                    
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                    
                    mouse = pygame.mouse.get_pos()

                    # deselect choice
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and constants.HEIGHT/2+35 <= mouse[1] <= constants.HEIGHT and attacker == "L2":
                        selected = False
                        screens.updateGameScreen()
                        move = True
                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2 <= mouse[0] <= constants.WIDTH and constants.HEIGHT/2+25 <= mouse[1] <= constants.HEIGHT and attacker == "R2":
                        selected = False
                        screens.updateGameScreen()
                        move = True

                    # split choices
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and constants.HEIGHT/2+35 <= mouse[1] <= constants.HEIGHT and attacker == "R2" and constants.L2 < 4 and constants.R2 > 1:
                        screens.updateGameScreen()
                        move =  conditions.split(attacker, attack)
                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2 <= mouse[0] <= constants.WIDTH and constants.HEIGHT/2+25 <= mouse[1] <= constants.HEIGHT and attacker == "L2" and constants.R2 < 4 and constants.L2 > 1:
                        screens.updateGameScreen()
                        move = conditions.split(attacker, attack)

                    # attack choices
                    if ev.type == MOUSEBUTTONDOWN and 0 <= mouse[0] <= constants.WIDTH/2 and 0 <= mouse[1] <= constants.HEIGHT/2-35:
                        constants.L1 += attack
                        if constants.L1 >= 5:
                            constants.L1 = 0
                        move = True
                    if ev.type == MOUSEBUTTONDOWN and constants.WIDTH/2+1 <= mouse[0] <= constants.WIDTH and 0 <= mouse[1] <= constants.HEIGHT/2-35:
                        constants.R1 += attack
                        if constants.R1 >= 5:
                            constants.R1 = 0
                        move = True

                pygame.display.update()
                pygame.time.delay(10)

        # render game screen
        screens.updateGameScreen()

        # check if there's a winner
        game_over = conditions.checkWinner()

        if game_over:
            selected = True
            move = True
            

        # updates the frames of the game
        pygame.display.update()
        pygame.time.delay(10)