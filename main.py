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
        plt.bar(dfpulledNumbersStats.index,dfpulledNumbersStats['sum'],tick_label=dfpulledNumbersStats.index)
        plt.ylabel('# Häufigkeit')
        ymax= int(max(dfpulledNumbersStats['sum']))
        xmax= dfpulledNumbersStats[dfpulledNumbersStats['sum']==ymax].index.values
        plt.title('Verteilung gezogener Zahlen // Häufigste Zahl ' + str(xmax[0]))
        

    
    dfpulledNumbers = pd.DataFrame(columns=['1','2','3','4','5','6'])
    lspulledNumbers = []
    dfPlayer = pd.DataFrame(columns=['Name','1','2','3','4','5','6','Gewinn','AnzGewinne'])

    intPlayerNumber = int(input("Bitte Anzahl der Spieler*innen eingeben: "))
    y=0
    while y < intPlayerNumber:
        dfnewPlayer = newPlayer()
        dfPlayer = pd.concat([dfPlayer,dfnewPlayer],ignore_index=True)
        y += 1

    ani = FuncAnimation(plt.gcf(), animate, interval=1)
    plt.tight_layout()
    plt.show()

        
main()


