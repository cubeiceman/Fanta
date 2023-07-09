import pygame
import scene_class
import button_class
import functions

def version_check():
    ver_maj = pygame.version.vernum.major
    ver_min = pygame.version.vernum.minor

    if (ver_maj == 2 and ver_min < 5) or (ver_maj < 2):
        exit('pygame version 2.5 or later is needed. You have version ', ver_maj, '.', ver_min, '.')

version_check()

pygame.init()

WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode([WIDTH, HEIGHT])
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
#program_loop()

class Board:
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width, self.height = width, height

        self.square_width = self.width/8
        self.square_height = self.height/8

    def draw(self):
        square_width = self.width/8
        square_height = self.height/8
        square_color = [[0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0],
                        [0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0],
                        [0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0],
                        [0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0]]
        for row in range(8):
            for col in range(8):
                top = row*self.square_height
                left = col*self.square_width
                if square_color[row][col] == 0:
                    color = (100,100,100) # black
                else:
                    color = (200,200,200) # white
                pygame.draw.rect(self.surface, color, pygame.Rect(left, top, self.square_width, self.square_height))
                        
    def get_square(self, pos):
        col = ord(pos[0]) - ord('a')
        row = 7 - (ord(pos[1]) - ord('1'))
        top = row*self.square_height
        left = col*self.square_width

        return pygame.Rect(left,top,self.square_width, self.square_height)

    def get_surface(self):
        return self.surface

    def process_mouse_click(self, mouse_pos):
        pass # board does nothing with mouse clicks

class MainScene:
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width, self.height = width, height
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def draw(self):
        for object in self.objects:
            object.draw()
        pygame.display.flip()

    def process_mouse_click(self, mouse_pos):
        for object in self.objects:
            object.process_mouse_click(mouse_pos)

class Piece:
    def __init__(self, board, color, type, index, pos):
        self.board = board
        self.color = color
        self.type = type
        self.index = index
        self.pos = pos

        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render(self.type+str(self.index), True, (255,0,0))
        self.selected = False

        self.square = self.board.get_square(self.pos)

    def draw(self):
        if self.selected == False:
            color = (0,0,0) # black
            if self.color == 'white':
                color = (255,255,255) # white
        else:
            color = (0,255,0)

        pygame.draw.ellipse(self.board.get_surface(), color, self.square)

        self.board.get_surface().blit(self.text, self.square)

    def process_mouse_click(self, mouse_pos):
        if self.square.collidepoint(mouse_pos):
            if self.selected == True:
                self.selected = False
            else:
                self.selected = True

def init(surface):
    scene = MainScene(surface, WIDTH, HEIGHT)
    board = Board(surface, WIDTH, HEIGHT)
    scene.add(board)
    piece_info = [
        {'color':"black", 'type':"rook", 'index':0, 'pos':'a8'},
        {'color':"black", 'type':"knight", 'index':0, 'pos':'b8'},
        {'color':"black", 'type':"bishop", 'index':0, 'pos':'c8'},
        {'color':"black", 'type':"queen", 'index':0, 'pos':'d8'},
        {'color':"black", 'type':"king", 'index':0, 'pos':'e8'},
        {'color':"black", 'type':"bishop", 'index':1, 'pos':'f8'},
        {'color':"black", 'type':"knight", 'index':1, 'pos':'g8'},
        {'color':"black", 'type':"rook", 'index':1, 'pos':'h8'},
        {'color':"black", 'type':"pawn", 'index':0, 'pos':'a7'},
        {'color':"black", 'type':"pawn", 'index':1, 'pos':'b7'},
        {'color':"black", 'type':"pawn", 'index':2, 'pos':'c7'},
        {'color':"black", 'type':"pawn", 'index':3, 'pos':'d7'},
        {'color':"black", 'type':"pawn", 'index':4, 'pos':'e7'},
        {'color':"black", 'type':"pawn", 'index':5, 'pos':'f7'},
        {'color':"black", 'type':"pawn", 'index':6, 'pos':'g7'},
        {'color':"black", 'type':"pawn", 'index':7, 'pos':'h7'},

        {'color':"white", 'type':"pawn", 'index':0, 'pos':'a2'},
        {'color':"white", 'type':"pawn", 'index':1, 'pos':'b2'},
        {'color':"white", 'type':"pawn", 'index':2, 'pos':'c2'},
        {'color':"white", 'type':"pawn", 'index':3, 'pos':'d2'},
        {'color':"white", 'type':"pawn", 'index':4, 'pos':'e2'},
        {'color':"white", 'type':"pawn", 'index':5, 'pos':'f2'},
        {'color':"white", 'type':"pawn", 'index':6, 'pos':'g2'},
        {'color':"white", 'type':"pawn", 'index':7, 'pos':'h2'},
        {'color':"white", 'type':"rook", 'index':0, 'pos':'a1'},
        {'color':"white", 'type':"knight", 'index':0, 'pos':'b1'},
        {'color':"white", 'type':"bishop", 'index':0, 'pos':'c1'},
        {'color':"white", 'type':"queen", 'index':0, 'pos':'d1'},
        {'color':"white", 'type':"king", 'index':0, 'pos':'e1'},
        {'color':"white", 'type':"bishop", 'index':1, 'pos':'f1'},
        {'color':"white", 'type':"knight", 'index':1, 'pos':'g1'},
        {'color':"white", 'type':"rook", 'index':1, 'pos':'h1'}
        ]

    for info in piece_info:
        piece = Piece(board, info['color'], info['type'], info['index'], info['pos'])
        scene.add(piece)
    scene.draw()

    return scene

def check_for_user_input(scene):
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            scene.process_mouse_click(mouse_pos)

def draw_graphics(scene):
    scene.draw()

def my_loop(scene):
    while True:
        check_for_user_input(scene)
        draw_graphics(scene)

#####################################################

scene = init(surface)

my_loop(scene)

user_input = input("Press any key to continue...")
