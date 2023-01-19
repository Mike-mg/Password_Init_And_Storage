#! /usr/bin/env python3
# coding:utf-8

import controllers
import os

os.system("clear")


class Main:
    """
    entry the program
    """

    def __init__(self) -> None:
        self.controllers_start_screen = controllers.ControllerStartScreen()

    def show_start_screen(self):
        """
        Show start screen
        """

        self.controllers_start_screen.show_banner_program()
        self.controllers_start_screen.show_menu_list()


main = Main()
main.show_start_screen()
