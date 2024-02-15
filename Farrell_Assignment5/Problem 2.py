def resterauntV2():

    #initializers
    order = str(input("What is the order? (ex: 1 c 2 s 11 p)"))
    runningc = 0
    runnings = 0
    runningp = 0

    #while there is an order, continue

    while order != "":

        #initialize counter, split order into a list
        counter = 0
        order = order.split(" ") #(["2,c,2,s,11,p"])

        #For loop parses for c s and p and then records the number in the element before it
        for element in order:
            if order[counter] == "c":
                runningc = runningc +int(order[counter - 1])
            elif order[counter] == "s":
                runnings = runnings + int(order[counter -1])
            elif order[counter] == "p":
                runningp = runningp + int(order[counter -1])
            counter = counter +1

        #new order to continue loop
        order = str(input("What is the order? (ex: 1 c 2 s 11 p"))
        
    #print to user
    print("The resteraunt delivered {c} Caesar Salads, {s} sandwiches and {p} Pizzas".format(c=runningc,s=runnings,p=runningp))
resterauntV2()