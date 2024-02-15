
def Utensils():

    #Initializers

    partyTotals = []
    listOfseated = []
    seatedRunning = 0

    #Inquire amount of groups from user
    numberOfgroups = int(input("How many groups are coming today?"))

    #Inquire amount of people per group from 'waiter' and store in list
    for x in range(numberOfgroups):
        tempInt = int(input("Group"+str(x+1)+" Has left, how many people were seated? (1-4)"))
        partyTotals.append(tempInt)

    #Calculate the total unused utensils and create list of party sizes
    for x in partyTotals:

        listOfseated.append(partyTotals[x])
        seatedRunning = seatedRunning + (4-partyTotals[x])

    #calculate amount of tables that could have been seated and print final statement

    remainingUtensils = seatedRunning // 4
    print("The restaurant had "+(str(numberOfgroups))+" parties and their sizes are"+(str(listOfseated))+". if unused utensil packs had not been sent to wash, the restaurant would have had been able to attend "+(str(remainingUtensils))+" more tables")

Utensils()