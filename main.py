"""
Entry of the program
"""

import controllers


class Main:
    """
    Entry the program
    """

    def __init__(self):
        self.controllers_program = controllers.controller_program.\
            ControllerGeneral()

    def entry_program(self):
        """
        Entry of program
        """

        self.controllers_program.entry_program()


main = Main()
main.entry_program()
