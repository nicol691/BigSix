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

# My program

dice1 = Dice()
print("dice1 value: ", dice1)
dice1.roll()
print("dice1 value: ", dice1)


    
