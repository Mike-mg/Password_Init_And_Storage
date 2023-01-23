"""
Entry of the program
"""

import controllers


class Main:
    """
    Class entry the program
    """

    def __init__(self):
        self.controllers_program = controllers.ControllerGeneral()

    def entry_program(self):
        """
        Entry of program
        """

        self.controllers_program.init_program()


main = Main()
main.entry_program()
