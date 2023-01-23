"""
Module of controller general of program
"""

import os

import pkg_program
import pkg_password
import pkg_bdd


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self):

        self.views_program = pkg_program.ViewStartScreen()
        self.view_password = pkg_password.ViewsPassword()
        self.model_password = pkg_password.ModelPassword()
        self.data = pkg_bdd.DataControls()

    def init_program(self):
        """
        Start screen program
        """
        os.system("clear")

        self.views_program.banner()
        self.views_program.menu_list()

        while True:

            choice_menu = self.views_program.choice_menu()

            if choice_menu == 0:
                os.system("clear")
                self.data.show_all_elements()
                self.views_program.menu_list()
                choice_menu = self.views_program.choice_menu()

            if choice_menu == 1:
                os.system("clear")
                self.model_password.generate_password(
                    self.view_password.return_characters_unauthorized(),
                    self.view_password.return_password_label())

                self.data.insert_into_database(
                    self.model_password.password_generate)
                self.views_program.menu_list()

            if choice_menu == 2:
                os.system("clear")
                self.data.remove_element()
                self.views_program.menu_list()

            if choice_menu == 3:
                break
