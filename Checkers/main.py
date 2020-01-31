import pygame as pyg
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from collections import namedtuple
import math as m
import random as r
import os
import sys

#GAME BOARD COLORS
c_BLACK = (0,0,0)
c_WHITE = (255,255,255)
c_RED = (255,0,0)
c_GREEN = (0,255,0)
c_BLUE = (0,0,255)
c_BROWN = (139,69,19)
c_BEIGE = (245,245,220)

#CONSTANTS
WIDTH = 700
HEIGHT = 700
GAME_PIECE_SIZE = 100

class Game:
    def __init__(self):
        self.status = 'playing'
        self.turn = r.randrange(2)
        self.players = ['x','o']
        self.token = None
        self.can_jump = False

        if self.players[self.turn % 2] == 0:
            pyg.display.set_caption("Black's Turn")
        elif self.players[self.turn % 2 == 1]:
            pyg.display.set_caption("Red's Turn")
        
        self.game_board = [ ['x','_','x','_','x','_','x','_'],
                            ['_','x','_','x','_','x','_','x'],
                            ['x','_','x','_','x','_','x','_'],
			    ['_','_','_','_','_','_','_','_'],
			    ['_','_','_','_','_','_','_','_'],
			    ['_','o','_','o','_','o','_','o'],
			    ['o','_','o','_','o','_','o','_'],
			    ['_','o','_','o','_','o','_','o'] ]

    def check_mouse_click(self, mouse_position):
        row = get_mouse_y(mouse_position)
        column = get_mouse_x(mouse_position)
        if self.token:
            self.token = None
        else:
            if self.game_board[row][column].lower() == self.players[self.turn%2]:
                if column == 7:
                    print(str(row) + str(' + ') + str(column))
                    self.token = [row, column+2]
                else:
                    self.token = [row, column+1]
        
    def draw(self, imgx, imgy, imgg):
        for i in range(9):
            pyg.draw.line(screen, c_BLACK, [int(float(i*WIDTH/8)), 0], [int(float(i*WIDTH/8)), HEIGHT], 5)
            pyg.draw.line(screen, c_BLACK, [0, int(float(i*HEIGHT/8))], [WIDTH, int(float(i*HEIGHT/8))], 5)
        font = pyg.font.SysFont('Calibri', GAME_PIECE_SIZE, False, False)
        for r in range(len(self.game_board)):
            for c in range(len(self.game_board[r])):
                pieces = self.game_board[r][c]
                if self.token:
                    if self.token[0] == r and self.token[1] == c:
                        loadImg_g = pyg.image.load(imgg+".png")
                        screen.blit(loadImg_g, ([int(float(x - img_x.width/2)), int(float(y - img_x.height/2))]))
                if pieces != '_':
                    x = WIDTH / 8 * c + WIDTH / 16
                    y = HEIGHT / 8 * r + HEIGHT / 16
                    if pieces == 'x':
                        loadImg_x = pyg.image.load(imgx+".png")
                        screen.blit(loadImg_x, ([int(float(x - img_x.width/2)), int(float(y - img_x.height/2))]))
                    elif pieces == 'o':
                        loadImg_y = pyg.image.load(imgy+".png")
                        screen.blit(loadImg_y, ([int(float(x - img_y.width/2)), int(float(y - img_y.height/2))]))

    def validate_moves(self, player, location, nextrow, nextcol):
        currrow = location[0]
        currcol = location[1]
        thistoken = self.game_board[currrow][currcol]

        
        

def get_mouse_x(mouse_position):
    x = mouse_position[0]
    for i in range(1,8):
        if x < i*WIDTH/8:
            return i-1
    return 7

def get_mouse_y(mouse_position):
    y = mouse_position[1]
    for i in range(1,8):
        if y < i*HEIGHT/8:
            return i-1
    return 7

def make_pieces_image(img, color):
    dr = ImageDraw.Draw(img)
    dr.ellipse((0,0,100,100), color)

def save_pieces_image(img, color, string):
    make_pieces_image(img, color)
    img.save(string+".png")
                    
pyg.init()
size = (WIDTH, HEIGHT)
screen = pyg.display.set_mode(size)

# create and save board pieces
img_x = Image.new("RGB", (60,60), c_BEIGE)
img_y = Image.new("RGB", (60,60), c_BEIGE)
img_clicked = Image.new("RGB", (60,60), c_BEIGE)
save_pieces_image(img_x, c_RED, "img_x")
save_pieces_image(img_y, c_BLACK, "img_y")
save_pieces_image(img_clicked, c_GREEN, "img_g")

g = Game()

is_done = False

while not is_done:
    # if any user events occur
    for event in pyg.event.get():
        # if user closed game, then exit game
        if event.type == pyg.QUIT:
            done = True
        # if user pressed keyboard, ignore input
        # unless 'r' pressed --> restart program
        if event.type == pyg.KEYDOWN:
            entry = int(event.key)
            if entry == 114:
                os.execl(sys.executable, sys.executable, *sys.argv)
        # if user clicked mouse, get click position 
        if event.type == pyg.MOUSEBUTTONDOWN:
            #print ('Mouse clicked!')
            g.check_mouse_click(pyg.mouse.get_pos())
            pyg.display.update()
        	
    # fill background color
    screen.fill(c_BEIGE)
    # draw game board
    g.draw("img_x", "img_y", "img_g")
    # keep updating the graphics
    pyg.display.flip()

# close and quit applcation
# program gets stuck without this
pyg.quit()
