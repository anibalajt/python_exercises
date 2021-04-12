'''
  2.	Write a program that allows the user to navigate the lines of
  text in a file. The program should prompt the user for a filename
  and input the lines of text into a list. The program then enters a
  loop in which it prints the number of lines in the file and
  prompts the user for a line number. Actual line numbers range
  from 1 to the number of lines in the file. If the input is 0,
  the program quits. Otherwise, the program prints the line
  associated with that number.
'''

# function to open the file and read its content
def readFile(nameFile):
    try:
        reader = open(nameFile+".txt", "r")
        file_content = reader.readlines()
        return file_content
        # Further file processing goes here
    except:
        return False


def userInput(firstRun, nameFile, lenFile):
    nLine = 0
    while True:
        try:
            # firt run
            if(firstRun):
                firstRun = False
                print(f"{nameFile} has {lenFile} lines")
                nLine = int(input("Enter the line you want to see: "))
            else:  # display a different message after the first run
                nLine = int(
                    input(f"desea ver otra linea, enter line number 1 - {lenFile}: "))
            # If the number entered by the user is greater than the lines in the file, we ask for a new number
            if(nLine > lenFile):
                continue
        except ValueError:
            # If the user does not enter a number, we ask him again to enter a number
            print("Enter a number")
            continue
        else:
            return nLine
            break


def main():
    firstRun = True
    nameFile = input("Enter file name without extension: ")
    file_content = readFile(nameFile)
    nLine = 1
    # loop to see each line until user type 0
    if(file_content):
        while nLine != 0:
            nLine = userInput(firstRun, nameFile, len(file_content))
            # if nline equal to 0 break the loop
            if(nLine == 0):
                break
            # prints the line chosen by the user
            print(f"Line {nLine} is: {file_content[nLine-1]}")
    else:
        print("File doesn't exist\n")

    print("\nthe program is over")


main()
