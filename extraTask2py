
import re

# Alpha.Beta_Theta@gamma.ru
# Ivan_Petrov@yandex.com
# Anna.Wolf@gmail.com
# Big_Compayny.A@mail.ru
# Il.cane@yahoo.com

emailList = ["Alpha.Beta_Theta@gamma.ru", 
            "Ivan_Petrov@yandex.com",
            "Anna.Wolf@gmail.",
            "Big_Compayny.A@mail.ru",
            "Il.cane@yahoo.com"]

emailregularExpression = "[a-zA-Z\d\.\_]+@[a-zA-Z]+\.(ru|com|net)"

def verifyEmailAdress(emailAdress):
    
    if (re.search(emailregularExpression,emailAdress)):
        domain = emailAdress.split("@")[1]
        print(domain)
    else:
        print("Fail!")

def main ():

    for email in emailList:
        print(email)

    print("-----------------------------------------")
    for email in emailList:
        verifyEmailAdress(email)
    

if __name__ == "__main__":
    main()




