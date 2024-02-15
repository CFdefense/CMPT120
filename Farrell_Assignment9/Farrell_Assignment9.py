from random import *
class Deck:
    def __init__(self):
        #create deck of cards calling card class
        listsuit = ["Clubs","Diamonds","Hearts","Spades"]
        listnums = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.listofcards = []
        for suit in listsuit:
            for num in listnums:
                card = Card(suit,num)
                self.listofcards.append(card)
    def dealCard(self):
        suit,num = self.listofcards[0].dealcard()
        del self.listofcards[0]
        return(suit,num)

    def cardsLeft(self):
        return(len(self.listofcards))

    def Shuffle(self):
        shuffle(self.listofcards)

    def getNumericValue(self):
        #get info about the top card
        suit, num = self.listofcards[0].dealcard()
        if num == "Ace": value = 1
        elif num == "Jack": value = 11
        elif num == "Queen": value = 12
        elif num == "King": value = 13
        else: value =  int(num)
        return(value)
class Card:
    #creates the card and holds the values inputted
    def __init__(self,suit,num):
        self.suit = suit
        self.num = num

    #returns its suit and name
    def dealcard(self):
        return(self.suit,self.num)


def main():

    decks = []
    #create the decks and store in the list
    for i in range(10):
        deck = Deck()
        deck.Shuffle()
        decks.append(deck)

    #sort them by greatest numeric value first (using selection sort)



    #set new minimum everytime
    max = len(decks)
    for i in range(max):
        min = 0
        #go through the rest of the list everytime
        for j in range(i+1,max):
            if decks[j].getNumericValue() > decks[i].getNumericValue():
                decks[j],decks[i] = decks[i],decks[j]

    #to test to see theyre sorted correctly
    for x in range(len(decks)):
        print(decks[x].getNumericValue())

main()
