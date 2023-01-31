"""
Utils for the database
"""

import sqlite3
import bdd


class UtilsDb:
    """
    Utility for the database
    """

    def __init__(self) -> None:
        self.database = "pkg_bdd/database.db"
        self.view_database = bdd.ViewBdd()

    def insert_database(self, values):
        """
        Connection at bdd
        """
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("insert into sesame values(?, ?, ?)", values)
        connection.commit()
        connection.close()

    def show_all_database(self):
        """
        Show all elements of the database
        """

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        all_element_database = cursor.execute(
            "select * from sesame").fetchall()

        self.view_database.show_formated_element_table(all_element_database)
        connection.close()

    def remove_element_database(self):
        """
        Remove a elements of the database
        """

        self.show_all_database()

        choice_id = self.view_database.choice_option_menu()

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(f"delete from sesame where id = {choice_id}")
        connection.commit()

        connection.close()
