"""
Entry of the program
"""

from controllers import controller_program


class Main:
    """
    entry the program
    """

    def __init__(self):
        self.controllers_program = controller_program.ControllerGeneral()

    def entry_program(self):
        """
        Entry of program
        """

        self.controllers_program.start_screen()


main = Main()
main.entry_program()
