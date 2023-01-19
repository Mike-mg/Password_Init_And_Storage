#! /usr/bin/env python3
# coding:utf-8

"""
Entry of the program
"""

from controllers.controller_program import ControllerGeneral


class Main:
    """
    entry the program
    """

    def __init__(self):
        self.controller_entry_program = ControllerGeneral()

    def entry_program(self):

        self.controller_entry_program.entry_program()


main = Main()
main.entry_program()
