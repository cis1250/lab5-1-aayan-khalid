def get_valid_input():
    while True:
        try:
            terms_str = input("How many terms of the Fibonacci sequence do you want? ")
            num_terms = int(terms_str)
            if num_terms > 0:
                return num_terms
            else:
                print(" Error: Please enter a positive integer.")
        except ValueError:
            print(" Error: Invalid input. Please enter a whole number.")

def generate_fibonacci(n):
    a, b = 0, 1
    sequence = []
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence

def print_sequence(sequence):
    print("\n🔢 The Fibonacci Sequence is:")
    print(f"{' -> '.join(map(str, sequence))}")

if __name__ == "__main__":
    number_of_terms = get_valid_input()
    fib_sequence = generate_fibonacci(number_of_terms)
    print_sequence(fib_sequence)
