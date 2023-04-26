from dungeons_dragons.models import User, LoginModel
from dungeons_dragons.view.inputs import InputStatement
from painless.helper import exceptions as exc
from dungeons_dragons.controller import CheckSatus
from dungeons_dragons.view.prints import PrintStatements
from painless.helper.messages import Message
from dungeons_dragons.view.clear_screen import ClearScreen


class Authentication:
    @staticmethod
    def check_user():
        ClearScreen.clear_screen()
        current_user = LoginModel.read()
        user = None
        if current_user is not None:
            user = current_user[0]
            continue_or_not = InputStatement.continue_or_not(user)
            if continue_or_not == "no" or continue_or_not == "n":
                LoginModel.delete()
                user = None
        return user

    @classmethod
    def login_register(cls, user):
        if user is None:
            ClearScreen.clear_screen()
            selection = InputStatement.login_or_register()
            if selection == "1":
                ClearScreen.clear_screen()
                cls.register()
                ClearScreen.clear_screen()
                user = cls.login()
            if selection == "2":
                ClearScreen.clear_screen()
                user = cls.login()
        return user

    @staticmethod
    def register():
        register_status = False
        name = family = username = password = None
        while register_status is False:
            try:
                if name is None:
                    ClearScreen.clear_screen()
                    user_input = InputStatement.input_name()
                    name = CheckSatus.check_name(user_input)
                if family is None:
                    ClearScreen.clear_screen()
                    user_input = InputStatement.input_family()
                    family = CheckSatus.check_family(user_input)
                if username is None:
                    ClearScreen.clear_screen()
                    user_input = InputStatement.input_username()
                    username = CheckSatus.check_username(user_input)
                if password is None:
                    ClearScreen.clear_screen()
                    user_input = InputStatement.input_password()
                    password = CheckSatus.check_password(user_input)
                ClearScreen.clear_screen()
                User.create(name, family, username, password)
                register_status = True
                PrintStatements.print_func(
                    Message.need_to_login,
                    color='magenta'
                    )
                return register_status
                InputStatement.empty_input()
            except exc.NameLengthError as e:
                InputStatement.show_message(e, color='red')
            except exc.FamilyLengthError as e:
                InputStatement.show_message(e, color='red')
            except exc.UsernameLengthError as e:
                InputStatement.show_message(e, color='red')
            except exc.WrongUserNameError as e:
                InputStatement.show_message(e, color='red')
            except exc.SameUserNameError as e:
                InputStatement.show_message(e, color='red')
            except exc.PasswordLengthError as e:
                InputStatement.show_message(e, color='red')
            except exc.WrongPasswordError as e:
                InputStatement.show_message(e, color='red')

    @staticmethod
    def login():
        login_status = False
        while login_status is False:
            ClearScreen.clear_screen()
            get_username = InputStatement.input_username()
            ClearScreen.clear_screen()
            get_password = InputStatement.input_password()
            user = User.read(get_username)
            if user is not None:
                user = user[0]
                if user.password == get_password:
                    LoginModel.create(
                        user.name,
                        user.family,
                        get_username,
                        get_password
                        )
                    login_status = True
                    logged_in_user = user
            if login_status is False:
                InputStatement.show_message(Message.login_error, color='red')
        ClearScreen.clear_screen()
        PrintStatements.print_func('\n')
        return logged_in_user
