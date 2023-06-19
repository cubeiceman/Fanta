import pygame

class Scene:
    def __init__(self, width, height, image):
        self.width, self.height = width, height
        self.image = image
        self.surface = pygame.Surface((width, height))
        self.active = True

    def add(self, type, key, value):
        # add some key and value to a determined dictionary inside the scene(game or menu)
        pass

    def handle_keyboard(self):
        # handles the keyboard, in this case, the quit button and the mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False

    def draw(self):
        # draws things onto the scene's surface, which is later drawn on the actual window
        pass


class Game_Scene(Scene):
    def __init__(self, width, height, image):
        super().__init__(width, height, image)
        self.active = False
        self.button_dict = {}
        self.piece_dict = {}

    def add(self, type, key, value):
        if type == "button":
            self.button_dict[key] = value
        elif type == "piece":
            self.piece_dict[key] = value

    def draw(self):
        for button in list(self.button_dict.values()):
            button.draw(self.surface)
        self.surface.blit(self.image, (0, 0))


class Menu_Scene(Scene):
    def __init__(self, width, height, image):
        super().__init__(width, height, image)
        self.button_dict = {}
        
    def add(self, key, value):
        self.button_dict[key] = value

    def draw(self):
        for button in list(self.button_dict.values()):
            button.draw(self.surface)
        self.surface.blit(self.image, (0, 0))
        