from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c
from sets import Set
from moves import MOVES
import pygame as pg
import random




def main():
    """Add states to control here."""
    moveList = [pg.K_a,pg.K_RIGHT,0]
    # currMove = {}
    NumParents = 5
    MutationPercent = .3
    NumMutations = int(len(MOVES) * MutationPercent)
    parents = []
    cildren = []
    lastPos = None

    #init the parents
    for i in range(NumParents):
        parents.append(list(MOVES))


    parentsFitness = []
    childFitness = []
    while(1):

        for i in range(NumParents):

            #Mutate the parents
            child = list(parents[i])
            # for index in (lastPos + random.sample(range(len(MOVES)), NumMutations)):
            #     child[index] = random.choice(moveList)
            while(1):
                tmp = list(child)

                if(lastPos):
                    for index in range(lastPos - 100,lastPos + 10):
                        child[index] = random.choice(moveList)

                run_it = tools.Control(child)
                state_dict = {c.LEVEL1: level1.Level1()}
                run_it.setup_states(state_dict, c.LEVEL1)
                cRun = run_it.main()
                lastPos = cRun['counter']

                if not cRun['mario dead']:
                    print("We Lived")
                    break;







        # state_dict = {c.MAIN_MENU: main_menu.Menu(),
        #               c.LOAD_SCREEN: load_screen.LoadScreen(),
        #               c.TIME_OUT: load_screen.TimeOut(),
        #               c.GAME_OVER: load_screen.GameOver(),
        #               c.LEVEL1: level1.Level1()}