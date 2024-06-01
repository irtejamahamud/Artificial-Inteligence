def find_largest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None  # In case the numbers are equal

# Example usage
num1 = 5
num2 = 3
result = find_largest(num1, num2)

if result is not None:
    print(f"The largest number between {num1} and {num2} is {result}")
else:
    print(f"{num1} and {num2} are equal")
