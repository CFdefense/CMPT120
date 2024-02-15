def main():
    #main function reads an input string, then calls reverse(), then compare reverse to original

    Input = (str(input("Please enter a word, number or phrase")))
    Reversed = reverse(Input)

    #Test if palindrome

    if (Input==Reversed):
        print("PALINDROME!")
    else:
        print("Not palindrome :(")

    #reverse function which reverses a string using a loop
def reverse(string):
    output= []
    accumulator=-1
    for char in (string):
        output.append(string[accumulator])
        accumulator = accumulator-1
    output = ("").join(output)
    return(output)

main()