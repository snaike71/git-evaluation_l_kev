import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def calculate(expression):
    try:
        return eval(expression)
    except SyntaxError:
        return "Erreur de syntaxe"
    except ZeroDivisionError:
        return "Division par zéro"
    except Exception as e:
        return f"Erreur : {str(e)}"

def interactive_mode():
    while True:
        try:
            expression = input("> ")
            if expression.lower() == 'exit':
                print("Fin des calculs")
                break
            result = calculate(expression)
            print(result)
        except Exception as e:
            print(f"Erreur : {e}")

def read_from_stdin():
    for line in sys.stdin:
        if line.strip():  # Ignore empty lines
            try:
                result = calculate(line.strip())
                print(result)
            except Exception as e:
                print(f"Erreur : {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--stdin':
        read_from_stdin()
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
