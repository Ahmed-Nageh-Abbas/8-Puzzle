import pygame
from math import *
from sys import exit
import DFS

pygame.init()

# frames controller
clock = pygame.time.Clock()

# 9 rectangles
rects = []
rect_size = 150
rect_border = 3
screen_side_width = 20
for i in range(4):
    row = []
    for j in range(4):
        row.append(pygame.Rect(0, 0, 0, 0))
    rects.append(row)
for i in range(4): rects[0][i].y = screen_side_width
for i in range(4): rects[i][0].x = screen_side_width
for i in range(3):
    for j in range(3):
        xx = rects[i + 1][j].midright[0] + rect_border
        yy = rects[i][j + 1].midbottom[1] + rect_border
        rects[i + 1][j + 1].x = xx
        rects[i + 1][j + 1].y = yy
        rects[i + 1][j + 1].width = rect_size
        rects[i + 1][j + 1].height = rect_size

# set cells font
cell_font = pygame.font.Font('fonts/SpaceStory.otf', 100)
cell_font.set_bold(0)

# set initial states
start, end = [5,6,7,4,0,8,3,2,1], [1,3,4,8,6,2,7,0,5]

states = []
DFS.dfs(start, 4, end, states)
states = states[::-1]
print("number of states:", len(states))
p = 0

# set up display
screen_width = rect_size*3 + rect_border*4 + screen_side_width*2
screen_height = rect_size*3 + rect_border*4 + screen_side_width*2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load('puzzle.jpg'))
pygame.display.set_caption('8 Puzzle (DFS)')

# set up music
back_ground_sound = pygame.mixer.Sound('music/back_ground.mp3')
back_ground_sound.set_volume(0.2)
back_ground_sound.play(loops = -1)
one_move_sound = pygame.mixer.Sound('music/one_move.mp3')

PuzzleIsRunning = True
while PuzzleIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if p/60 >= len(states):
        pygame.quit()
        exit()
    
    screen.fill('#000033')
    border_rect = pygame.Rect(rects[1][1].x, rects[1][1].y, 3*rect_size+2*rect_border, 3*rect_size+2*rect_border)
    pygame.draw.rect(screen, '#6666ff', screen.get_rect(), screen_side_width,5)
    # draw 9 rectangles
    for i in range(3):
        for j in range(3):
            cell = states[int(p/60)][i][j]
            # define color
            color = (0, 125, 210)
            # check if cell empty
            if cell == 0: color, cell = '#000033', ''
            # draw current rectangle
            temp_rect = pygame.draw.rect(screen, color, rects[i + 1][j + 1], ceil(rect_size/2), 3)
            # write current cell_number
            num = cell_font.render(str(cell), True, 'white')
            screen.blit(num, num.get_rect(center = rects[i + 1][j + 1].center))

    if p % 60 == 0 and p: one_move_sound.play()
    if (p + 1) / 60 < len(states): p += 1

    pygame.display.update()
    clock.tick(45)