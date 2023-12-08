def isPalindrome(x):
    # Convert the integer to a string
    str_x = str(x)
    
    # Check if the string is equal to its reverse
    return str_x == str_x[::-1]

# Example usage:
input_number = 121
output = isPalindrome(input_number)
print(output)  # Output: True

