def reorder_numbers(a, b, c):
    # Find the minimum value
    minimum = min(a, b, c)
    # Find the maximum value
    maximum = max(a, b, c)
    # Calculate the middle value by subtracting the minimum and maximum from the sum of all three numbers
    middle = a + b + c - minimum - maximum

    return minimum, middle, maximum

# Example usage:
num1 = 5
num2 = 2
num3 = 8

reordered_nums = reorder_numbers(num1, num2, num3)
print(reordered_nums)  # Output: (2, 5, 8)
