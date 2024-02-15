def interestDouble():

    #program will use a while loop to determine time for investment to double at given interest
    #input is yearly interest rate and initial investment, output is amount of years for double

    #initializers
    runningYears = 0
    investment = float(input("What is the initial investment?"))
    rate = int(input("What is the interest rate percentage? (ex: 5)"))/100
    runningTotal = investment

    #loop runs until the running total is bigger than 2 times the investment
    while runningTotal < (2 * investment):
        #document last total + new accured interest
        runningTotal = runningTotal + (runningTotal * rate)
        #count years
        runningYears = runningYears + 1

    #output result to user
    print("It will take "+str(runningYears)+" years for "+str(investment)+" to double at the interest rate "+str(rate*100)+"%")

interestDouble()