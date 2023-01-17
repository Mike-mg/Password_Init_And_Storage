#! /usr/bin/env python3
# coding: utf-8


class ViewMenu:
    """
    menu view management
    """

    MENU_LIST = [
        "List of all password",
        "Create a password",
        "Remove a password",
    ]

    def program_banner(self):
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

    #     self.format_menu(
    #         ""
    #     )
    #     # self.sub_menu("* MENU *")

    #     # for index, m_menu in enumerate(self.MENU_LIST):
    #     #     print(f"[ {index} ]  {m_menu}")

    #     # print(f"{'-' * 79}")

    # def choice_menu(self) -> int:
    #     """
    #     Verification and redirection to controller of menu indexes
    #     """

    #     choice = input(
    #         f"\n\n\n{'=' * 22}\n"
    #         f"Help : {len(self.MENU_LIST) - 2} > Return menu"
    #         f"\n{'-' * 22}"
    #         f"\n{':: Select a option > '}"
    #     )

    #     try:
    #         choice = int(choice)

    #     except ValueError:
    #         print(f"\n{':: ERROR > Enter a valid option [0-8]'}\n")

    #     return choice

    # def format_menu(self, title: str) -> None:
    #     """
    #     Format the under-menu titles
    #     """

    def sub_menu(self, title: str) -> None:
        """
        Format the under-menu titles
        """

        print(
            f"{title.center(50)}\n"
            f"{title.center(50)}\n"
            f"{str('-' * 50)}"
        )