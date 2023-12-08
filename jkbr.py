def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0
    
    for numeral in reversed(s):
        value = roman_dict[numeral]
        
        if value < prev_value:
            result -= value
        else:
            result += value
        
        prev_value = value
    
    return result

# Example usage:
roman_numeral = "XXVII"
integer_value = roman_to_int(roman_numeral)
print(f'The integer value of {roman_numeral} is: {integer_value}')
