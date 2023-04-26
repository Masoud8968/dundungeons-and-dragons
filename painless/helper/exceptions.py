class NameLengthError(ValueError):
    def __str__(self):
        return "\nThe name must be 3 characters long\n\nPress Enter to continue " # noqa E501


class FamilyLengthError(ValueError):
    def __str__(self):
        return "\nThe Family must be 3 characters long!\n\nPress Enter to continue " # noqa E501


class UsernameLengthError(ValueError):
    def __str__(self):
        return "\nThe Username must be 5 characters long!\n\nPress Enter to continue " # noqa E501


class WrongUserNameError(ValueError):
    def __str__(self):
        return "\nThe Username must start with letters!\n\nPress Enter to continue " # noqa E501


class SameUserNameError(ValueError):
    def __str__(self):
        return "\nThis username has already been taken\n\nPress Enter to ensert another one " # noqa E501


class PasswordLengthError(ValueError):
    def __str__(self):
        return "\nThe Password must be 8 characters long\n\nPress Enter to continue " # noqa E501


class WrongPasswordError(ValueError):
    def __str__(self):
        return "\nThe Password must contain letters and numbers\n\nPress Enter to continue " # noqa E501


class WrongUsernameOrPasswordError(ValueError):
    def __str__(self):
        return "\nThe Username or Password does not match!\n\nPress Enter to continue " # noqa E501
