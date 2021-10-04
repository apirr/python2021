import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 300))

HOUSE_surface = pygame.display.set_mode((700, 300))

TREE_surface = pygame.display.set_mode((700, 300))

CLOUDS_surface = pygame.display.set_mode((700, 300))

GREEN_for_tree = tuple()
GREEN_for_tree = (15, 83, 14)

BLACK = tuple()
BLACK = (0, 0, 0)

WHITE = tuple()
WHITE = (255, 255, 255)

SKY_col = tuple()
SKY_col = (161, 235, 245)

GRASS_col = tuple()
GRASS_col = (14, 147, 37)

HOUSE_col = tuple()
HOUSE_col = (147, 107, 14)

ROOF_col = tuple()
ROOF_col = (235, 47, 68)

WINDOW_col = tuple()
WINDOW_col = (181, 98, 17)

GLASS_col = tuple()
GLASS_col = (14, 147, 145)

SUN_col = tuple()
SUN_col = (249, 194, 194)

polygon(screen, SKY_col, [(0, 65), (700, 65)], 150)
polygon(screen, GRASS_col, [(0, 215), (700, 215)], 150)

big_n_polygon = list()
small_npolygon = list()

def polygons(big_n_polygon, small_npolygon, x, y, R):
    '''
    функция задает координаты Солнца
    x - первая координата
    y - вторая координата
    R - радиус
    '''
    tmp_1 = tuple()
    tmp_2 = tuple()
    for i in range(20):
        tmp_1 = (x + R * math.cos(2 * math.pi * i/20)), (y + R * math.sin(2 * math.pi * i/20))
        tmp_2 = (x + 0.9 * R * math.cos(2 * math.pi / 40 + 2 * math.pi * i/20)), (y + 0.9 * R * math.sin(2 * math.pi / 40 + 2 * math.pi * i/20))
        big_n_polygon.append(tmp_1)
        small_npolygon.append(tmp_2)

def house(HOUSE_surface, x, y, scale, HOUSE_col, ROOF_col, WINDOW_col, GLASS_col):
    '''
    функция строит дом
    x - первая координата
    y - вторая координата
    scale - характерный размер объекта
    HOUSE_col - цвет дома
    ROOF_col - цвет крыши
    WINDOW_col - цвет рамки окна
    GLASS_col - цвет стекла в окне
    '''
    polygon(HOUSE_surface, BLACK, [(x - 2, y + 2), (x+110.0 * scale + 2, y + 2), (x + 110.0 * scale + 2,y + 75.0 * scale - 2), (x - 2, y + 75.0 * scale - 2)])
    a = 110.0 * scale
    b = 75.0 * scale
    polygon(HOUSE_surface, HOUSE_col, [(x, y), (x + 110.0 * scale, y), (x+110.0 * scale,y+75.0 * scale), (x, y+75.0 * scale)])
    polygon(HOUSE_surface, ROOF_col, [(x + a, y), (x, y), (x + a/2, y - 0.5*b)])
    polygon(HOUSE_surface, WINDOW_col, [(x + 38.0 * scale, y + 40.0 * scale), (x + 77.0 * scale, y + 40.0 * scale)], int(32 * scale))
    polygon(HOUSE_surface, GLASS_col, [(x + 40.0 * scale, y + 40.0 * scale), (x + 75.0 * scale, y + 40.0 * scale)], int(30 * scale))

def clouds(CLOUDS_surface, x, y, scale, GREY):
    '''
    функция создает облака
    x - первая координата
    y - вторая координата
    scale - характерный размер объекта
    GREY - цвет облаков
    '''
    for i in range(2):
        circle(CLOUDS_surface, BLACK, (x + i * int(15 * scale), y), int(14 * scale) + 1)
        circle(CLOUDS_surface, GREY, (x + i * int(15 * scale), y), int(14 * scale))

    for i in range (4):
        circle(CLOUDS_surface, BLACK, (x + i * int(15 * scale) - 15, y + 15), int(14 * scale) + 1)
        circle(CLOUDS_surface, GREY, (x + i * int(15 * scale) - 15, y + 15), int(14 * scale))

def tree(TREE_surface, x, y, scale, WOOD_col, GREEN_for_tree):
    '''
    функция садит дерево
    x - первая координата
    y - вторая координата
    scale - характерный размер объекта
    WOOD_col - цвет ствола
    GREEN_for_tree - цвет листвы
    '''
    polygon(TREE_surface, WOOD_col, [(x-5 * scale, y), (x-5 * scale, y + 50 * scale), (x+5 * scale, y + 50 * scale), (x+5, y)])

    circle(TREE_surface, BLACK, (x - 15 * scale, y - 5 * scale), int(15 * scale))
    circle(TREE_surface, GREEN_for_tree, (x - 15 * scale, y - 5 * scale), int(14 * scale))

    circle(TREE_surface, BLACK, (x - 15 * scale, y - 20 * scale), int(15 * scale))
    circle(TREE_surface, GREEN_for_tree, (x - 15 * scale, y - 20 * scale), int(14 * scale))

    circle(TREE_surface, BLACK, (x, y - 13 * scale), int(15 * scale))
    circle(TREE_surface, GREEN_for_tree, (x, y - 13 * scale), int(14 * scale))

    circle(TREE_surface, BLACK, (x, y - 28 * scale), int(15 * scale))
    circle(TREE_surface, GREEN_for_tree, (x, y - 28 * scale), int(14 * scale))

    circle(TREE_surface, BLACK, (x + 20 * scale, y - 5 * scale), int(15 * scale))
    circle(TREE_surface, GREEN_for_tree, (x + 20 * scale, y - 5 * scale), int(14 * scale))

    circle(TREE_surface, BLACK, (x + 20 * scale, y - 20 * scale), int(15 * scale))
    circle(TREE_surface, GREEN_for_tree, (x + 20 * scale, y - 20 * scale), int(14 * scale))

tree(TREE_surface, 400, 140, 1, BLACK, GREEN_for_tree)

clouds(CLOUDS_surface, 100, 75, 1, WHITE)

house(HOUSE_surface, 50, 145, 1, HOUSE_col, ROOF_col, WINDOW_col, GLASS_col)

tree(TREE_surface, 200, 155, 0.8, BLACK, GREEN_for_tree)

clouds(CLOUDS_surface, 300, 60, 0.8, WHITE)

clouds(CLOUDS_surface, 600, 50, 1.2, WHITE)

house(HOUSE_surface, 500, 160, 0.8, HOUSE_col, ROOF_col, WINDOW_col, GLASS_col)

polygons(big_n_polygon, small_npolygon, 500, 75, 20)

total = list()

for i in range(20):
    total.append(big_n_polygon[i])
    total.append(small_npolygon[i])

polygon(screen, SUN_col, total)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
