"""
Module of controller general of program
"""

import program
import password
import bdd


class ControllerGeneral:
    # Class of controllers general of program

    def __init__(self):

        self.views_program = program.ViewStartScreen()
        self.view_password = password.ViewsPassword()
        self.model_password = password.ModelPassword()
        self.data = bdd.DataControls()

    def show_menu(self) -> None:
        # Show the program menu

        self.views_program.show_menu()

    def choice_user_menu(self) -> bool:
        # Menu selection

        choice = self.views_program.choice_menu()

        if choice == 0:
            # Show all database table

            self.data.show_all_elements()

        elif choice == 1:
            # Add new element in the table

            self.view_password.sub_menu_label_and_chars_no_permit()
            self.model_password.generate_password(
                self.view_password.return_characters_unauthorized(),
                self.view_password.return_password_label())
            self.data.insert_into_database(
                self.model_password.password_generate)

        elif choice == 2:
            # Remove a element of the table

            self.data.remove_element()

        elif choice == 3:
            # Return menu program

            self.views_program.show_menu()

        elif choice == 4:
            # Leave program

            return False
