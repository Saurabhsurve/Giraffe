from Questions_deutsch import Questions
prompts=[
    "\nWie ..... das auf Deutsch?\n",
    "\nDas... ich nicht.\n",
    "\n...., wie bitte ?\n",
    "\nKönnen Sie das bitte ....\n"
]

question_instances = [
    Questions(prompts[0], "heißt"),
    Questions(prompts[1], "verstehe"),
    Questions(prompts[2], "Entschuldigung"),
    Questions(prompts[3], "buchstabieren")
]



def start_test(question_instance):
    Score = 0
    print("Fill in the blanks with right word: \n verstehe, buschstabieren, Entschuldigung, heißt.")
    for question in question_instance:
        answer= input(question.prompt)
        if answer==question.answer:
            Score+=1

    print("You got "+ str(Score)+ " out of "+ str(len(question_instance)) + " questions correct.")

start_test(question_instances)
