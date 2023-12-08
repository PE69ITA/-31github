def is_power_of_two(n):
    # Check if the number is positive and has only one bit set
    return n > 0 and (n & (n - 1)) == 0

# Example usage:
result = is_power_of_two(1)
print(result)  # This will print True because 16 is 2^4