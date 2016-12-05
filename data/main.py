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

        ####Generation
        for i in range(NumParents):

            #Mutate the parents
            child = list(parents[i])
            # for index in (lastPos + random.sample(range(len(MOVES)), NumMutations)):
            #     child[index] = random.choice(moveList)


            while(1):
                #Randomize around point of death to find living solution
                if(lastPos):
                    for index in range(lastPos - 200,lastPos + 10):
                        child[index] = random.choice(moveList)

                #Run the fitness game
                run_it = tools.Control(child)
                state_dict = {c.LEVEL1: level1.Level1()}
                run_it.setup_states(state_dict, c.LEVEL1)
                cRun = run_it.main()

                #Get pos where death occured
                lastPos = cRun['counter']

                if not cRun['mario dead']:
                    print("Produced Working Solution")
                    break

            #add solution and fitness
            children.append(child)
            childFitness.append(cRun['current time'])

        #Combine parents and child for selection (U+V)
        parents = parents + children
        parentsFitness = parentsFitness + childFitness

        #Selection############
        selectSort = [i for i in sorted(enumerate(parentsFitness), key=lambda x:x[1])]
        selected = zip(*selectSort)[0][0:NumParents]

        #replace old parents with the newly selected ones
        parents = [parents[i] for i in selected]
        parentsFitness = [parentsFitness[i] for i in selected]




        # state_dict = {c.MAIN_MENU: main_menu.Menu(),
        #               c.LOAD_SCREEN: load_screen.LoadScreen(),
        #               c.TIME_OUT: load_screen.TimeOut(),
        #               c.GAME_OVER: load_screen.GameOver(),
        #               c.LEVEL1: level1.Level1()}