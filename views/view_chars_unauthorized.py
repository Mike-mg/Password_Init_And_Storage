#! /usr/bin/env python3
# coding:utf-8


class GetCharactersUnauthorized:
    """
    class views characters no permitted
    """

    def __init__(self):

        self.characters_unauthorized = ""

    def characters_unauthorised(self) -> str:
        """
        Specify characters no authorized
        """

        self.characters_unauthorized = input(
            "Indicate the characters no authorized : ")

        return self.characters_unauthorised
