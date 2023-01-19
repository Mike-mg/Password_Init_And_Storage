#! /usr/bin/env python3
# coding: utf-8


from views.view_chars_unauthorized import GetCharactersUnauthorized


class ControllerViewsPassword:
    """
    Controllers of views password
    """

    def __init__(self):
        self.chars_unauthorized = ""
        self.label_password = ""
        self.view_chars_unauthorized = GetCharactersUnauthorized()

    def return_chars_unauthorized(self):
        """
        Return the chars no permit
        """

        self.view_chars_unauthorized.return_characters_unauthorized()

# def return_password_label(self):
#     """
#     Return the label pour the password
#     """

#     self.label_password = self.view_
