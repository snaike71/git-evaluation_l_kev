import random
import sys

def generate_expression():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operation = random.choice(operations)
    return f"{num1}{operation}{num2}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python generator.py <number_of_expressions>")
        sys.exit(1)
    
    try:
        num_expressions = int(sys.argv[1])
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)

    for _ in range(num_expressions):
        print(generate_expression())

if __name__ == "__main__":
    main()
