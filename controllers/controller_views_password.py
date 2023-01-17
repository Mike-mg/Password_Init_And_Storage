#! /usr/bin/env python3
# coding: utf-8


import views


class ControllerViewsPassword:
    """
    Controllers of views password
    """

    def __init__(self):
        self.characters_unauthorized = ""
        self.label_password = ""
        self.view_chars_no_permit = views.GetUnauthorizedCharacters()
        self.view_label_password = views.PasswordLabel()

    def return_chars_unauthorized(self):
        """
        Return the chars no permit
        """

        self.characters_unauthorized = self.view_chars_no_permit.c

    def return_password_label(self):
        """
        Return the label pour the password
        """

        self.label_password = self.view_label_password.get_password_label()
