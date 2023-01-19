#! /usr/bin/env python3
# coding:utf-8

"""
Controller of program
"""

from controllers.controller_start_screen import ControllerStartScreen
from views.view_start_screen import ViewStartScreen


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self) -> None:

        self.controller_start_screen = ControllerStartScreen()
        self.view_start_screen = ViewStartScreen()

    def start_screen(self):
        """
        Entry of program
        """

        self.controller_start_screen.show_banner_program()
        self.controller_start_screen.show_menu_list()

    def choice_menu(self):

        choice_menu = input("Choice action menu : ")

        if choice_menu == 0:
            pass

        if choice_menu == 1:
            pass

        if choice_menu == 2:
            pass
