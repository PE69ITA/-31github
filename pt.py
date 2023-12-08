def longest_common_prefix(strings):
    if not strings:
        return ""

    # Sort the strings to easily find common prefix
    strings.sort()

    # Take the first and last string in the sorted array
    first_str, last_str = strings[0], strings[-1]

    # Find common prefix between the first and last string
    common_prefix = ""
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix += first_str[i]
        else:
            break

    return common_prefix

# Example usage:
string_array = ["flower", "flow", "flight"]
result = longest_common_prefix(string_array)
print("Longest Common Prefix:", result)
