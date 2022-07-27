from Question import Question

question_prompts = [
    "Which waterfall is called the smoke that thunders?\n(a) Victoria Falls\n(b) Niagra Falls\n(c) Iguazu Falls\n(d) Angel Falls\n\n",
    "Which of the following is not a waterfall?\n(a) Iguazu\n(b) Niagra\n(c) Matopos\n(d) Angel\n\n",
    "Which mountain has the tallest peak on Earth?\n(a) Mount Denali\n(b) Mount Everest\n(c)  Mount Makalu\n(d) Mount Kilimanjaro\n\n",
    "Where is the Grand Canyon located?\n(a)  Peru\n(b) Norway\n(c) Ireland\n(d) Unites States\n\n",
    "The largest Coral reef located in which country?\n(a) United Kingdom\n(b) Australia\n(c) France\n(d) Botswana\n\n",
]

questions = [
    Question(question_prompts[0], "a")
    Question(question_prompts[1], "c")
    Question(question_prompts[2], "b")
    Question(question_prompts[3], "d")
    Question(question_prompts[4], "b")
]

print(questions)

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)
