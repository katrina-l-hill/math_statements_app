# Logical Operations
def conjunction(A, B):
    return A and B

def disjunction(A, B):
    return A or B

def negation(A):
    return not A

def implication(A, B):
    return not A or B

def biconditional(A, B):
    return A == B

# Display results of logical operations based on user input
def display_results(A, B):
    print(f"\nResults for A = {A} and B = {B}:")
    print(f"A AND B: {conjunction(A, B)}")
    print(f"A OR B: {disjunction(A, B)}")
    print(f"NOT A: {negation(A)}")
    print(f"NOT B: {negation(B)}")
    print(f"A IMPLIES B: {implication(A, B)}")
    print(f"A IF AND ONLY IF B: {biconditional(A, B)}")
    print()

# Generate a truth table for all possible values of A and B
def truth_table():
    print("\nTruth Table:")
    print("A | B | A AND B | A OR B | NOT A | A -> B | A <-> B")
    print("---------------------------------------------------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{int(A)} | {int(B)} | {int(conjunction(A, B))} | {int(disjunction(A, B))} | {int(negation(A))} | {int(implication(A, B))} | {int(biconditional(A, B))}")
    print()

# Main program to get user input and display results or truth table
def main():
    while True:
        print("Logical Operations Program")
        print("1. Enter values for A and B")
        print("2. Generate truth table")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            # Get user input for A and B (either 1 or 0)
            try:
                input_a = int(input("Enter a value for A (1 or 0): "))
                input_b = int(input("Enter a value for B (1 or 0): "))

                if input_a in [0, 1] and input_b in [0, 1]:
                    A, B = bool(input_a), bool(input_b)
                    display_results(A, B)
                else:
                    print("Invalid input. Please enter 1 or 0.\n")
            except ValueError:
                print("Invalid input. Please enter numeric values (1 or 0).\n")

        elif choice == '2':
            truth_table()

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
