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
print (quiz_data)
# pick a random question
# let the taker answer the question
# check the answer if it is correct
# display if they passed or not