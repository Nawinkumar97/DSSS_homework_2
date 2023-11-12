import random

def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

def function_B():
    return random.choice(['+', '-', '*'])

def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3  # Set the number of questions to an integer value

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10)
        n2 = function_A(1, 5)  # Corrected the range for n2 to avoid potential issues with subtraction
        o = function_B()

        problem, answer = function_C(n1, n2, o)
        print(f"\nQuestion: {problem}")
        useranswer = input("Your answer: ")
        
        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Skip the rest of the loop for this iteration

        if useranswer == answer:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
