import random
import time

operators = ["+", "-", "*"]

total_problems = int(input("Enter the number of problems you want to solve "))
wrong_answers = 0

def generate_problem():
  operator = random.choice(operators)
  left_number = random.randint(1, 11)
  right_number = random.randint(1, 11)
  expr = str(left_number) + " " + operator + " " + str(right_number)
  answer = eval(expr)
  return expr, answer

input("Press any key to start!")
print("-----------------------------------------------")
start_time = time.time()

for i in range(total_problems):
  expr, answer = generate_problem()
  
  while True:
    user_answer = input("The problem number" + str(i+1) + ": " + expr + " " + "= ")
    if user_answer == str(answer):
      break
    wrong_answers += 1

print("-----------------------------------------------")
end_time = time.time()

totale_time = round(end_time - start_time, 2)
total_score = total_problems - wrong_answers

print("You got a total score of: " + str(total_score)+ "/" + str(total_problems) + " " + "in total time of : " + str(totale_time)+ " seconds")


