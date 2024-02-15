def readGrade():

    # (A: >= 90 /B:80-89 /C:70-79 /D: 60-69 /F: < 60).
    #Read files

    gradesFile = open("grades.txt","r")
    namesFile = open("students.txt","r")
    accumulator = 0
    #Convert to lists
    
    NAMES = (namesFile.read()).splitlines()
    GRADES = (gradesFile.read()).splitlines()

    #for loop will run through students and grades, determine letter grade and print

    for x in NAMES:
        #find current name and current set of grades, reset counters to 0
        currentname = NAMES[accumulator]
        gradeaccumulator = 0
        runningtotal = 0
        currentgrade = (GRADES[accumulator]).split(",")
        accumulator=accumulator+1

        #calculate average grade
        for grade in list(currentgrade):

            runningtotal = runningtotal + int(currentgrade[gradeaccumulator])
            gradeaccumulator=gradeaccumulator+1

        averagegrade = runningtotal / len(currentgrade)

        #find which average grade fits the grade mark
        if averagegrade >= 90:
            mark = "A"
        elif averagegrade >=80:
            mark = "B"
        elif averagegrade >=70:
            mark = "C"
        elif averagegrade >= 60:
            mark = "D"
        elif averagegrade < 60:
            mark = "F"
        print(str(currentname)+","+str(mark))
    #close files
    gradesFile.close()
    namesFile.close()
readGrade()