"""
Class get label password
"""


class PasswordLabel:
    """
    View label of password
    """

    def __init__(self):

        self.password_label = ""

    def get_password_label(self) -> str:
        """
        Get the password label
        """

        self.password_label = input(
            "> Entry the password label : ").capitalize()

        return self.password_label
