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

#--------------------------------------------------------------------

game_scene = scene_class.Game_Scene(WIDTH, HEIGHT, BOARD_IMAGE)
menu_scene = scene_class.Menu_Scene(WIDTH, HEIGHT, MENU_IMAGE)

    # On the menu screen
#one_player_button = button_class.button(menu)

#--------------------------------------------------------------------



#--------------------------------------------------------------------




def game_loop():
    functions.check_user_input(game_scene)
    functions.run_ai()
    functions.move_everything()
    functions.resolve_collisions()
    functions.draw_scene(game_scene, window)
    functions.play_sounds()

def menu_loop():
    while menu_scene.active:
        functions.check_user_input(menu_scene)
        functions.resolve_collisions()
        functions.draw_scene(menu_scene, window)
        functions.play_sounds()
        c.tick(FPS)

def program_loop():
    while menu_scene.active or game_scene.active:
        if menu_scene.active:
            menu_loop()
        elif game_scene.active:
            game_loop()

#------------------------------------------------------------------
program_loop()