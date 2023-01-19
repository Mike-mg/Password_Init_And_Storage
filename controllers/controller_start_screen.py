#! /usr/bin/env python3
# coding: utf-8

from views import view_start_screen


class ControllerStartScreen:
    """
    Controller show menu
    """

    def __init__(self) -> None:
        self.view_start_sreen = view_start_screen.ViewStartScreen()

    def show_banner_program(self) -> str:
        """
        show the banner program
        """

        self.view_start_sreen.program_banner()

    def show_menu_list(self) -> list:
        """
        show the list menu
        """
        self.view_start_sreen.menu_list(
            "List of all passwords & labels",
            "Create a password",
            "Remove a password",)
