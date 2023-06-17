import pygame
import scene_class
import button_class
import functions

pygame.init()

WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode([WIDTH, HEIGHT])
c = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARD_IMAGE = pygame.image.load("chess board.png")
MENU_IMAGE = pygame.image.load("menu.png")
ONE_PLAYER_IMAGE = pygame.image.load("1 player button.png")
TWO_PLAYER_IMAGE = pygame.image.load("2 player button.png")

#--------------------------------------------------------------------

game_scene = scene_class.Game_Scene(WIDTH, HEIGHT, BOARD_IMAGE)
menu_scene = scene_class.Menu_Scene(WIDTH, HEIGHT, MENU_IMAGE)

    # On the menu screen
one_player_button = button_class.Button(0, 0, ONE_PLAYER_IMAGE)
#one_player_button_pos = functions.position(menu_scene, one_player_button, 1/2, 1/5)
#one_player_button.change_position(one_player_button_pos)

#--------------------------------------------------------------------

menu_scene.add("1", one_player_button)

#--------------------------------------------------------------------




def game_loop():
    functions.check_user_input(game_scene)
    functions.run_ai()
    functions.move_everything()
    functions.resolve_collisions()
    functions.draw_scene(game_scene, window)
    functions.play_sounds()

def menu_loop():
    functions.check_user_input(menu_scene)
    functions.resolve_collisions()
    functions.draw_scene(menu_scene, window)
    functions.play_sounds()
        

def program_loop():
    while menu_scene.active or game_scene.active:
        if menu_scene.active:
            menu_loop()
            c.tick(FPS)
        elif game_scene.active:
            game_loop()
            c.tick(FPS)

#------------------------------------------------------------------
program_loop()