#! /usr/bin/env python3
# coding:utf-8

"""
Entry of the program
"""

import os

from controllers.controller_program import ControllerGeneral

os.system("clear")


class Main:
    """
    entry the program
    """

    def __init__(self):
        self.controller_entry_program = ControllerGeneral()

    def show_start_screen(self):

        self.controller_entry_program.start_screen()
        self.controller_entry_program.choice_menu()


main = Main()
main.show_start_screen()
