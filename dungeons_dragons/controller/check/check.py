from painless.helper import exceptions as exc
from dungeons_dragons import models


class CheckSatus:
    @staticmethod
    def check_name(get_name):
        if len(get_name) < 3:
            raise exc.NameLengthError()
        return get_name

    @staticmethod
    def check_family(get_family):
        if len(get_family) < 3:
            raise exc.FamilyLengthError()
        return get_family

    @staticmethod
    def check_username(get_username):
        username = models.User.read(get_username)
        if username is not None:
            raise exc.SameUserNameError()
        if len(get_username) < 5:
            raise exc.UsernameLengthError()
        if not get_username[0].isalpha():
            raise exc.WrongUserNameError()
        return get_username

    @staticmethod
    def check_password(get_password):
        if len(get_password) < 8:
            raise exc.PasswordLengthError()
        if get_password.isalpha() or get_password.isdigit():
            raise exc.WrongPasswordError()
        return get_password
