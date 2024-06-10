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

if __name__ == "__main__":
    interactive_mode()
