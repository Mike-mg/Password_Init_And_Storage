#! /usr/bin/env python3
# coding:utf-8

import os

"""
Controller of program
"""

from models.model_password import ModelPassword
from controllers.controller_start_screen import ControllerStartScreen
from controllers.controller_views_password import ControllerViewsPassword


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self) -> None:

        self.view_start_screen = ControllerStartScreen()
        self.view_controller_password = ControllerViewsPassword()
        self.model_password = ModelPassword()

    def start_screen(self):
        """
        Entry of program
        """

        self.view_start_screen.show_banner_program()
        self.view_start_screen.show_menu_list()

    def entry_program(self):

        while True:

            os.system("clear")

            self.start_screen()

            choice_menu = int(input("> Choice action menu : "))

            if choice_menu == 0:
                pass

            if choice_menu == 1:

                chars_no_permit = self.view_controller_password
                chars_no_permit.return_chars_unauthorized()

                label_password = self.view_controller_password
                label_password.return_password_label()

                password = self.model_password
                password.generate_password(
                    chars_no_permit.chars_no_permit,
                    label_password.label_password)

            if choice_menu == 2:
                pass

            if choice_menu == 3:
                break

            else:
                if choice_menu not in range(3):
                    break
