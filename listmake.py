from things import *

opt1 = 0
opt = 0
gnum = 0

while opt != 5:
    opt = int(input("What is the category of the item?\n1 = Groceries\n2 = Clothes\n3 = Books\n4 = Electronics\n5 = Finished "))

    if opt == 1:
        groceries.append(input("Item "))
    if opt == 2:
        clothes.append(input("Item "))
    if opt == 3:
        books.append(input("Item "))
    if opt == 4:
        electronics.append(input("Item "))

betterListPrintG(groceries)
betterListPrintC(clothes)
betterListPrintB(books)
betterListPrintE(electronics)
while opt1 != 2:
    opt1 = int(input("Do you want to remove anything?\n1 for yes\n2 for no "))

    if opt1 ==1:
        deleteItems()

groceries.sort()
clothes.sort()
books.sort()
electronics.sort()

betterListPrintG(groceries)
betterListPrintC(clothes)
betterListPrintB(books)
betterListPrintE(electronics)