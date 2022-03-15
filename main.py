from locale import normalize
import pandas as pd
from random import randint, sample, shuffle
from random import seed
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from itertools import count

def main():

    def newPlayer():
        playername = input("Bitte Name eingeben: ")
        print(playername +" wurde erfasst.")
        return pd.DataFrame([[playername,enterNumbers(1),enterNumbers(2),enterNumbers(3),enterNumbers(4),enterNumbers(5),enterNumbers(6),0,0]],columns=dfPlayer.columns)

    def enterNumbers(x):
        return int(input("Bitte " + str(x) + ". Zahl eingeben (zwischen 1 und 49): "))

    def randNumber():
        return randint(1,49)

    def pullNumbers():
        return [randNumber(),randNumber(),randNumber(),randNumber(),randNumber(),randNumber()]

    index = count()
    
    def animate(i):
        lspulledNumbers = pullNumbers()
        print(lspulledNumbers)
        dfpulledNumbers.loc[len(dfpulledNumbers)] = lspulledNumbers
        print(dfpulledNumbers)
        dfpulledNumbersStats = dfpulledNumbers.apply(pd.Series.value_counts)
        dfpulledNumbersStats['sum'] = dfpulledNumbersStats.sum(axis=1)
        
        plt.cla()
        plt.plot(dfpulledNumbersStats.index,dfpulledNumbersStats['sum'],label='Anzahl')
    
    dfpulledNumbers = pd.DataFrame(columns=['1','2','3','4','5','6'])
    lspulledNumbers = []
    dfPlayer = pd.DataFrame(columns=['Name','1','2','3','4','5','6','Gewinn','AnzGewinne'])

    y=0
    #Adjust Number of Players here
    while y < 1:
        dfnewPlayer = newPlayer()
        dfPlayer = pd.concat([dfPlayer,dfnewPlayer],ignore_index=True)
        y += 1
        
    print(dfPlayer)

    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.tight_layout()
    plt.show()

        
main()


