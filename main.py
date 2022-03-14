import pandas as pd
def main():

    def newPlayer():
        playername = input("Bitte Name eingeben: ")
        print(playername +" wurde erfasst.")
        return pd.DataFrame([[playername,enterNumbers(1),enterNumbers(2),enterNumbers(3),enterNumbers(4),enterNumbers(5),enterNumbers(6)]],columns=dfPlayer.columns)

    def enterNumbers(x):
        return int(input("Bitte " + str(x) + ". Zahl eingeben (zwischen 1 und 49): "))

    dfPlayer = pd.DataFrame(columns=['Name','Zahl_1','Zahl_2','Zahl_3','Zahl_4','Zahl_5','Zahl_6'])
    y=0
    while y < 2:
        dfnewPlayer = newPlayer()
        dfPlayer = pd.concat([dfPlayer,dfnewPlayer],ignore_index=True)
        y += 1
    print(dfPlayer)
    

main()


