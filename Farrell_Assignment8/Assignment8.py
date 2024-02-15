import time
def main():

    #read file and get input from user
    File = open("dictionaryWords.txt","r").read().splitlines() #list of all words
    inputSentence = str(input("Type a Sentence")) #Input


    #filter the input sentence so words can be compared
    inputSentence = inputSentence.split(" ") #split into list at the spaces
    filteredlist = [] #new list of filtered words
    remove =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
                 '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','1','2','3','4','5','6','7','8','9','0'] #characters to be remove
    for word in inputSentence:  # loops through all elements in the list of words
        filteredword = ''
        # joins each character if the character is not in the remove list
        for char in word:
            if char not in remove:
                filteredword +=char.lower()

        filteredlist.append(filteredword)  # put filtered word in filter list

    #loop through each word and spellcheck using both methods - note misspelled words and time it took to complete

    # using linear search
    misspelledlinear = []
    startlinear = time.time()
    for search in filteredlist: # iterate through our sentence list
        if search not in File:
            misspelledlinear.append(search)
    endlinear = time.time()
    lineartime = endlinear-startlinear

    # print any mistakes found
    if misspelledlinear == []:
        print("Linear Found No Mistakes")
    else:
        print(misspelledlinear)

    # using binary search
    misspelledbinary = []
    startbinary = time.time()
    for search in filteredlist:
        low = 0
        high = len(File) -1
        found = False
        while low <= high:
            mid = (low+high)//2 #find middle
            item = File[mid]
            if search == item:
                found = True
                break
            elif search < item:
                high = mid -1
            else:
                low = mid +1
        if found == False:
            misspelledbinary.append(search)
    endbinary = time.time()
    binarytime = endbinary-startbinary

    # print any mistakes found
    if misspelledbinary == []:
        print("Binary Found No Mistakes")
    else:
        print(misspelledbinary)

    # print which was faster
    if binarytime == lineartime:
        print("Both methods took", binarytime)
    elif binarytime < lineartime:
        print("Binary Method was faster and took",binarytime,"seconds")
    elif binarytime > lineartime:
        print("Linear Method was faster and took",lineartime,"seconds")
main()