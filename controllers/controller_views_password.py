#! /usr/bin/env python3
# coding: utf-8


from views.view_chars_unauthorized import GetCharactersUnauthorized
from views.view_label_password import PasswordLabel


class ControllerViewsPassword:
    """
    Controllers of views password
    """

    def __init__(self):

        self.chars_no_permit = []
        self.label_password = ""
        self.view_chars_unauthorized = GetCharactersUnauthorized()
        self.view_label_password = PasswordLabel()

    def return_chars_unauthorized(self) -> list:
        """
        Return the chars no permit
        """
        self.chars_no_permit = (
            self.view_chars_unauthorized.return_characters_unauthorized()
        )

        return self.chars_no_permit

    def return_password_label(self):
        """
        Return the label for the password
        """

        self.label_password = self.view_label_password.get_password_label()

        return self.label_password
