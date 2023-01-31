"""
Management of the start screen
"""


import os
import sys


class ViewStartScreen:
    """
    Start screen management
    """

    MENU_LIST = [
        "List of all passwords & labels",
        "Create a password",
        "Remove a password",
        "Return menu",
        "Quit",
    ]

    def sub_menu(self, title: str) -> None:
        """
        Format the under-menu titles
        """

        print(f"{title.center(79)}\n{'-' * 79}")

    def clear_screen(self) -> None:
        """
        Clear the screen
        """

        if sys.platform.startswith("linux") or \
                sys.platform.startswith("darwin"):

            os.system("clear")

        elif sys.platform.startswith("win32"):
            os.system("cls")

    def banner(self) -> None:
        """
        Show the banner of program
        """

        name_program = "-*- Password Init And Storage -*-"

        print(
            f"\n{'=' * 79}\n"
            f"{'||'}{name_program.center(75)}{'||'}\n"
            f"{'||'}{'- Ver 0.0.1 - 2023 -'.center(75)}{'||'}\n"
            f"{'||'}{''.center(75)}{'||'}\n"
            f"{'||'}{'* Mike-Mg *':>75}{'||'}\n"
            f"{str('=' * 79)}\n\n\n"
        )

    def show_menu(self):
        """
        menu view management
        """

        self.clear_screen()
        self.banner()
        self.sub_menu("* MENU *")

        for index, m_menu in enumerate(self.MENU_LIST):
            print(f"[ {index} ]  {m_menu}")

        print(f"{'-' * 79}")

    def choice_menu(self) -> int:
        """
        Verification and redirection to controller of menu indexes
        """

        choice = input(
            f"\n\n\n{'=' * 22}\n"
            f"Help : {len(self.MENU_LIST) - 2} > Return menu"
            f"\n{'-' * 22}"
            f"\n{'> Select a option > '}"
        )

        try:
            choice = int(choice)

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid option [0-4]'}\n")

        return choice
