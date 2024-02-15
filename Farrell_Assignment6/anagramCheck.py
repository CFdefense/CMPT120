def anagramCheck():

    #take in two words or phrases

    Input1 = (input("Enter the First Word or Phrase"))
    Input2 = (input("Enter the Second Word or Phrase"))

    # for both, 1) remove spaces 2) lower case 3) sort

    Input1sorted = sorted(list(Input1.replace(" ","").lower()))
    Input2sorted = sorted(list(Input2.replace(" ","").lower()))

    # check if one input is an anagram of the other by comparing our new sorted lists

    if Input1sorted == Input2sorted:

        print(Input1+" and "+Input2+" are anagrams")
    else:

        print(Input1+" and "+Input2+" are NOT anagrams")



anagramCheck()
