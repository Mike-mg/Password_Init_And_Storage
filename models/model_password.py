#! /usr/bin/env python3
# coding: utf-8

import random
import string


class ModelPassword:
    """
    Model password and generate
    """

    password = ""

    def __init__(self):
        """
        init password
        """

        self.numbers = list(string.digits)
        self.str_upper = list(string.ascii_uppercase)
        self.str_lower = list(string.ascii_lowercase)
        self.str_punctuation = list(string.punctuation)

    def generate_password(self, unauthorized_characters: list) -> str:
        """
        Generate the password
        """

        for chars in unauthorized_characters:
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

        for num_int in range(4):
            """
            Selects 4 integer for the password
            """

            self.password += random.choice(self.numbers)

        for type_string in range(2):
            """
            Selects 2 chars of by type string for the password
            """
            self.password += random.choice(self.str_upper)
            self.password += random.choice(self.str_lower)
            self.password += random.choice(self.str_punctuation)

        self.password = ''.join(random.sample(
            self.password, len(self.password)))

        return self.password
