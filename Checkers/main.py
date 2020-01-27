import pygame as pyg
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
        self.token = None
        self.status = 'playing'
        self.turn = r.randrange(2)
        self.players = ['x','o']
        self.can_jump = False
        pyg.display.set_caption("%s's turn" % self.players[self.turn % 2])
        self.game_board = [ ['x','_','x','_','x','_','x','_'],
                            ['_','x','_','x','_','x','_','x'],
                            ['x','_','x','_','x','_','x','_'],
			    ['_','_','_','_','_','_','_','_'],
			    ['_','_','_','_','_','_','_','_'],
			    ['_','o','_','o','_','o','_','o'],
			    ['o','_','o','_','o','_','o','_'],
			    ['_','o','_','o','_','o','_','o'] ]

    def check_mouse_click(self, mouse_position):
        row = get_mouse_x(mouse_position)
        column = get_mouse_y(mouse_position)
        if self.token:
            return True
        else:
            if self.game_board[row][column].lower() == self.players[self.turn%2]:
                self.token = [row, column]
        
    def draw(self):
        for i in range(9):
            pyg.draw.line(screen, c_BLACK, [int(float(i*WIDTH/8)), 0], [int(float(i*WIDTH/8)), HEIGHT], 5)
            pyg.draw.line(screen, c_BLACK, [0, int(float(i*HEIGHT/8))], [WIDTH, int(float(i*HEIGHT/8))], 5)
        font = pyg.font.SysFont('Calibri', GAME_PIECE_SIZE, False, False)
        for r in range(len(self.game_board)):
            for c in range(len(self.game_board[r])):
                pieces = self.game_board[r][c]
                if pieces == 'x':
                    change_color = c_RED
                else:
                    change_color = c_BLACK
                if self.token:
                    if self.token[0] == r and self.token[1] == c:
                        change_color = c_GREEN
                if pieces != '_':
                    pieces_show = font.render(self.game_board[r][c], True, change_color)
                    x = WIDTH / 8 * c + WIDTH / 16
                    y = HEIGHT / 8 * r + HEIGHT / 16
                    screen.blit(pieces_show, [int(float(x - pieces_show.get_width()/2)), int(float(y - pieces_show.get_height()/2))])

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
                    
pyg.init()
size = (WIDTH, HEIGHT)
screen = pyg.display.set_mode(size)

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
            print ('Mouse clicked!')
            g.check_mouse_click(pyg.mouse.get_pos())
        	
    # fill background color
    screen.fill(c_BEIGE)
    # draw game board
    g.draw()
    # keep updating the graphics
    pyg.display.flip()

# close and quit applcation
# program gets stuck without this
pyg.quit()
