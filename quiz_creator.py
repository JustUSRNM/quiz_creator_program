# defining the function for creating a question
import json
def question_making():
    # input the question
    question = input("Enter the question\n")
    # input the choices
    choices = {}
    for option in ['A', 'B', 'C', 'D']:
        choices[option] = input(f"Enter the answer for option {option}\n")
    # input the correct answer
    correct_answer = input("Enter the correct answer for this question\n")
    while correct_answer not in choices.values():
        correct_answer = input("Your correct answer is not in the choices you have given\nThe correct anwers must be one of your choices\nenter the correct answer again\n")
    # save the question data using a dictionary
    question_data = {'question' : question, 'choices' : choices, 'answer' : correct_answer}
    return question_data
# using a loop to create question and stopping when prompted to
quiz_data = []
while True:
    # run the creating a question function
    question_data = question_making()
    quiz_data.append(question_data)
    # ask if the user to continue
    continue_input = input('Add another question? (y/n)\n')
    if continue_input.lower() == 'n':
        break
# export the data to a text file
with open(r"C:\Users\Admin\Documents\Python Compilations\quiz_tasks\quiz.json", "w") as json_file:
    json.dump(quiz_data, json_file, indent=4)