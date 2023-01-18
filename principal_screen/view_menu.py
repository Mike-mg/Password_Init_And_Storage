#! /usr/bin/env python3
# coding: utf-8


class ViewMenu:
    """
    menu view management
    """

    def __init__(self) -> None:
        self.menu = []

    def sub_menu(self, title: str) -> None:
        """
        Format the under-menu titles
        """

        print(f"{title.center(79)}\n{'-' * 79}")

    def program_banner(self) -> None:
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

    def list_menu(self, *menu_list):
        """"
        Get the menu list
        """

        for field in menu_list:
            self.menu.append(field)

        self.sub_menu("<<< Menu Program >>>")

        for index, field_menu in enumerate(self.menu):
            print(f"[ {index} ]  {field_menu}")

        print(f"{'-' * 79}\n")
