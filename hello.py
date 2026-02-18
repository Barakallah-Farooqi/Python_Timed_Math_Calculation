import random
import time
Min_VALUE = 3
Max_VALUE = 12
Problems = 10
OPERAND = ["+","-","*"]
def gen_problems():
    first_value = random.randint(Min_VALUE,Max_VALUE)
    operand = random.choice(OPERAND)
    second_value = random.randint(Min_VALUE,Max_VALUE)
    exp = str(first_value) + " " + operand + " " + str(second_value)
    answer = eval(exp)
    return exp,answer
input("Press enter to start")
print("-----------------------")
start_time = time.time()
for i in range(Problems):
    exp,answer = gen_problems()
    
    while True:
        guess = input(f"Problem no {i+1}, {exp} = ")
        if guess == str(answer):
            break
        continue
end_time = time.time()
full_time = end_time - start_time
print(f"You solved all the problems in           {full_time}")
