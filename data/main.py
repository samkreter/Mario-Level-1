from __future__ import division #because I hate python3

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
import itertools
import csv


MainResults = []
ConfigResults = []
DeathResults = []


#Make sure that the program does not fail to print the results
def writeOutput(MainResults,ConfigResults,DeathResults):

    f1 = open("timings/mainResults.csv",'a')
    f2 = open("timings/deathResults.csv",'a')
    f3 = open("timings/configResults.csv",'a')
    try:
        #Iteration | Score | # of moves | Totoal Time | best move list
        np.savetxt(f1, np.array(MainResults),delimiter=',',fmt="%.4f")
        print("passed first")
        #Total Time For solution | # of attempts
        np.savetxt(f2, np.array(DeathResults),delimiter=',',fmt="%.4f")
        print("passed second")
        # Link Index | NumParents | Mutation Prob | CrossOver Prob
        np.savetxt(f3,np.array(ConfigResults),delimiter=',',fmt="%.4f")
    except Exception, e:
        print(e)
        print("Failed to do percision")
        try:
            #Iteration | Score | # of moves | Totoal Time | best move list
            np.savetxt(f1, np.array(MainResults),delimiter=',')
            print("pass1")
            #Total Time For solution | # of attempts
            np.savetxt(f2, np.array(DeathResults),delimiter=',')
            print("pass2")
            # Link Index | NumParents | Mutation Prob | CrossOver Prob
            np.savetxt(f3,np.array(ConfigResults),delimiter=',')
        except Exception, e:
            print(e)
            print("Failed to do regular")


            wr1 = csv.writer(f1)
            wr2 = csv.writer(f2)
            wr3 = csv.writer(f3)

            wr1.writerows(f1)
            wr2.writerows(f2)
            wr3.writerows(f3)

        f1.close()
        f2.close()
        f3.close()
    #failed the regular

#catch the control c and save the files
def signal_handler(signal, frame):
        # np.savetxt("timings/mainResults.csv",np.array(MainResults),delimiter=',',fmt="%.4f")
        # np.savetxt("timings/deathResults.csv",np.array(DeathResults),delimiter=',',fmt="%.4f")
        # np.savetxt("timings/configResults.csv",np.array(ConfigResults),delimiter=',',fmt="%.4f")
        writeOutput()
        sys.exit(0)

#Perfroms one point cross over
def singleCrossOver(p1,p2):
    start = .2
    index = random.choice(range(int(len(p1)*start),len(p1)))
    return (p1[:index] + p2[index:],p2[:index] + p1[index:])

def main():

    #Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)


    #Timing and Results store
    global MainResults
    global ConfigResults
    global DeathResults

    #move list for random options to create a valid solution laster
    moveList = [pg.K_a,pg.K_RIGHT,0]

    # #Load in the best solution from last time
    # MOVES = list(np.loadtxt("timings/m1.csv",delimiter=',')[1][4:].astype(int))
    # MOVES += MOVES

    BASEFITNESS = 0
    MAX_GERATIONS = 10
    NumParentsList = (2,4,5)
    MutationPercent = .3
    MutationProbList = (0,.7,1)
    crossProbList = (0,.7,1)
    proportionalSelectList = (1,0)

    totalTimeStart = time.time()

    for NumParents,MutationProb,crossProb,proportionalSelect in list(itertools.product(NumParentsList,MutationProbList,crossProbList,proportionalSelectList)):
        #Make sure there is some for of mutation or there will be no change with parents
        if MutationProb == 0 and crossProb == 0:
            continue

        ConfigResults.append([float(len(MainResults)),float(NumParents),float(MutationProb),float(crossProb),float(proportionalSelect)])

        print("##### Using Configureation #######")
        print("NumParents: " + str(NumParents))
        print("MutationProb: " + str(MutationProb))
        print("crossProb: " + str(crossProb))
        print("proportionalSelect: " + str(proportionalSelect))
        print("#################################")

        NumMutations = int(len(MOVES) * MutationPercent)
        parents = []
        children = []
        lastPos = None
        parentsFitness = []
        childFitness = []
        parentLastPosList = []
        childLastPosList = []

        #initilize the parents
        for i in range(NumParents):
            parents.append(list(MOVES))
            parentsFitness.append(BASEFITNESS)
            parentLastPosList.append(0)


        for gen in range(MAX_GERATIONS):

            iterTimeStart = time.time()
            ####Generation
            for i in range(NumParents):
                childBreed = []

                #Mutate the parents
                childBreed.append(list(parents[i]))


                #Mutation
                if random.uniform(0,1) < MutationProb:
                    for index in (random.sample(range(len(MOVES)), NumMutations)):
                        childBreed[0][index] = random.choice(moveList)

                #CrossOver
                if random.uniform(0,1) < crossProb and i < NumParents - 1:
                    tmp = singleCrossOver(parents[i],parents[i+1])
                    childBreed.append(tmp[0])
                    childBreed.append(tmp[1])

                #Compute the fitness
                for j,child in enumerate(childBreed):

                    print("Gen:" + str(gen) + " - Starting child: " + str(j) + " of parent:" + str(i))
                    deathTimes = []
                    count = 0
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
                            DeathResults.append([sum(deathTimes),float(len(deathTimes))])
                            deathTimes = []
                            break
                        count = count + 1
                        if count > 100:
                            print("Times out")
                            cRun['score'] = 0
                            break;

                        print("died for child:" + str(j))

                    #add solution and fitness
                    children.append(child)
                    childFitness.append(cRun['score'])
                    childLastPosList.append(lastPos)
                    lastPos = None


            iterTimeEnd = time.time()
            #Combine parents and child for selection (U+V)
            parents = parents + children
            parentsFitness = parentsFitness + childFitness
            parentLastPosList = parentLastPosList + childLastPosList

            #Selection############

            if(proportionalSelect):
                overall = sum(parentsFitness)
                p = []
                #Create the probablilities
                for fit in parentsFitness:
                    p.append(fit/overall)

                selected = np.random.choice(len(parentsFitness), NumParents, p=p)

            else:
                selectSort = sorted(enumerate(parentsFitness), key=lambda x:x[1], reverse=True)
                selected = zip(*selectSort)[0][0:NumParents]

            print("selection is " + str(selected) + " High score is: " + str(parentsFitness[0]))

            #replace old parents with the newly selected ones
            parents = [parents[i] for i in selected]
            parentsFitness = [parentsFitness[i] for i in selected]
            parentLastPosList = [parentLastPosList[i] for i in selected]


            MainResults.append([gen,parentsFitness[0],parentLastPosList[0],
                (iterTimeEnd - iterTimeStart)] + parents[0][:(parentLastPosList[0]+10)])

            writeOutput(MainResults,ConfigResults,DeathResults)
            #Timing and Results store
            MainResults = []
            ConfigResults = []
            DeathResults = []

    print("Total time is: " + str(time.time() - totalTimeStart))




        # state_dict = {c.MAIN_MENU: main_menu.Menu(),
        #               c.LOAD_SCREEN: load_screen.LoadScreen(),
        #               c.TIME_OUT: load_screen.TimeOut(),
        #               c.GAME_OVER: load_screen.GameOver(),
        #               c.LEVEL1: level1.Level1()}