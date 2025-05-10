import random

def generate_random_number(start, end):
    return random.randint(start, end)

# Example usage
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
random_number = generate_random_number(start, end)

print(f"Random number between {start} and {end}: {random_number}")