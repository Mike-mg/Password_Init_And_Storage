"""
Module controller pkg_password
"""

import views_pkg_password
import model_pkg_password


class ControllerViewsPassword:
    """
    Controllers of views password
    """

    def __init__(self):

        self.view_chars_unauthorized = views_pkg_password.\
            GetCharactersUnauthorized()
        self.view_label_password = views_pkg_password.PasswordLabel()
        self.model_password = model_pkg_password()

    def get_password(self):
        """
        Retunrn the password generate
        """

        password = self.model_password(
            self.view_chars_unauthorized, self.view_label_password)

        print(password)

    # def return_chars_unauthorized(self) -> list:
    #     """
    #     Return the chars no permit
    #     """
    #     self.chars_no_permit = (
    #         self.view_chars_unauthorized.return_characters_unauthorized()
    #     )

    #     return self.chars_no_permit

    # def return_password_label(self):
    #     """
    #     Return the label for the password
    #     """

    #     self.label_password = self.view_label_password.get_password_label()

    #     return self.label_password
