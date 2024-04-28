import re

def check_password_complexity(password):
    # Define regular expressions for various complexity criteria
    length_regex = r'^.{8,}$'  # Minimum length of 8 characters
    uppercase_regex = r'[A-Z]'  # At least one uppercase letter
    lowercase_regex = r'[a-z]'  # At least one lowercase letter
    digit_regex = r'\d'  # At least one digit
    special_char_regex = r'[\W_]'  # At least one special character

    # Check each complexity criterion
    length_check = bool(re.match(length_regex, password))
    uppercase_check = bool(re.search(uppercase_regex, password))
    lowercase_check = bool(re.search(lowercase_regex, password))
    digit_check = bool(re.search(digit_regex, password))
    special_char_check = bool(re.search(special_char_regex, password))

    # Determine overall complexity based on checks
    complexity = "Weak"
    if length_check and uppercase_check and lowercase_check and digit_check and special_char_check:
        complexity = "Strong"
    elif length_check and (uppercase_check or lowercase_check) and (digit_check or special_char_check):
        complexity = "Moderate"

    return complexity

# Example usage
password = input("Enter your password: ")
complexity = check_password_complexity(password)
print("Password complexity:", complexity)
