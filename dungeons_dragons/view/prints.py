from termcolor2 import colored


class PrintStatements:
    @staticmethod
    def print_func(message, color='white'):
        print(colored(message, color=color))
