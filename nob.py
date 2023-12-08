def increment_large_integer(digits):
    # Start from the rightmost digit
    i = len(digits) - 1
    carry = 1

    while i >= 0 and carry:
        # Add the carry to the current digit
        digits[i] += carry
        # Update the carry for the next iteration
        carry = digits[i] // 10
        # Update the current digit
        digits[i] %= 10
        # Move to the next digit towards the left
        i -= 1

    # If there is still a carry after iterating through all digits,
    # it means we need to add a new digit at the beginning
    if carry:
        digits.insert(0, carry)

    return digits

# Example usage:
input_digits = [1, 2, 3]
result = increment_large_integer(input_digits)
print(result)
