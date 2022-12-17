import json

from meditations_text import meditations

import os 

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

meditations_full = meditations_book_1 + meditations_book_2 + meditations_book_3 + meditations_book_4 + meditations_book_5 + meditations_book_6 + \
    meditations_book_7 + meditations_book_8 + meditations_book_9 + \
    meditations_book_10 + meditations_book_11 + meditations_book_12

    

def search_book_for_string():
    book = int(input("Which book would you like to search? (1 - 12, or 13 to search all the books.): "))
    substring = input("What topic would you like to search for?: ")
    subchapters_with_keyword_1 = [string for string in meditations_book_1 if substring in string]
    subchapters_with_keyword_2 = [string for string in meditations_book_2 if substring in string]
    subchapters_with_keyword_3 = [string for string in meditations_book_3 if substring in string]
    subchapters_with_keyword_4 = [string for string in meditations_book_4 if substring in string]
    subchapters_with_keyword_5 = [string for string in meditations_book_5 if substring in string]
    subchapters_with_keyword_6 = [string for string in meditations_book_6 if substring in string]
    subchapters_with_keyword_7 = [string for string in meditations_book_7 if substring in string]
    subchapters_with_keyword_8 = [string for string in meditations_book_8 if substring in string]
    subchapters_with_keyword_9 = [string for string in meditations_book_9 if substring in string]
    subchapters_with_keyword_10 = [string for string in meditations_book_10 if substring in string]
    subchapters_with_keyword_11 = [string for string in meditations_book_11 if substring in string]
    subchapters_with_keyword_12 = [string for string in meditations_book_12 if substring in string]
    subchapters_with_keyword_all = [string for string in meditations_full if substring in string]
    if book == 1:
        if len(subchapters_with_keyword_1) > 0:
            for x in range(len(subchapters_with_keyword_1)):
                print("\n", subchapters_with_keyword_1[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 1. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 2:
        if len(subchapters_with_keyword_2) > 0:
            for x in range(len(subchapters_with_keyword_2)):
                print("\n", subchapters_with_keyword_2[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 2. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 3:
        if len(subchapters_with_keyword_3) > 0:
            for x in range(len(subchapters_with_keyword_3)):
                print("\n", subchapters_with_keyword_3[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 3. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 4:
        if len(subchapters_with_keyword_4) > 0:
            for x in range(len(subchapters_with_keyword_4)):
                print("\n", subchapters_with_keyword_4[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 4. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 5:
        if len(subchapters_with_keyword_5) > 0:
            for x in range(len(subchapters_with_keyword_5)):
                print("\n", subchapters_with_keyword_5[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 5. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 6:
        if len(subchapters_with_keyword_6) > 0:
            for x in range(len(subchapters_with_keyword_6)):
                print("\n", subchapters_with_keyword_6[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 1. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 7:
        if len(subchapters_with_keyword_7) > 0:
            for x in range(len(subchapters_with_keyword_7)):
                print("\n", subchapters_with_keyword_7[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 7. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 8:
        if len(subchapters_with_keyword_8) > 0:
            for x in range(len(subchapters_with_keyword_8)):
                print("\n", subchapters_with_keyword_8[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 8. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 9:
        if len(subchapters_with_keyword_9) > 0:
            for x in range(len(subchapters_with_keyword_9)):
                print("\n", subchapters_with_keyword_9[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 9. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 10:
        if len(subchapters_with_keyword_10) > 0:
            for x in range(len(subchapters_with_keyword_10)):
                print("\n", subchapters_with_keyword_10[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 10. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 11:
        if len(subchapters_with_keyword_11) > 0:
            for x in range(len(subchapters_with_keyword_11)):
                print("\n", subchapters_with_keyword_11[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 11. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 12:
        if len(subchapters_with_keyword_12) > 0:
            for x in range(len(subchapters_with_keyword_12)):
                print("\n", subchapters_with_keyword_12[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in Meditations Book 12. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')
    elif book == 13:
        if len(subchapters_with_keyword_all) > 0:
            for x in range(len(subchapters_with_keyword_all)):
                print("\n", subchapters_with_keyword_all[x], "\n")
        else:
            next_step = input("That key word does not seem to exist in any of the Meditations Books. Do you want to try another word? (Y/N) :")
            if next_step == "Y":
                search_book_for_string()
            elif next_step == "y":
                search_book_for_string()
            elif next_step == "N":
                os.system('cls||clear')
            elif next_step == "n":
                os.system('cls||clear')

search_book_for_string()
