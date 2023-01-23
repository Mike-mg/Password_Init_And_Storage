"""
Utils for the database
"""

import sqlite3


class UtilsDb:
    """
    Utility for the database
    """

    def __init__(self) -> None:
        self.database = "pkg_bdd/database.db"

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

        for element in all_element_database:
            print(f"[ {element[0]} ] {element[1]} - {element[2]}")

        connection.close()

    def remove_element_database(self):
        """
        Remove a elements of the database
        """

        self.show_all_database()

        choice_id = int(input("Choice id a remove : "))

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(f"delete from sesame where id = {choice_id}")

        connection.close()
