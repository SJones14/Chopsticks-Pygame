import pygame

pygame.init()

# players' values
R1 = 1
R2 = 1
L1 = 1
L2 = 1

# time
FRAMERATE = 60

# Makes display screen
RES = (720,720)
SCREEN = pygame.display.set_mode(RES)
WIDTH = SCREEN.get_width()
HEIGHT = SCREEN.get_height()

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BACKGROUND = (200,130,58)
SHADOW = (54,69,79)
SELECTED = (255,255,51)

# fonts
FONT = pygame.font.Font("Pixel_Font/PixelFJVerdana12pt.ttf", 50)
SMALL_FONT = pygame.font.Font("Pixel_Font/PixelFJVerdana12pt.ttf", 25)
NUMBERS_FONT =  pygame.font.Font("Pixel_Font/PixelFJVerdana12pt.ttf", 100)
SMALL_NUMBERS_FONT = pygame.font.Font("Pixel_Font/PixelFJVerdana12pt.ttf", 20)
RULES_FONT = pygame.font.Font("Pixel_Font/PixelFJVerdana12pt.ttf", 12)

# Graphics
BUTTON = pygame.image.load("Graphics/Chopsticks_Button.png")
HOVER_BUTTON = pygame.image.load("Graphics/Chopsticks_LightButton.png")
SPLIT_BUTTON = pygame.image.load("Graphics/Chopsticks_Split_Button.png")
HOVER_SPLIT_BUTTON = pygame.image.load("Graphics/Chopsticks_Split_LightButton.png")
BACKGROUND_LOGO = pygame.image.load("Graphics/Background_Shadow.png")
LOGO = pygame.image.load("Graphics/Chopsticks_Logo.png")
icon = pygame.image.load('Graphics/Chopsticks_Icon.png')

# Sounds
BUTTON_CLICK_FX = pygame.mixer.Sound("Sounds/Button_Sound.mp3")
WINNER_FX = pygame.mixer.Sound("Sounds/Winner_Sound.mp3")

# Screens Text
PLAY = SMALL_FONT.render('Play', True, BLACK)
RULES = SMALL_FONT.render('Rules', True, BLACK)
QUIT = SMALL_FONT.render('Quit', True, BLACK)
BACK = SMALL_FONT.render('Back', True, BLACK)
TITLE = FONT.render('Chopsticks', True, BLACK)
TITLE_SHADOW = FONT.render('Chopsticks', True, SHADOW)
SS_TEXT = FONT.render('SJ.dev', True, BLACK)

# Rules Text
RULES_TITLE = SMALL_FONT.render('Rules:', True, BLACK)
RULES_LINE1 = RULES_FONT.render('Each player has 2 " hands ", each starting at 1 point each.', True, BLACK)
RULES_LINE2 = RULES_FONT.render('Both players take turns attacking the other player, adding', True, BLACK)
RULES_LINE2_2 = RULES_FONT.render('points to the other\'s hands.', True, BLACK)
RULES_LINE3 = RULES_FONT.render('Once a hand reaches 5 points it is eliminated.', True, BLACK)
RULES_LINE4 = RULES_FONT.render('A player can split points between hands as long as it doesn’t', True, BLACK)
RULES_LINE4_2 = RULES_FONT.render('eliminate the other hand and as long as the attacking hand is left', True, BLACK)
RULES_LINE4_3 = RULES_FONT.render('with at least 1 point.', True, BLACK)
RULES_LINE5 = RULES_FONT.render('Splitting may also be used to “revive” an eliminated hand.', True, BLACK)
RULES_LINE6 = RULES_FONT.render('A player wins by eliminating both of another player’s hands.', True, BLACK)
HTP_TITLE = SMALL_FONT.render('How to Play:', True, BLACK)
HTP_LINE1 = RULES_FONT.render('1. Pick a hand to attack with', True, BLACK)
HTP_LINE2 = RULES_FONT.render('2. Select an opponent\'s hand to attack or your other hand to split', True, BLACK)
HTP_LINE3 = RULES_FONT.render('3. If splitting select the amount of points to give to the', True, BLACK)
HTP_LINE3_2 = RULES_FONT.render('other hand', True, BLACK)
HTP_LINE4 = RULES_FONT.render('Extra: Reselect attacking hand to cancel selection', True, BLACK)

# Game Text
P1_NAME = SMALL_FONT.render('Player 1', True, BLACK)
P2_NAME = SMALL_FONT.render('Player 2', True, BLACK)
P1_WINNER_MESSAGE = SMALL_FONT.render('Player 1 Wins!', True, BLACK)
P2_WINNER_MESSAGE = SMALL_FONT.render('Player 2 Wins!', True, BLACK)
P1_TURN = SMALL_FONT.render('Player 1\'s Turn', True, BLACK)
P2_TURN = SMALL_FONT.render('Player 2\'s Turn', True, BLACK)
PLAY_AGAIN_MESSAGE = SMALL_FONT.render('Play Again?', True, BLACK)
SPLIT_1 = SMALL_NUMBERS_FONT.render('1', True, BLACK)
SPLIT_2 = SMALL_NUMBERS_FONT.render('2', True, BLACK)
SPLIT_3 = SMALL_NUMBERS_FONT.render('3', True, BLACK)
SPILT_TEXT = SMALL_FONT.render('Split Amount:' , True, BLACK)
YES_TEXT = SMALL_NUMBERS_FONT.render('Y', True, BLACK)
NO_TEXT = SMALL_NUMBERS_FONT.render('N', True, BLACK)
