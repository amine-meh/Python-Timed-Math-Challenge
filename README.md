# Timed Math Problems Game

This is a Python-based timed math problems game where users solve randomly generated math problems within a single session. The game tracks the user's total score, wrong answers, and time taken to complete the session.

## Features
- Randomly generates math problems using addition, subtraction, and multiplication operators.
- Allows users to set the number of problems they wish to solve.
- Tracks wrong answers and deducts them from the total score.
- Displays the total time taken to complete the problems.

## How It Works
1. The game asks the user to input the number of problems they want to solve.
2. It generates random math problems using the `+`, `-`, and `*` operators.
3. The user attempts to solve each problem and provides an answer.
4. If the answer is incorrect, the user is prompted to try again.
5. The game calculates the total score, considering wrong attempts, and displays the time taken to complete the session.

## Requirements
- Python 3.6 or higher

## Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Run the script:
   ```bash
   python timed_math_problems.py
   ```

## Code Explanation
### Key Components
- **Random Problem Generation:**
  ```python
  operators = ["+", "-", "*"]
  def generate_problem():
      operator = random.choice(operators)
      left_number = random.randint(1, 11)
      right_number = random.randint(1, 11)
      expr = str(left_number) + " " + operator + " " + str(right_number)
      answer = eval(expr)
      return expr, answer
  ```
  Random math problems are generated using the `random.choice` and `random.randint` functions, and evaluated using `eval`.

- **Timing and Scoring:**
  ```python
  start_time = time.time()
  end_time = time.time()
  totale_time = round(end_time - start_time, 2)
  total_score = total_problems - wrong_answers
  ```
  Timing is measured using `time.time()`, and the total score is calculated by subtracting wrong attempts from the total problems.

### Full Code
```python
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
```

## Contribution
Feel free to fork the repository and make improvements. Submit a pull request with a detailed explanation of your changes.

## License
This project is open-source and available under the MIT License.
