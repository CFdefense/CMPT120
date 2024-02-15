def babyBill():

    # input from user of start and end times
    startTime = str(input("What time did the session start? (00:00)")) #17:00
    endTime = str(input("What time did the session end? (00:00)")) #21:30

    splitStart = startTime.split(":") #[17,00]
    splitEnd = endTime.split(":") #[21,.30]

    # check to see if the correct start time has been entered, then convert incorrect start time into correct start time
    while float(splitStart[0]) > 24.0 or float(splitStart[1]) > 60.0:
        print("Invalid time format. Please provide the correct time (e.g., 17:00)")
        startTime = input("What time did the session start? (00:00)")
        splitStart = startTime.split(":")

    # convert times into
    startValue = ((float(splitStart[0])) * 60) + float(splitStart[1]) #1020
    endValue = ((float(splitEnd[0])) * 60) + float(splitEnd[1]) #1290

    # check to see if the babysitter worked past the 9 pm cutoff, if so calculate the times at the different rates then add
    # Else we just find the difference between the end and start and multiply it by the rate of $5 an hour
    if endValue >= 1260.0:
        payafter9 = (endValue - 1260) * .04166
        paybefore9 = ((1260-startValue)) * .0833
        totalexpense = round((paybefore9 + payafter9),2)
    else:
        totalexpense = round(((endValue - startValue) * .0833),2)

    print("The baby sitting bill is $"+(str(totalexpense))+".")

babyBill()