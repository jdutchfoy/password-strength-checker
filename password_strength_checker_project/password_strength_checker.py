def check_password_strength(password):
    """
    Check the strength of a password based on various criteria.
    Returns a list of remarks indicating the strength of the password.
    """

    # Initialize variables
    strength = 0
    remarks = []
    lower_count = upper_count = num_count = special_count = 0

    # Iterate over each character in the password
    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char.isdigit():
            num_count += 1
        elif char in string.punctuation:
            special_count += 1