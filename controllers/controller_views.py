#! /usr/bin/env python3
# coding: utf-8


import views


class ControllerMain:
    """
    Controllers of views
    """

    def __init__(self):
        self.characters_unauthorized = ""
        self.view_chars_no_permit = views.GetUnauthorizedCharacters()
        self.view_label_password = views.PasswordLabel()

    def return_chars_unauthorized(self):
        """
        Return the chars no permit
        """

        self.characters_unauthorized = self.view_chars_no_permit()
        return self.characters_unauthorized

    def return_password_label(self):
        """
        Return the label pour the password
        """
        pass
