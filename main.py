"""
Entry of the program
"""

import pkg_controllers


class Main:
    """
    Class entry the program
    """

    def __init__(self):
        self.views_entry_program = pkg_controllers.ControllerGeneral()

    def entry_program(self):
        """
        Entry of program
        """

        self.views_entry_program.init_program()


main = Main()
main.entry_program()
