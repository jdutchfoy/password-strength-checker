
import unittest
from password_strength_checker import check_password_strength

class PasswordStrengthCheckerTests(unittest.TestCase):
    """
    Unit tests for the Password Strength Checker.
    """
    
    # Test case: Minimum length requirement
    def test_minimum_length(self):
        remarks = check_password_strength("pass")
        self.assertEqual(remarks, ["Password should have a minimum length of 8 characters."])

    # Test case: Lowercase letters only
    def test_lowercase_letters_only(self):
        remarks = check_password_strength("password")
        expected = ["Password should contain at least one uppercase letter, one number, and one special character."]
        self.assertEqual(remarks, expected)

    # Test case: Uppercase letters only
    def test_uppercase_letters_only(self):
        remarks = check_password_strength("PASSWORD")
        expected = ["Password should contain at least one lowercase letter, one number, and one special character."]
        self.assertEqual(remarks, expected)

    # Test case: Numbers only
    def test_numbers_only(self):
        remarks = check_password_strength("12345678")
        expected = ["Password should contain at least one lowercase letter, one uppercase letter, and one special character."]
        self.assertEqual(remarks, expected)

    # Test case: Special characters only
    def test_special_characters_only(self):
        remarks = check_password_strength("@#$%^&*")
        expected = ["Password should contain at least one lowercase letter, one uppercase letter, and one number."]
        self.assertEqual(remarks, expected)

    # Test case: Strong password
    def test_strong_password(self):
        remarks = check_password_strength("P@ssw0rd!")
        expected = ["Your password is very strong. Great job!"]
        self.assertEqual(remarks, expected)

    # Test case: Weak password missing special character
    def test_weak_password_missing_special_character(self):
        remarks = check_password_strength("Password123")
        expected = ["Password should contain at least one special character."]
        self.assertEqual(remarks, expected)

    # Test case: Weak password with short length and missing uppercase letter
    def test_weak_password_short_length_missing_uppercase_letter(self):
        remarks = check_password_strength("pass123")
        expected = ["Password should have a minimum length of 8 characters and contain at least one uppercase letter."]
        self.assertEqual(remarks, expected)


if __name__ == '__main__':
    unittest.main()