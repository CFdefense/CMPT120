def UserGenerator():

    #Initializers

    names = []
    emailResults = []
    Seperate = ""
    running = 0

    #Request total number of usernames to generate

    totalEmails = int(input("How many Emails would you like to generate?"))

    #Collect names in a list

    for loop in range(totalEmails):
        currentName = str(input("Enter a name"))
        names.append(currentName)


    #Convert each list name into an email and print to user

    for loop in range(totalEmails):
        Seperate = names[running]
        firstName = (Seperate[0:1]).lower()
        lastName = ((((Seperate.split(" "))[1])[0:10])).lower()
        Index = (running) + 1
        print((firstName + lastName + str(Index)) + ("@marist.edu"))
        running = running + 1






UserGenerator()
