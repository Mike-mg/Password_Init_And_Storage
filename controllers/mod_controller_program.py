"""
Module of controller general of program
"""

# import os

import pkg_program
import pkg_password
import pkg_bdd


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self):
        pass

        self.views_program = pkg_program.ViewStartScreen()
        self.view_chars_unauthorized = pkg_password.GetCharactersUnauthorized()
        self.view_label_password = pkg_password.GetPasswordLabel()
        self.model_password = pkg_password.ModelPassword()
        self.data = pkg_bdd.DataControls()

    def init_program(self):
        """
        Start screen program
        """

        while True:

            # os.system("clear")

            choice_menu = self.views_program.start_program()

            if choice_menu == 0:
                self.data.show_all_elements()

            if choice_menu == 1:
                self.model_password.generate_password(
                    self.view_chars_unauthorized.return_characters_unauthorized(), # noqa
                    self.view_label_password.return_password_label())

                self.data.insert_into_database(
                    self.model_password.password_generate)

            if choice_menu == 2:
                self.data.remove_element()

            if choice_menu == 3:
                break
