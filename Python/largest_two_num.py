def largest(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are equal")

# Example usage
largest(5, 3)    # Output: 5 is greater than 3
largest(2, 4)    # Output: 4 is greater than 2
largest(7, 7)    # Output: 7 and 7 are equal
