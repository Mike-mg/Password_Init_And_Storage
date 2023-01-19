#! /usr/bin/env python3
# coding:utf-8


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
