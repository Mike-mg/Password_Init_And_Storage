#! /usr/bin/env python3
# coding:utf-8

"""
Controller of program
"""

from controllers.controller_start_screen import ControllerStartScreen
from controllers.controller_views_password import ControllerViewsPassword


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self) -> None:

        self.view_start_screen = ControllerStartScreen()
        self.view_controller_password = ControllerViewsPassword()

    def start_screen(self):
        """
        Entry of program
        """

        self.view_start_screen.show_banner_program()
        self.view_start_screen.show_menu_list()

    def choice_menu(self):

        choice_menu = int(input("Choice action menu : "))

        if choice_menu == 0:
            pass

        if choice_menu == 1:
            self.view_controller_password.return_chars_unauthorized()

        if choice_menu == 2:
            pass
