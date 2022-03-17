from locale import normalize
import pandas as pd
from random import randint, sample, shuffle
from random import seed
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from itertools import count


def main():

    plt.rcParams["figure.autolayout"] = True

    def newPlayer():
        playername = input("Bitte Name eingeben: ")
        print(playername +" wurde erfasst.")
        return pd.DataFrame([[playername,enterNumbers(1),enterNumbers(2),enterNumbers(3),enterNumbers(4),enterNumbers(5),enterNumbers(6),0,0,0,0,0,0,0,0]],columns=dfPlayer.columns)

    def enterNumbers(x):
        return int(input("Bitte " + str(x) + ". Zahl eingeben (zwischen 1 und 49): "))

    def randNumber():
        return randint(1,49)

    def pullNumbers():
        return [randNumber(),randNumber(),randNumber(),randNumber(),randNumber(),randNumber()]

    def checkNumbers(lspulledNumbers):
        for index, row in dfPlayer.iterrows():
            x=1
            intGuessedNumbers = 0
            while x < 7:
                if lspulledNumbers[x-1] == dfPlayer.at[index,str(x)]:
                    intGuessedNumbers += 1
                x+=1
            if intGuessedNumbers > 0:
                dfPlayer.at[index,str(intGuessedNumbers)+'er'] = dfPlayer.at[index,str(intGuessedNumbers)+'er'] + 1
        

    index = count()
    
    def animate(i):
        lspulledNumbers = pullNumbers()
        dfpulledNumbers.loc[len(dfpulledNumbers)] = lspulledNumbers
        dfpulledNumbersStats = dfpulledNumbers.apply(pd.Series.value_counts)
        dfpulledNumbersStats['sum'] = dfpulledNumbersStats.sum(axis=1)
        checkNumbers(lspulledNumbers)
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.bar(dfpulledNumbersStats.index,dfpulledNumbersStats['sum'],tick_label=dfpulledNumbersStats.index,color='blue')
        plt.ylabel('# Häufigkeit')
        ymax= int(max(dfpulledNumbersStats['sum']))
        xmax= dfpulledNumbersStats[dfpulledNumbersStats['sum']==ymax].index.values
        plt.title(str(dfpulledNumbers.size) + ' gezogene Zahlen // Häufigste Zahl ' + str(xmax[0]))
        plt.subplot(2, 1, 2)
        plt.cla()
        plt.table(cellText=dfPlayer.values,colLabels=dfPlayer.columns, loc='center')
        plt.axis('off')
        

    dfpulledNumbers = pd.DataFrame(columns=['1','2','3','4','5','6'])
    lspulledNumbers = []
    dfPlayer = pd.DataFrame(columns=['Name','1','2','3','4','5','6','Gewinn','AnzGewinne','1er','2er','3er','4er','5er','6er'])

    intPlayerNumber = int(input("Bitte Anzahl der Spieler*innen eingeben: "))
    y=0
    while y < intPlayerNumber:
        dfnewPlayer = newPlayer()
        dfPlayer = pd.concat([dfPlayer,dfnewPlayer],ignore_index=True)
        y += 1
        
    fig = plt.figure(figsize=(12,5))
    ani = FuncAnimation(plt.gcf(), animate, interval=1)
    plt.tight_layout()
    plt.show()

        
main()


