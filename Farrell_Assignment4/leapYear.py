def leapYear():
    daysnum = [31,28,31,30,31,30,31,31,30,31,30,31]
    date = str(input("What is the Date? 00/00/0000"))
    splitDate = date.split("/") #[00,00,0000]

    #test if input is valid
    while (int(splitDate[0])> 12) or (int(splitDate[1]) > daysnum[int(splitDate[0])]):
        newdate = str(input("Incorrect date input, What is the Date? 00/00/0000"))
        date = newdate
        splitDate = date.split("/") #[00,00,0000]

    #test to see if leap year
    if int(splitDate[2]) % 400 == 0  or int(splitDate[2]) % 4 == 0 and int(splitDate[2]) % 100 != 0:
        print("Leap year")

    else:
        print("Not a Leap Year")

leapYear()