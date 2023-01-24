# Module views pkg_password


class ViewsPassword:
    # class views characters no permit

    def __init__(self):

        self.characters_unauthorized = []
        self.password_label = ""

    def sub_menu_label_and_chars_no_permit(self):
        # Show sub menu label and chars no permit

        str_sub_menu = "<<< Indicate no permit characters and the label >>>"

        print(f"\n{'=' * 79}\n{str_sub_menu.center(79)}\n{'=' * 79}")

        return self.characters_unauthorized

    def return_characters_unauthorized(self) -> list:
        # Specify characters no authorized

        self.characters_unauthorized = list(
            input("\n> Indicate the characters no authorized : ")
        )

        return self.characters_unauthorized

    def return_password_label(self) -> str:
        # Get the password label

        self.password_label = input(
            "> Entry the password label : ").capitalize()

        return self.password_label
