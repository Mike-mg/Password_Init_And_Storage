"""
Module of controller general of program
"""

import os

import pkg_program


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self):
        pass

        self.pkg_view_program = pkg_program.ViewStartScreen()

    def init_program(self):
        """
        Start screen program
        """

        os.system("clear")

        choice_menu = self.pkg_view_program.start_program()

        while True:

            if choice_menu == 0:
                pass

            if choice_menu == 1:
                pass
            if choice_menu == 2:
                pass

            if choice_menu == 3:
                break
