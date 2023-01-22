"""
Entry of the program
"""

import controllers


class Main:
    """
    entry the program
    """

    def __init__(self):
        self.controllers_program = controllers.controller_program.\
            ControllerGeneral()

    def entry_program(self):
        """
        Entry of program
        """

        self.controllers_program.start_screen()


main = Main()
main.entry_program()
