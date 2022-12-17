import random

# a nice function that provides lower case letters which I have used to number the question options (a,b,c,d instead of (1,2,3,4).
from string import ascii_lowercase

number_of_questions_per_quiz = 5

quiz_questions = { 
    "What was Marcus Aurelius' occupation": [ "Emperor", "Slavemaster", "Financier", "Artisan"
    ],
    "Which school of philosphy is Marcus Aurelius famous in": [ "Stoicism", "Epicureanism", "Skepticism", "Buddhism"
    ],
    "What is the modern name of the country in which Marcus Aurelius was born": [ "Italy", "Spain", "Nigeria", "Portugal"
    ],
    "How many books is Marcus Aurelius' meditations comprised of?: ": [ "12", "20", "15", "200"
    ],
    "Fill in the blank word in the following quote: \"Everything suits me that suits your ____, oh my universe.\"": [ "designs", "plans", "schemes", "desires"
    ]
}

number_of_questions = min(number_of_questions_per_quiz, len(quiz_questions))
questions = random.sample(list(quiz_questions.items()), k=number_of_questions_per_quiz)

# lists question and answer options 
num_correct = 0
for num, (question, alt_answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}")
    # prints the question with a question mark so I do not have to remember to put them in when I make the question lol
    print(f"{question}?")
    correct_answer = alt_answers[0]
    # sorted() changes the answer order (orders alphabetically to shuffle the order)
    numbered_answers = dict(zip(ascii_lowercase, random.sample(alt_answers, k=len(alt_answers))))
    # add a number for each question option (iterates through the for loop and number each option)
    for number, alternative in numbered_answers.items():
        print(f" {number}) {alternative}")
    # checks to see if user answer is the same as the options (a,b,c or d) and if not, prompts user to pick again
    while (answer_number := input("\nYour Choice?: ")) not in numbered_answers:
        print(f"Please pick between options a, b, c, or d")

    answer = numbered_answers[answer_number]
    if answer == correct_answer:
        num_correct += 1
        print("\n⭐️Correct - Great job!⭐️")
    else:
        print(f"🛑The answer is {correct_answer}, not {answer!r}. Good Try!🛑")


#build some functions to help organise the code 

def quiz_execution():

def question_preparation():

def ask_questions():

def get_answers():




print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\nYou got {num_correct} answers correct out of {num} questions!")
score_average = (num_correct/num)*100
print(f"That is a success rate of ", round(score_average, 2), "%!")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
