from locale import normalize
import pandas as pd
from random import randint, sample, shuffle
from random import seed
import matplotlib.pyplot as plt

def main():

    def newPlayer():
        playername = input("Bitte Name eingeben: ")
        print(playername +" wurde erfasst.")
        return pd.DataFrame([[playername,enterNumbers(1),enterNumbers(2),enterNumbers(3),enterNumbers(4),enterNumbers(5),enterNumbers(6),0,0]],columns=dfPlayer.columns)

    def enterNumbers(x):
        return int(input("Bitte " + str(x) + ". Zahl eingeben (zwischen 1 und 49): "))

    def randNumber():
        return randint(1,49)

    dfPlayer = pd.DataFrame(columns=['Name','1','2','3','4','5','6','Gewinn','AnzGewinne'])
    y=0
    #Adjust Number of Players here
    while y < 1:
        dfnewPlayer = newPlayer()
        dfPlayer = pd.concat([dfPlayer,dfnewPlayer],ignore_index=True)
        y += 1
    print(dfPlayer)

    dfpulledNumbers = pd.DataFrame(columns=['1','2','3','4','5','6'])
    y = 0
    while y < 9:
        dfpulledNumbers = pd.concat([pd.DataFrame([[randNumber(),randNumber(),randNumber(),randNumber(),randNumber(),randNumber()]],columns=dfpulledNumbers.columns),dfpulledNumbers],ignore_index=True)
        y += 1

    dfpulledNumbersStats = dfpulledNumbers.apply(pd.Series.value_counts)
    dfpulledNumbersStats['sum'] = dfpulledNumbersStats.sum(axis=1)
    print(dfpulledNumbersStats)

main()


