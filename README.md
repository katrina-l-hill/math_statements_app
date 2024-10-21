# Mathematical Statements Application

## Author: Katrina Hill

## Description
This is an application that interacts with users to evaluate logical operations on given inputs and generates truth tables, with a goal of reinforcing the understanding of conjunction, disjunction, negation, implication, and biconditional statements through practical implementation. The logical operations include:

- Conjunction (AND)
- Disjunction (OR)
- Negation (NOT)
- Implication (IF...THEN)
- Biconditional (IF AND ONLY IF)

## Features
- Accepts user inputs for two boolean values, A and B.
- Computes and displays results of:
   - A AND B
   - A OR B
   - NOT A
   - NOT B
   - A IMPLIES B
   - A IF AND ONLY IF B
- Generates and displays a full truth table for A and B.

## Files
- `app.py`: The main program that performs the base conversions.
- `tests.py`: A suite of tests for validating the functionality of the logical operations.

## Requirements
- Python 3.11

## How to Run
1. **Clone the repository** (or download the files):
   - git clone https://github.com/katrina-l-hill/math_statements_app.git
   - cd into the repository directory
2. **Run the Main program**:
   - run python app.py to run the program
   - the program presents you with 3 options:
      - Enter values for A and B:
         - choose 1 (True) or 0 (False)
      - Generate true table
      - Exit the program
3. **Run the tests**:
   - run python -m pytest tests.py to run the tests