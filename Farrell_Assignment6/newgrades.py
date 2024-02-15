def grades():

#open file
    with open("grades.txt", "r") as file:

        #initializers
        i= 0 #counter
        gradelist = [] # initialize to append grades into
        line = file.readline()

# 1)splits our list into each name/grade pair 2)into just one pair 3) index the number 4) adds the grade to gradelist
        while line:
                gradesplit = line.strip().split(",")
                namesplit = gradesplit[0]
                gradelist.append(gradesplit[1])
                line = file.readline()

#sort gradelist smallest to largest
        n = len(gradelist)
        i = 0 # reset counter to one (starting at 0 for current so skip 0)
        for i in range(n):
            #last element falls in place so -1
            for h in range(0,(n-1)):
                #swap if bigger
                if int(gradelist[h]) > int(gradelist[h+1]):
                    gradelist[h], gradelist[h + 1] = gradelist[h + 1], gradelist[h]

# print to user
        i = 0 #reset counter
        for elem in gradelist:
            print(gradelist[i])
            i=i+1

grades()