# Basic Flow Tracking with print()

def add_numbers(a, b):
    print(f"Debug: a = {a}, b = {b}")  # Debug print
    result = a + b
    print(f"Debug: result = {result}")  # Debug print
    return result

add_numbers(3, 5)