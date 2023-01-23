"""
Module of controller general of program
"""


import pkg_views_program
import pkg_password


class ControllerGeneral:
    """
    Class of controllers general of program
    """

    def __init__(self):

        self.pkg_view_program = pkg_views_program.view_start_screen.\
            ViewStartScreen()
        self.get_password = pkg_password.ControllerViewsPassword.\
            get_password()

    def entry_program(self):
        """
        Start screen program
        """

        choice_menu = self.pkg_view_program.start_program()

        while True:

            if choice_menu == 0:
                pass

            if choice_menu == 1:
                self.get_password

            if choice_menu == 2:
                pass

            if choice_menu == 3:
                break
