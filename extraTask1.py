
import re


regularExpression = "(\w+\s){5,5}\w+[.?!]"


   
def main ():
    inputText = open("RomeoAndJuliet.txt", "r", encoding="utf-8").read()

    matchList = re.findall(regularExpression, inputText)
    if (len(matchList) > 0):
         for match in matchList:
             print(match)







if __name__ == "__main__":
    main()




