"""
Module of controller general of program
"""

import os

import pkg_password


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self):

        self.view_start_screen = pkg_password.
        # self.view_chars_unauthorized = views.view_chars_unauthorized.\
        #     GetCharactersUnauthorized()
        # self.view_label_password = views.view_label_password.PasswordLabel()
        # self.model_password = models.model_password.ModelPassword()
        self.chars_no_permit = []
        self.label_password = ""
        self.password = {}

    def start_screen(self):
        """
        Entry program of controller
        """

        while True:

            os.system("clear")
            print("ok")

            # self.view_start_screen.program_banner()
            # self.view_start_screen.menu_list()

            # choice_menu = int(input("> Choice action menu : "))

            # if choice_menu == 0:
            #     pass

            # if choice_menu == 1:
            #     self.chars_no_permit = self.view_chars_unauthorized.\
            #         return_characters_unauthorized()

            #     self.label_password = self.view_label_password.\
            #         get_password_label()

            #     self.password = self.model_password.generate_password(
            #         self.chars_no_permit, self.label_password
            #     )

            # if choice_menu == 2:
            #     pass

            # if choice_menu == 3:
            #     break
