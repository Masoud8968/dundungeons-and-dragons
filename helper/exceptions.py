class NameLengthError(ValueError):

    def __str__(self):
        return "The name must be 3 characters long"

class FamilyLengthError(ValueError):

    def __str__(self):
        return "The Family must be 3 characters long!"

class UsernameLengthError(ValueError):

    def __str__(self):
        return "The Username must be 5 characters long!"

class WrongUserNameError(ValueError):

    def __str__(self):
        return "The Username must start with letters!"

class SameUserNameError(ValueError):
    def __str__(self):
        return "This username has already been taken\nPlease enter another one:"

class PasswordLengthError(ValueError):
    
    def __str__(self):
        return "The Password must be 8 characters long"

class WrongPasswordError(ValueError):

    def __str__(self):
        return "The Password must contain letters and numbers"

class WrongUsernameOrPasswordError(ValueError):
    def __str__(self):
        return "The Username or Password does not match!"


