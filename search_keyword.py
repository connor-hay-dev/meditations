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

# User input, which book they want to search for.
meditations_book_to_search = input(
    "Which book would you like to search? (1 - 12, or 13 to search all the books.): ")

# allows user to search by book number
meditations_book_to_search_num_int = int(meditations_book_to_search)

substring = input("What topic do you want to search for?: ")

# Searches for keywords with all the criteria of the above formatting.
subchapters_with_keyword_1 = [
    string for string in meditations_book_1 if substring in string]
subchapters_with_keyword_2 = [
    string for string in meditations_book_2 if substring in string]
subchapters_with_keyword_3 = [
    string for string in meditations_book_3 if substring in string]
subchapters_with_keyword_4 = [
    string for string in meditations_book_4 if substring in string]
subchapters_with_keyword_5 = [
    string for string in meditations_book_5 if substring in string]
subchapters_with_keyword_6 = [
    string for string in meditations_book_6 if substring in string]
subchapters_with_keyword_7 = [
    string for string in meditations_book_7 if substring in string]
subchapters_with_keyword_8 = [
    string for string in meditations_book_8 if substring in string]
subchapters_with_keyword_9 = [
    string for string in meditations_book_9 if substring in string]
subchapters_with_keyword_10 = [
    string for string in meditations_book_10 if substring in string]
subchapters_with_keyword_11 = [
    string for string in meditations_book_11 if substring in string]
subchapters_with_keyword_12 = [
    string for string in meditations_book_12 if substring in string]
subchapters_with_keyword_all = [
    string for string in meditations_full if substring in string]

# Returns passages only from the book the user has chosen. 13 is a placeholder for all books.


def return_keyword_passages():
    if meditations_book_to_search_num_int == 1:
        return (subchapters_with_keyword_1)
    elif meditations_book_to_search_num_int == 2:
        return (subchapters_with_keyword_2)
    elif meditations_book_to_search_num_int == 3:
        return (subchapters_with_keyword_3)
    elif meditations_book_to_search_num_int == 4:
        return (subchapters_with_keyword_4)
    elif meditations_book_to_search_num_int == 5:
        return (subchapters_with_keyword_5)
    elif meditations_book_to_search_num_int == 6:
        return (subchapters_with_keyword_6)
    elif meditations_book_to_search_num_int == 7:
        return (subchapters_with_keyword_7)
    elif meditations_book_to_search_num_int == 8:
        return (subchapters_with_keyword_8)
    elif meditations_book_to_search_num_int == 9:
        return (subchapters_with_keyword_9)
    elif meditations_book_to_search_num_int == 10:
        return (subchapters_with_keyword_10)
    elif meditations_book_to_search_num_int == 11:
        return (subchapters_with_keyword_11)
    elif meditations_book_to_search_num_int == 12:
        return (subchapters_with_keyword_12)
    elif meditations_book_to_search_num_int == 13:
        return (subchapters_with_keyword_all)
    else:
        print("That is a not a book in Meditations. Please try again!")


# returns the output of the list and seperates each list item into its own, seperate paragraph. Improves legibility a lot!
# loops through the outputs and inserts a blank link before and after each output.

def return_with_space_between_each_output():
    if return_keyword_passages() == subchapters_with_keyword_1:
        for x in range(len(subchapters_with_keyword_1)):
            print("\n", subchapters_with_keyword_1[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_2:
        for x in range(len(subchapters_with_keyword_2)):
            print("\n", subchapters_with_keyword_2[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_3:
        for x in range(len(subchapters_with_keyword_3)):
            print("\n", subchapters_with_keyword_3[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_4:
        for x in range(len(subchapters_with_keyword_4)):
            print("\n", subchapters_with_keyword_4[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_5:
        for x in range(len(subchapters_with_keyword_5)):
            print("\n", subchapters_with_keyword_5[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_6:
        for x in range(len(subchapters_with_keyword_6)):
            print("\n", subchapters_with_keyword_6[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_7:
        for x in range(len(subchapters_with_keyword_7)):
            print("\n", subchapters_with_keyword_7[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_8:
        for x in range(len(subchapters_with_keyword_8)):
            print("\n", subchapters_with_keyword_8[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_9:
        for x in range(len(subchapters_with_keyword_9)):
            print("\n", subchapters_with_keyword_9[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_10:
        for x in range(len(subchapters_with_keyword_10)):
            print("\n", subchapters_with_keyword_10[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_11:
        for x in range(len(subchapters_with_keyword_11)):
            print("\n", subchapters_with_keyword_11[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_12:
        for x in range(len(subchapters_with_keyword_12)):
            print("\n", subchapters_with_keyword_12[x], "\n")
    elif return_keyword_passages() == subchapters_with_keyword_all:
        for x in range(len(subchapters_with_keyword_all)):
            print("\n", subchapters_with_keyword_all[x], "\n")


return_with_space_between_each_output()
