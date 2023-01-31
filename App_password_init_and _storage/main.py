# Entry of the program


import program


class Main:
    # Program entry point

    def __init__(self):

        self.controller_general = program.ControllerGeneral()

    def start_main(self):
        """
        Show the menu while var choice_user_menu
        Is True (4 = False and quit the program)
        """

        self.controller_general.show_menu()

        while True:

            if self.controller_general.choice_user_menu() is False:
                break


main = Main()
main.start_main()
