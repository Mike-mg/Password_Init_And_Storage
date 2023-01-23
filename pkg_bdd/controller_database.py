"""
Controllers database
"""

import pkg_bdd


class DataControls:
    """
    Utils for database
    """

    def __init__(self) -> None:
        self.data_utils = pkg_bdd.UtilsDb()

    def insert_into_database(self, cle_tuple):
        """
        Insert data into Bdd
        """

        self.data_utils.insert_database(cle_tuple)

    def show_all_elements(self):
        """
        Show all elements of the database
        """

        self.data_utils.show_all_database()

    def remove_element(self):
        """
        Remove a element of the database
        """

        self.data_utils.remove_element_database()
