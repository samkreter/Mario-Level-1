from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c
from sets import Set
from moves import MOVES

import pygame as pg
import random
import numpy as np
import time


def singleCrossOver(p1,p2):
    start = .2
    index = random.choice(range(int(len(p1)*start),len(p1)))
    return (p1[:index] + p2[index:],p2[:index] + p1[index:])

def main():
    """Add states to control here."""
    moveList = [pg.K_a,pg.K_RIGHT,0]

    MAXFITNESS = 71000
    NumParents = 2
    MutationPercent = .3
    crossProb = .9
    NumMutations = int(len(MOVES) * MutationPercent)
    parents = []
    children = []
    lastPos = None
    parentsFitness = []
    childFitness = []

    #init the parents
    for i in range(NumParents):
        parents.append(list(MOVES))
        parentsFitness.append(MAXFITNESS)



    while(1):

        ####Generation
        for i in range(NumParents):
            childBreed = []

            #Mutate the parents
            childBreed.append(list(parents[i]))




            #Mutation
            for index in (random.sample(range(len(MOVES)), NumMutations)):
                childBreed[0][index] = random.choice(moveList)

            #CrossOver
            if random.uniform(0,1) < crossProb and i < NumParents - 1:
                print("doing crossOver")
                tmp = singleCrossOver(parents[i],parents[i+1])
                childBreed.append(tmp[0])
                childBreed.append(tmp[1])

            #Compute the fitness
            for j,child in enumerate(childBreed):

                print("Starting child:" + str(j) + " of parent:" + str(i))
                while(1):
                    #Randomize around point of death to find living solution
                    if(lastPos):
                        for index in range(lastPos - 150,lastPos):
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
                    print("died for child:" + str(j))

                #add solution and fitness
                children.append(child)
                childFitness.append(cRun['current time'])

        #Combine parents and child for selection (U+V)
        parents = parents + children
        parentsFitness = parentsFitness + childFitness

        #Selection############
        selectSort = [i for i in sorted(enumerate(parentsFitness), key=lambda x:x[1])]
        selected = zip(*selectSort)[0][0:NumParents]
        print("selection is " + str(selected))
        #replace old parents with the newly selected ones
        parents = [parents[i] for i in selected]
        parentsFitness = [parentsFitness[i] for i in selected]


# np.savetxt("test.csv",t,delimiter=',')


        # state_dict = {c.MAIN_MENU: main_menu.Menu(),
        #               c.LOAD_SCREEN: load_screen.LoadScreen(),
        #               c.TIME_OUT: load_screen.TimeOut(),
        #               c.GAME_OVER: load_screen.GameOver(),
        #               c.LEVEL1: level1.Level1()}