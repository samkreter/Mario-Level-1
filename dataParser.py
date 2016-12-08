import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Need for a work around with different column sizes
names = [i for i in range(1300)]

#open the files with the data
main = pd.read_csv("timings/m1.csv",names=names,sep=',',header=None)
death = pd.read_csv("timings/d1.csv",sep=',',header=None)
conf = pd.read_csv("timings/tconf.csv",sep=',',header=None)




#Print the Death Stats
print("Average time to solution: ",death[0].mean() / 60, " mins")
print("Average number of attemps: ",death[1].mean(), " attemps")

#Find the best score
m = main[1].argmax()
#find what configuration was the best score
for i in range(int(conf.shape[0])):
    if m > i*10 and m < i*10 + 10:
        confL = conf.iloc[i,1:].tolist()
        title = "NumParents:" + str(confL[0]) + " MP:" + str(confL[1]) + \
                    " CP: " + str(confL[2]) + " PS:" + str(confL[3])
        print("Max: ",main.iloc[m,1]," config:",title)


## Set up the Plots ###########################

yIter = []
#get the y axis or beset score
for i in range(10,main.shape[0],10):
    yIter.append(main.iloc[i-10:i,1].tolist())

#the rest is just plotting everthing to look pretty
fig = plt.figure(1)
fig2 = plt.figure(2)
figCount = 1
fig2Count = 1
#Plot each of the iterations vs Stuff
for index,y in enumerate(yIter):
    confL = conf.iloc[index,1:].tolist()
    title = "NP: "+ str(confL[0]) +"MP:" + str(confL[1]) + \
                    " CP: " + str(confL[2])

    #fig = plt.figure(figsize=[7,5])
    if confL[3]:
        ax = fig.add_subplot(320 + figCount)
        figCount += 1
    else:
        ax = fig2.add_subplot(220 + fig2Count)
        fig2Count += 1

    #ax = plt.subplot(230 + (index+1))
    l = ax.fill_between(range(1,11), y)


    ax.set_xlabel('Generation Number')
    ax.set_ylabel('Top Score')
    ax.set_title(title, y=1.08)
    ax.grid('on')
    ax.set_ylim(10000, 24000)

    l.set_facecolors([[.5,.5,.8,.3]])
    l.set_edgecolors([[0, 0, .5, .3]])
    l.set_linewidths([3])


    # add more ticks
    # remove tick marks
    ax.xaxis.set_tick_params(size=0)
    ax.yaxis.set_tick_params(size=0)

    # change the color of the top and right spines to opaque gray
    ax.spines['right'].set_color((.8,.8,.8))
    ax.spines['top'].set_color((.8,.8,.8))

    # tweak the axis labels
    xlab = ax.xaxis.get_label()
    ylab = ax.yaxis.get_label()

    xlab.set_style('italic')
    xlab.set_size(10)
    ylab.set_style('italic')
    ylab.set_size(10)

    # tweak the title
    ttl = ax.title
    ttl.set_weight('bold')

fig.tight_layout()
fig.suptitle('Propotional Selection', fontsize=20)
fig2.suptitle('Top Rank Selection', fontsize=20)
fig2.tight_layout()
fig.subplots_adjust(top=0.85)
fig2.subplots_adjust(top=0.85)
fig.savefig('WithPRop.png')
fig2.savefig('NoProp.png')
plt.show()


