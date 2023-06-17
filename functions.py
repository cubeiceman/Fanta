import pygame

def position(surface, object, x_proportion, y_proportion):
    """
    Returns top x and y based on the proportions given and the width/height and the width and height of the object

    Parameters:
    surface (class): width and height will be used for the new position
    object (class or rect): width and height will be used for the new position
    x_proportions (float): a fraction between 0 and 1
    y_proportions (float): a fraction between 0 and 1

    Returns:
    new_x (int): the top x of the new position
    new_y (int): the top y of the new position
    """
    new_center_x = surface.width * x_proportion
    new_center_y = surface.height * y_proportion
    
    new_x = new_center_x - (object.width / 2)
    new_y = new_center_y - (object.height / 2)
    return (new_x, new_y)

def check_user_input(scene):
    """
    Checks for user input in the scene

    Parameters:
    scene (class): the surface that checks for user input

    Returns
    None
    """
    scene.handle_keyboard()

def run_ai():
    """
    Runs the ai of the computer

    Parameters:
    None

    Returns
    None
    """
    pass

def move_everything():
    """
    Moves everything in the scene

    Parameters:
    None

    Returns
    None
    """
    pass

def resolve_collisions():
    """
    Checks for colliding objects in the scene

    Parameters:
    None

    Returns
    None
    """
    pass

def play_sounds():
    """
    Plays sounds in the scene based on what happened

    Parameters:
    None

    Returns
    None
    """
    pass

def draw_scene(scene, window):
    """
    Draws a scene surface onto the main window

    Parameters:
    scene (class): the surface that will be drawn
    window (window): the surface that the scene is being drawn on

    Returns
    None
    """
    scene.draw()
    window.blit(scene.surface, (0, 0))
    pygame.display.flip()