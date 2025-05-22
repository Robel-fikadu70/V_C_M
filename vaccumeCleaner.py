import pygame
import random

pygame.init()

grid = []
grid_size = 5
cell_size = 100
width = grid_size * cell_size
height = grid_size * cell_size

WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

agen_position = [0,0]
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Vacuum cleaner")

for i in range(5):
    row = []
    for j in range(5):
        row.append(random.choice([0,1]))
    grid.append(row)

def draw():
    for k in range(grid_size):
        for g in range(grid_size):
            Color = BROWN if grid[k][g] == 1 else WHITE
            pygame.draw.rect(screen, Color, (g*cell_size, k*cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (g*cell_size, k*cell_size, cell_size, cell_size), width = 2)
def agent():
    x, y = agen_position
    pygame.draw.circle(screen, BLUE, (y * cell_size + cell_size//2, x * cell_size + cell_size//2) ,cell_size//4)

def move():
    x, y = agen_position
    if grid[x][y] == 1:
        grid[x][y] = 0
    else:
        if y < grid_size - 1:
            agen_position[1] += 1
        elif x < grid_size - 1:
            agen_position[0] += 1
            agen_position[1] = 0



run = True
clock = pygame.time.Clock()
while run:
    screen.fill(WHITE)
    draw()
    agent()
    pygame.display.flip()
    move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(2)



pygame.quit()