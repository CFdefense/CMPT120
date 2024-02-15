from random import *
class Deck:

    def __init__(self):
        """ Creates a standard deck of cards"""
        self.standardDeck = [
        '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts',
        '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds',
        '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs',
        '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades' ]

    def Shuffle(self):
        """ shuffles the deck"""
        shuffle(self.standardDeck)
        return self.standardDeck

    def dealCard(self,currentdeck, n):
        """return the first card in the deck"""
        i = 0
        listofCards = []
        while i < n:
            dealtcard = self.standardDeck[0]
            del self.standardDeck[0]
            listofCards.append(dealtcard)
            i+=1
        return(listofCards)

    def cardsLeft(self):
        """find total elements remaining in the string"""
        if len(self.standardDeck) != 0:
            return(str(len(self.standardDeck))+" Cards left")
        else:
            return("Deck is Empty")


def main():

    #main used to test the program and its methods
    currentdeck = Deck()
    userResponse = str(input("Welcome, would you like to shuffle, deal a card, check the remaining number of cards in the deck, or exit?"))

    while userResponse[0].lower() != "e":

        if userResponse[0].lower() == "s":

            currentdeck.Shuffle()
            print("deck has been shuffled")

        elif userResponse[0].lower() == "d":

            n = int(input("How many cards would you like to deal?"))
            dealtcards = currentdeck.dealCard(currentdeck,n)
            print(dealtcards)

        elif userResponse[0].lower() == "c":
            check = currentdeck.cardsLeft()
            print(check)

        userResponse = str(input("Welcome, would you like to shuffle, deal a card, check the remaining number of cards in the deck, or exit?"))

main()