from Quiz import Quiz

questions = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are bananas\n(a) Blue\n(b) Puprple\n(c) Yellow\n"
]

quiz_map = [
    Quiz(questions[0], 'a'),
    Quiz(questions[1], 'c'),
]


def run_quiz(quiz_map):
    score = 0
    for question in quiz_map:
        answer = input(question.question)
        if question.answer == answer:
            score += 1
    print('Score: ' + str(score))


run_quiz(quiz_map)
