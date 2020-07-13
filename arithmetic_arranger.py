import re

def arithmetic_arranger(problems, answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    probs = {}
    length = 0
    first_number = ""
    operator = ""
    second_number = ""
    answer = ""

    ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}

    for i, problem in enumerate(problems):
        probs[i] = re.split("\s", problem)

    for j in range(len(probs)):
        
        if probs[j][1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        elif len(probs[j][0]) > 4 or len(probs[j][2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        elif not probs[j][0].isdigit() or not probs[j][2].isdigit():
            return "Error: Numbers must only contain digits."
        
        length = (max(len(probs[j][0]), len(probs[j][2])))
        
        if j == 0:

            first_number += " "*(length - len(probs[j][0]) + 2) + probs[j][0]
        
            operator += probs[j][1] + " "*(length - len(probs[j][2])+1) + probs[j][2]
        
            second_number += "-"*(length+2)
        
        else:
            
            first_number += "    " + " "*(length - len(probs[j][0]) + 2) + probs[j][0]
        
            operator += "    " + probs[j][1] + " "*(length - len(probs[j][2])+1) + probs[j][2]
        
            second_number += "    " + "-"*(length+2)

        if answers == True:
            if j == 0:
                calculation = ops[probs[j][1]](int(probs[j][0]), int(probs[j][2]))
                answer += " "*(length - len(str(calculation)) + 2) + str(calculation)
            else:
                calculation = ops[probs[j][1]](int(probs[j][0]), int(probs[j][2]))
                answer += "    " + " "*(length - len(str(calculation)) + 2) + str(calculation)

    if answers == True:
        arranged_problems = "\n".join([first_number, operator, second_number, answer])
    else:
        arranged_problems = "\n".join([first_number, operator, second_number])

    return arranged_problems
