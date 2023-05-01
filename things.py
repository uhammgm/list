def betterListPrintG(list):
    NLS = ""
    for item in list:
        NLS += str(item) + "\n"
    print("~Groceries~\n" + NLS)

def betterListPrintB(list):
    NLS = ""
    for item in list:
        NLS += str(item) + "\n"
    print("~Books~\n" + NLS)

def betterListPrintE(list):
    NLS = ""
    for item in list:
        NLS += str(item) + "\n"
    print("~Electronics~\n" + NLS)

def betterListPrintC(list):
    NLS = ""
    for item in list:
        NLS += str(item) + "\n"
    print("~Clothes~\n" + NLS)

def deleteItems():
    DelOpt = input("What category do you want to delete the item from?\n1 = Groceries\n2 = Clothes\n3 = Books\n4 = Electronics")
    if DelOpt == 1: 
        