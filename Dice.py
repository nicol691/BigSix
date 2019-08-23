from random import randint

class Dice :
    def __init__(self) :
        self.numValue = 1

    def roll(self) :
        self.numValue = randint(1, 6)
        return self.numValue

    def value(self) :
        return self.numValue

    def __str__(self) :
        return str( self.numValue )
    
class Player :
    def __init__(self) :
        self.noChips = 5

    def adjustChips(self, adjust) :
        self.noChips = self.noChips + adjust
        return self.noChips

gameBoard = [ 0 ] * 6
dicecube = Dice()

# My program

print("Number of players: ")
noPlayers = int(input())

playerList = []
for i in range(noPlayers):
    playerList.append(Player())

currentChips = 1
while currentChips > 0:    
    for i in range(noPlayers):
        outcome = dicecube.roll()
        print("Player ", i+1)
        print("   rolled ", outcome)
        if outcome==6:
            gameBoard[5] = gameBoard[5] + 1
            currentChips = playerList[i].adjustChips(-1)
        else:
            if gameBoard[outcome-1]==0:
                gameBoard[outcome-1] = 1
                currentChips = playerList[i].adjustChips(-1)
            else:
                gameBoard[outcome-1] = 0
                currentChips = playerList[i].adjustChips(1)
            
        print("   has ", currentChips, " chips")
        if currentChips==0:
            print("CONGRATULATIONS YOU WON")
            break

    input()


    
