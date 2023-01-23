"""
Module model pkg_password
"""

import random
import string


class ModelPassword:
    """
    Model password and generate
    """

    password = ""
    password_label = ""
    password_generate = ()

    def __init__(self):
        """
        init password
        """

        self.numbers = list(string.digits)
        self.str_upper = list(string.ascii_uppercase)
        self.str_lower = list(string.ascii_lowercase)
        self.str_punctuation = list(string.punctuation)

    def generate_password(
            self, chars_no_permit: list, label_password: str) -> tuple:
        """
        Generate the password
        """

        for chars in chars_no_permit:
            """
            remove the chars unauthorized chars of list
            """

            if chars in self.numbers:
                self.numbers.remove(chars)

            elif chars in self.str_upper:
                self.str_upper.remove(chars)

            elif chars in self.str_lower:
                self.str_lower.remove(chars)

            elif chars in self.str_punctuation:
                self.str_punctuation.remove(chars)

        nb_int = 0
        while nb_int < 4:
            """
            Selects 4 integer for the password
            """
            self.password += random.choice(self.numbers)
            nb_int += 1

        nb_str = 0
        while nb_str < 2:
            """
            Selects 2 chars of by type string for the password
            """

            self.password += random.choice(self.str_upper)
            self.password += random.choice(self.str_lower)
            self.password += random.choice(self.str_punctuation)
            nb_str += 1

        self.password_label = label_password.capitalize()
        self.password = "".join(
            random.sample(self.password, len(self.password)))

        self.password_generate = (None, self.password_label, self.password)

        return self.password_generate
