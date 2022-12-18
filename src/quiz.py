import random

# a nice function that provides lower case letters which I have used to number the question options (a,b,c,d instead of (1,2,3,4).
from string import ascii_lowercase

from main import select_mode

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

def next_step():
    next = input("Press Y to play again. Press any other key to go back to main menu.")
    if next == "y":
        quiz_execution()
    elif next == "Y":
        quiz_execution()
    else:
        select_mode()

def quiz_execution():
    questions = question_preparation(quiz_questions, number_of_questions=number_of_questions_per_quiz)
    num_correct = 0
    for num, (question, alt_answers) in enumerate(questions, start=1):
        print(f"\nQuestion {num}")
        num_correct += ask_questions(question, alt_answers)
    print(f"\nYou have answered {num_correct} questions out of {num} correctly! Fantastic!")
    score_average = (num_correct/num)*100
    print(f"That is a success rate of ", round(score_average, 2), "%!")
    next_step()

#prepares questions
def question_preparation(questions, number_of_questions):
    number_of_questions = min(number_of_questions, len(questions))
    return random.sample(list(questions.items()), k=number_of_questions)

def ask_questions(question, alt_answers):
    correct_answer = alt_answers[0]
    ordered_alt_answers = random.sample(alt_answers, k=len(alt_answers))
    answer = get_answers(question, ordered_alt_answers)
    if answer == correct_answer:
         print("\n⭐️Correct - Great job!⭐️")
         return 1
    else:
        print(f"🛑The answer is {correct_answer}, not {answer!r}. Good Try!🛑")
        return 0

def get_answers(question, alt_answers):
    print(f"{question}?")
    numbered_answers = dict(zip(ascii_lowercase, alt_answers))
    for number, alternative in numbered_answers.items():
        print(f" {number}) {alternative}")
    while (answer_number := input("\nYour Choice?: ")) not in numbered_answers:
        print(f"Please pick between options a, b, c, or d")
    return numbered_answers[answer_number]

if __name__ == "__main__":
    quiz_execution()