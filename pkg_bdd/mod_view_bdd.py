"""
Views for the database
"""


class ViewBdd:
    """
    Views for the Dbb
    """

    def __init__(self) -> None:
        pass

    def choice_option_menu(self) -> int:
        """
        Select choice for action of database
        """

        choice_id = int(input("Choice id a remove : "))
        return choice_id

    def show_formated_element_table(self, all_element_database):
        """
        Get element of the table and show
        """

        for element in all_element_database:
            print(f"[ {element[0]} ] {element[1]} - {element[2]}")
