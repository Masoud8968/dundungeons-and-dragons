from termcolor2 import colored
from getpass import getpass


class InputStatement:
    @staticmethod
    def empty_input():
        input()

    @staticmethod
    def show_message(message, color):
        input(colored(message, color=color))

    @staticmethod
    def continue_or_not(user):
        user = colored(str(user), 'light_red')
        yes = colored('[yes]', 'green')
        question_mark = colored('?', 'light_green')
        statement = colored(
            f'\n\nDo you want to continue with {user}{question_mark} {yes}',
            'light_green'
            )
        condition = input(statement)
        return condition

    @staticmethod
    def login_or_register():
        register_statement = colored("\n\nPress 1 to register\n\n", "red")
        login_statement = colored("\n\nPress 2 to login\n\n", 'green')
        login_register = input(f'{register_statement}{login_statement}')
        return login_register

    @staticmethod
    def input_name():
        statement = colored('\n\nPlease Enter Your name: ', 'light_green')
        name = input(statement)
        return name

    @staticmethod
    def input_family():
        statement = colored('\n\nPlease Enter your family: ', 'light_green')
        family = input(statement)
        return family

    @staticmethod
    def input_username():
        statement = colored('\n\nPlease Enter your username: ', 'light_green')
        username = input(statement)
        return username

    @staticmethod
    def input_password():
        statement = colored('\n\nPlease Enter your password: ', 'light_green')
        password = getpass(statement)
        return password
