import pygame

def check_user_input(scene):
    scene.handle_keyboard()

def run_ai():
    pass

def move_everything():
    pass

def resolve_collisions():
    pass

def play_sounds():
    pass

def draw_scene(scene, window):
    scene.draw()
    window.blit(scene.surface, (0, 0))
    pygame.display.flip()