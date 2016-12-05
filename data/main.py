from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c
from sets import Set
from moves import MOVES

import pygame as pg
import random
import numpy as np
import time
import signal
import sys

#Timing and Results store
MainResults = []
ConfigResults = []
DeathResults = []

#catch the control c and save the files
def signal_handler(signal, frame):
        np.savetxt("timings/mainResults.csv",np.array(MainResults),delimiter=',')
        np.savetxt("timings/deathResults.csv",np.array(DeathResults),delimiter=',')
        sys.exit(0)


def singleCrossOver(p1,p2):
    start = .2
    index = random.choice(range(int(len(p1)*start),len(p1)))
    return (p1[:index] + p2[index:],p2[:index] + p1[index:])

def main():
    """Add states to control here."""

    #Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    #move list for random options to create a valid solution laster
    moveList = [pg.K_a,pg.K_RIGHT,0]


    MAXFITNESS = 71000
    MAX_GERATIONS = 1
    NumParents = 1
    MutationPercent = .3
    crossProb = .9
    NumMutations = int(len(MOVES) * MutationPercent)
    parents = []
    children = []
    lastPos = None
    parentsFitness = []
    childFitness = []
    parentLastPosList = []
    childLastPosList = []

    #init the parents
    for i in range(NumParents):
        parents.append(list(MOVES))
        parentsFitness.append(MAXFITNESS)
        parentLastPosList.append(0)



    for gen in range(MAX_GERATIONS):

        iterTimeStart = time.time()
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
                deathTimes = []
                while(1):
                    deathTimeStart = time.time()
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

                    deathTimes.append(time.time() - deathTimeStart)

                    if not cRun['mario dead']:
                        print("Produced Working Solution")
                        lastPos = None
                        DeathResults.append([sum(deathTimes),len(deathTimes)] + deathTimes)
                        break

                    print("died for child:" + str(j))

                #add solution and fitness
                children.append(child)
                childFitness.append(cRun['current time'])
                childLastPosList.append(lastPos)


        iterTimeEnd = time.time()
        #Combine parents and child for selection (U+V)
        parents = parents + children
        parentsFitness = parentsFitness + childFitness
        parentLastPosList = parentLastPosList + childLastPosList

        #Selection############
        selectSort = sorted(enumerate(parentsFitness), key=lambda x:x[1])
        selected = zip(*selectSort)[0][0:NumParents]

        print("selection is " + str(selected))

        #replace old parents with the newly selected ones
        parents = [parents[i] for i in selected]
        parentsFitness = [parentsFitness[i] for i in selected]
        parentLastPosList = [parentLastPosList[i] for i in selected]


        print(gen)
        print(parentsFitness[0])
        print(parentLastPosList[0])
        print(iterTimeEnd - iterTimeStart)
        print(parents[0])
        print("######################")
        print(parents[0][:(parentLastPosList[0]+10)])

        #Iteration|Score|# of moves|Totoal Time|best move list
        MainResults.append([gen,parentsFitness[0],parentLastPosList[0],
            (iterTimeEnd - iterTimeStart), parents[0][:(parentLastPosList[0]+10)]])


    np.savetxt("timings/mainResults.csv",np.array(MainResults),delimiter=',')
    np.savetxt("timings/deathResults.csv",np.array(DeathResults),delimiter=',')

        # state_dict = {c.MAIN_MENU: main_menu.Menu(),
        #               c.LOAD_SCREEN: load_screen.LoadScreen(),
        #               c.TIME_OUT: load_screen.TimeOut(),
        #               c.GAME_OVER: load_screen.GameOver(),
        #               c.LEVEL1: level1.Level1()}