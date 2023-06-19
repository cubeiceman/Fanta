import pygame

class Button:
    def __init__(self, x, y, image):
        self.x, self.y = x, y
        self.image = image
        self.width, self.height = int(image.get_width()), int(image.get_height())
        self.surface = pygame.Surface((self.width, self.height))

    def change_position(self, new_pos):
        self.x = new_pos[0]
        self.y = new_pos[1]

    def draw(self, scene_surface):
        self.surface.blit(self.image, (0, 0))
        scene_surface.blit(self.surface, (self.x, self.y))
