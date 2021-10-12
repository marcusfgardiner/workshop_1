import math

def calculator(operator, param_one, param_two):
    if operator == 'x':
        return param_one * param_two
    elif operator == '+':
        return param_one + param_two
    elif operator == '-':
        return param_one - param_two
    elif operator == '/':
        return param_one / param_two
    elif operator == '%':
        return param_one % param_two
    elif operator == '^':
        return param_one ** param_two
    else:
        return 'Invalid operator'
    
with open("step_2.txt", 'r') as f:
    total = 0
    for line in f:
        arguments = line.strip().split(' ')
        total += calculator(arguments[1], int(arguments[2]), int(arguments[3]))
        
print(total)

def get_next_line_number(line):
    if line[1] != 'calc':
        return int(line[1])
    else:
        return math.floor(calculator(line[2], int(line[3]), int(line[4])))

with open("step_3.txt", 'r') as f:
    viewed_statements = []
    lines = f.readlines()
    line_number = 1
    while True:
        current_line = lines[line_number - 1].strip().split(' ')
        print(current_line)
        
        if current_line in viewed_statements:
            break
        else:
            line_number = get_next_line_number(current_line)
            print('next line number:' + str(line_number))
            viewed_statements.append(current_line)
