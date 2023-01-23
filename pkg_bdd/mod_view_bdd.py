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

        choice_id = int(input("> Choice id at remove : "))
        return choice_id

    def show_formated_element_table(self, all_element_database):
        """
        Get element of the table and show
        """
        texte_menu_table = f"{'Id'.center(11)} | {'Label'.center(45)} | {'Password'.center(15)} |"

        print(f"\n{'<<< Table Sesame >>>'.center(79)}\n{'=' * 79}\n{texte_menu_table}\n{'=' * 79}")

        for element in all_element_database:
            print(f"{str(element[0]).center(11)} | {str(element[1]).center(45)} | {str(element[2]).center(15)} |")

        print(f"{'=' * 79}\n")
