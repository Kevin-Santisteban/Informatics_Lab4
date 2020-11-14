
import re


regularExpression = "([0|1][0-9]|2[0-3]):(([0-5]?[0-9]))?:?(([0-5]?[0-9]))?"

def replaceMatches(inputText, replacingText):
    print(re.sub(regularExpression, replacingText,inputText))


def main ():
    inputText = open("lab4Tests/test5.txt", "r", encoding="utf-8").read()
    

    print("\nInput************************************************************************ \n")
    print(inputText)
    print("*****************************************************************************\n")
    

    print("Output*********************************************************************** \n")
    replaceMatches(inputText, "(TBD)")
    print("*****************************************************************************")
    

if __name__ == "__main__":
    main()


