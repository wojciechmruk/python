import json

points = 0

with open('quiz.json') as json_file:
    questions = json.load(json_file)

for question in questions:
    print(question['question'])
    print('a) ' + str(question['a']))
    print('b) ' + str(question['b']))
    print('c) ' + str(question['c']))

    if input('Answer: ') == question['answer']:
        points += 1
        print('Bravo\n')
    else:
        print('Nope. Correct answer is: ' + question['answer'] + '\n')

print('Total points: ' + str(points))
