# questions for quiz game in a dictionary format

name = input("What's your name? ")

# a nice function that provides lower case letters which I have used to number the question options (a,b,c,d instead of (1,2,3,4).
from string import ascii_lowercase


questions = { 
    "What was Marcus Aurelius' occupation": [ "Emperor", "Slavemaster", "Financier", "Artisan"
    ],
    "Which school of philosphy is Marcus Aurelius famous in": [ "Stoicism", "Epicureanism", "Skepticism", "Buddhism"
    ],
    "What is the modern name of the country in which Marcus Aurelius was born": [ "Italy", "Spain", "Nigeria", "Portugal"
    ],


}

# lists question and answer options 

for num, (question, alt_answers) in enumerate(questions.items(), start=1):
    print(f"\nQuestion {num}")
    # prints the question with a question mark so I do not have to remember to put them in when I make the question lol
    print(f"{question}?")
    correct_answer = alt_answers[0]
    numbered_answers = dict(zip(ascii_lowercase, sorted_alt))
    # sorted() changes the answer order (orders alphabetically to shuffle the order)
    sorted_alt = sorted(alt_answers)
    # add a number for each question option (iterates through the for loop and number each option)
    for number, alternative in enumerate(sorted_alt):
        print(f" {number}) {alternative}")
    # takes user input as an integer
    answer_number = int(input(f"{question}? "))
    answer = sorted_alt[answer_number]
    if answer == correct_answer:
        print("Correct - Great job!")
    else:
        print(f"The answer is {correct_answer}, not {answer!r}. Good Try!")
