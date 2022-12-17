import json

from meditations_text import meditations

meditations_book_1 = meditations["1"]
meditations_book_2 = meditations["2"]
meditations_book_3 = meditations["3"]
meditations_book_4 = meditations["4"]
meditations_book_5 = meditations["5"]
meditations_book_6 = meditations["6"]
meditations_book_7 = meditations["7"]
meditations_book_8 = meditations["8"]
meditations_book_9 = meditations["9"]
meditations_book_10 = meditations["10"]
meditations_book_11 = meditations["11"]
meditations_book_12 = meditations["12"]

#converts the book which is originally in a list, into a plain text string
def listtostring(s):
    str1 = ""
    return (str1.join(s))

def return_book(): 
    meditations_book_chosen = int(input("Which Book Would You Like to Search (1 to 12)?: "))
    if meditations_book_chosen == 1:
        print(listtostring(meditations_book_1))
    elif meditations_book_chosen == 2:
        print(listtostring(meditations_book_2))
    elif meditations_book_chosen == 3:
        print(listtostring(meditations_book_3))
    elif meditations_book_chosen == 4:
        print(listtostring(meditations_book_4))
    elif meditations_book_chosen == 5:
        print(listtostring(meditations_book_5))
    elif meditations_book_chosen == 6:
        print(listtostring(meditations_book_6))
    elif meditations_book_chosen == 7:
        print(listtostring(meditations_book_7))
    elif meditations_book_chosen == 8:
        print(listtostring(meditations_book_8))
    elif meditations_book_chosen == 9:
        print(listtostring(meditations_book_9))
    elif meditations_book_chosen == 10:
        print(listtostring(meditations_book_10))
    elif meditations_book_chosen == 11:
        print(listtostring(meditations_book_11))
    elif meditations_book_chosen == 12:
        print(listtostring(meditations_book_12))
    else:
        print("Meditations does not have that many books! Please try again.")

return_book()
