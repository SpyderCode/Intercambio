from Names import Names
from Email import Email
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def intercambio():
    emails=Names.getEmails()
    names=destination=Names.getNames()
    #print(names)
    print("Randomizing destination")
    destination=Names.RandomizeDest(destination)
    print("Destination Randomized")

    IntercambioList=[]
    for name,destiny in zip(names,destination):
        exchange=name+" Tu intercambio es:  "+destiny
        IntercambioList.append(exchange)

    for correo,mensaje in zip(emails,IntercambioList):
        #Email.SendEmail(emails[1],IntercambioList[1])
        Email.SendEmail(correo,mensaje)

    print("DONE")







if __name__ == '__main__':
    intercambio()

