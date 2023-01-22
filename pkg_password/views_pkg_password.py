"""
Class get chars no permit
Class get label password
"""


class GetCharactersUnauthorized:
    """
    class views characters no permit
    """

    def __init__(self):

        self.characters_unauthorized = ""

    def return_characters_unauthorized(self) -> list:
        """
        Specify characters no authorized
        """

        self.characters_unauthorized = list(
            input("\n\n> Indicate the characters no authorized : ")
        )

        return self.characters_unauthorized


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
