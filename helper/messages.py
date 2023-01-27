from termcolor2 import colored
from helper.enums import emoji

class Message:
    staticmethod
    def print_welcome_message():
        message = (
            message
        ) = f"\n\t\t\t\t\t\t\tWelcome to the chasing game\n\n\
\t\t\t\t\t\t In this game you have to kill the dragons {emoji.dragon}\n\n\
\t\t\tDragons do not sit idle; they are seeking to kill you too. What a fascinating matchup it will be.\n\n\
You are normally {emoji.normal_player} very vulnerable to dragons. So try to avoid them.Until the red heart {emoji.booster} pops up in your path and make you a fireball {emoji.boosted_player} by eating the heart.\n\
\t\t\t   At this time, the dragons {emoji.dragon} run away when they see you, and you are the one who chases them.\n\n\
\t\tNote that this state is not permanent and you will return to the first state {emoji.normal_player} after some time. So follow the dragons carefully.\n\n\
\t\t    If the dragons are chasing you, when you see the green heart {emoji.separator}, move towards it so that the dragons move away from you.\n\
\n\t\t\t\t\t\t\tRemember, dragons can smell you.\n\n\
\t\t\t\t\t    What are you waiting for? Dragons are waiting for you.\n\n\t\t\t\t\t\t\tPress Enter to start the Game!"
        print(message)


