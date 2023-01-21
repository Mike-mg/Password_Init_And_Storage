"""
Controller of program
"""

import os

from views import view_start_screen


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self):

        self.view_start_screen = view_start_screen.ViewStartScreen()

    def start_screen(self):
        """
        Entry program of controller
        """

        while True:

            os.system("clear")

            self.view_start_screen.program_banner()
            self.view_start_screen.menu_list()

            choice_menu = int(input("> Choice action menu : "))

            if choice_menu == 0:
                pass

            if choice_menu == 1:
                pass

            if choice_menu == 2:
                pass

            if choice_menu == 3:
                break
