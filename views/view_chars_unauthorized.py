#! /usr/bin/env python3
# coding:utf-8


class GetCharactersUnauthorized:
    """
    class views characters no permitted
    """

    def __init__(self):

        self.characters_unauthorized = ""

    def return_characters_unauthorized(self) -> str:
        """
        Specify characters no authorized
        """

        self.characters_unauthorized = input(
            "\n\n> Indicate the characters no authorized : ")

        print(self.characters_unauthorized)
