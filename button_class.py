import pygame

class Button:
    def __init__(self, x, y, image):
        self.x, self.y = x, y
        self.image = image
        self.width, self.height = self.image.get_width, self.image.get_height()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))