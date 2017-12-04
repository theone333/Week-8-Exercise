def main():

    userInput = input("Enter a string: ")
   
    print(" there are ", count_spaces(userInput) )

def count_spaces(string):
   
    spaces = 0
    for char in string:
        if char == " " :
            spaces = spaces + 1

            
    return spaces


main()
