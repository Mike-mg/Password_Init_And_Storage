#! /usr/bin/env python3
# coding: utf-8

import menu


class ControllerMenu:
    """
    Controller show menu
    """

    def __init__(self) -> None:
        self.menu = menu.ViewMenu()

    def show_banner_program(self) -> str:
        """
        show the banner program
        """

        self.menu.program_banner()

    def show_menu_list(self) -> list:
        """
        show the list menu
        """

        self.menu.list_menu(
            "List of all password",
            "Create a password",
            "Remove a password",)
