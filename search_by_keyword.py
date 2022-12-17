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
        for x in range(len(subchapters_with_keyword_1)):
            print("\n", subchapters_with_keyword_1[x], "\n")
    elif book == 2:
        for x in range(len(subchapters_with_keyword_2)):
            print("\n", subchapters_with_keyword_2[x], "\n")
    elif book == 3:
        for x in range(len(subchapters_with_keyword_3)):
            print("\n", subchapters_with_keyword_3[x], "\n")
    elif book == 4:
        for x in range(len(subchapters_with_keyword_4)):
            print("\n", subchapters_with_keyword_4[x], "\n")
    elif book == 5:
        for x in range(len(subchapters_with_keyword_5)):
            print("\n", subchapters_with_keyword_5[x], "\n")
    elif book == 6:
        for x in range(len(subchapters_with_keyword_6)):
            print("\n", subchapters_with_keyword_6[x], "\n")
    elif book == 7:
        for x in range(len(subchapters_with_keyword_7)):
            print("\n", subchapters_with_keyword_7[x], "\n")
    elif book == 8:
        for x in range(len(subchapters_with_keyword_8)):
            print("\n", subchapters_with_keyword_8[x], "\n")
    elif book == 9:
        for x in range(len(subchapters_with_keyword_9)):
            print("\n", subchapters_with_keyword_9[x], "\n")
    elif book == 10:
        for x in range(len(subchapters_with_keyword_10)):
            print("\n", subchapters_with_keyword_10[x], "\n")
    elif book == 11:
        for x in range(len(subchapters_with_keyword_11)):
            print("\n", subchapters_with_keyword_11[x], "\n")
    elif book == 12:
        for x in range(len(subchapters_with_keyword_12)):
            print("\n", subchapters_with_keyword_12[x], "\n")
    elif book == "13":
        for x in range(len(subchapters_with_keyword_all)):
            print("\n", subchapters_with_keyword_all[x], "\n")
