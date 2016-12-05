import pygame as pg
#MOVES = [pg.K_RIGHT,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT]
MOVES = [pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,pg.K_a,\
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    pg.K_a,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT, \
    #This line is for the first hole
    pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_RIGHT,pg.K_a,pg.K_RIGHT, \
    pg.K_LEFT,pg.K_LEFT,pg.K_LEFT,pg.K_LEFT,pg.K_LEFT,pg.K_LEFT,pg.K_LEFT, \
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]