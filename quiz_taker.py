# import the essential modules
import json
import random
import os

# get the file location of the quiz file
program_path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(program_path, "quiz.json")

# open the file
with open(filename, 'r') as file:
    quiz_data = json.load(file)

# pick a random question
random_question = random.choice(quiz_data)
comparison = {'a': 'option_a' , 'b' : 'option_b', 'c' : 'option_c' , 'd' : 'option_d'}
options = random_question['choices']

# let the taker answer the question
print ('Question:', random_question['question'])
for opt, ans in random_question['choices'].items():
    print(f"{opt[-1].upper()}: {ans}")
user_input = input('Type the letter of the correct answer:\n')
user_answer = options[comparison[user_input.lower()]]
print ('Your answer is:', user_answer)
print ('The correct answer is:', random_question['answer'])

# check the answer if it is correct
if random_question['answer'] == user_answer:

# display if they passed or not
    print ('correct')
else:
    print ('wrong')