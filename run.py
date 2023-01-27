import logging
import logging.config
from time import sleep
from board.board import Board
from termcolor2 import colored
from helper.tools import Tools
from helper.enums import emoji
from helper.messages import Message
from characters.user import User
import setting.game_settings as gs
from characters.dragon import Dragon
from helper import exceptions as exc
from helper.probability import Probability
from characters.game_characters import GameCharacter


Tools.clear_screen()
Message.print_welcome_message()
input()
Tools.clear_screen()
# asking login or register mode
sign = input(colored("Press 1 to register\n\nPress 2 to login\n\n", "red"))
if sign == "1":
    # registration questions 
    Tools.clear_screen()
    print("\n")
    name = input("Please Enter Your name: ")
    Tools.clear_screen()
    print("\n")
    family = input("Please Enter Your family: ")
    Tools.clear_screen()
    print("\n")
    username = input("Please Enter Your Username: ")
    Tools.clear_screen()
    print("\n")
    password = input("Please Enter Your password: ")
    Tools.clear_screen()
    print("\n")
    registration = False
    while registration is False:
        try:
            player = User(name, family)
            player.register(username, password)
            registration = True
            print("Thank you for registration\n\nNow you have to login!")
            input("Press Enter to login")
            sign = "2"
        except exc.NameLengthError as e:
            print(e)
            print("")
            name = input("Please Enter Your name again: ")
        except exc.FamilyLengthError as e:
            print(e)
            print("")
            family = input("Please Enter Your family again: ")
        except exc.UsernameLengthError as e:
            print(e)
            print("")
            username = input("Please Enter Your Username again: ")
        except exc.WrongUserNameError as e:
            print(e)
            print("")
            username = input("Please Enter Your Username again: ")
        except exc.SameUserNameError as e:
            print(e)
            print("")
            username = input("Please Enter Your Username again: ")
        except exc.PasswordLengthError as e:
            print(e)
            print("")
            password = input("Please Enter Your password again: ")
        except exc.WrongPasswordError as e:
            print(e)
            print("")
            password = input("Please Enter Your password again: ")
# logging in questions
if sign == "2":
    logged_in_user = None
    while logged_in_user is None:
        Tools.clear_screen()
        print("\n")
        print('You Can Press "q" to exit whenever you want!')
        print("")
        input("Press enter to continue")
        Tools.clear_screen()
        print("\n")
        username = input("Please Enter Your Username: ")
        if username == "q":
            break
        password = input("Please Enter Your Password: ")
        if password == "q":
            break
        try:
            logged_in_user = User.login(username, password)
        except exc.WrongUsernameOrPasswordError as e:
            print(e)

# set custom loggers 
logging.config.fileConfig(
    fname="setting/loggerConfig.toml", disable_existing_loggers=False
)
logger = logging.getLogger(__name__)
gamelog = logging.getLogger("gameLogger")
commandlog = logging.getLogger("commandLogger")
userLog = logging.getLogger("userLogger")
# initialize player and dragons locations
player_location = Tools.random_point()
dragons_location = Tools.initialize_dragons_location(3, player_location)
dragons = list()
for num in range(len(dragons_location)):
    name = f"dragon{num + 1}"
    name = Dragon(name, dragons_location[num], emoji.dragon)
    dragons.append(name)
player = GameCharacter(logged_in_user, player_location, emoji.normal_player)
# set game properties
game_loop_counter = 0
boosted_counter = 0
booster_is_on_screen = False
separator_is_on_screen = False
player_is_boosted = False
hearts = ["❤️", "❤️", "❤️"]
# infinite loop for starting game
while logged_in_user:
    Tools.clear_screen()
    game_loop_counter += 1
    boosted_counter += 1
    # define characters that have to show in board
    characters = Tools.shown_character(player, dragons)
    # generate randomly separator and booster 
    if (
        game_loop_counter > 10
        and booster_is_on_screen is False
        and player_is_boosted is False
        and separator_is_on_screen is False
    ):
        if Probability.generate() < 50:
            booster_location = Tools.random_point()
            while (
                booster_location in dragons_location
                or booster_location == player.location
            ):
                booster_location = Tools.random_point()
            booster = GameCharacter("booster", booster_location, emoji.booster)
            characters[tuple(booster.location)] = booster.icon
            booster_is_on_screen = True
            game_loop_counter = 0
        elif Probability.generate() < 30:
            separator_location = Tools.random_point()
            while (
                separator_location in dragons_location
                or separator_location == player.location
            ):
                separator_location = Tools.random_point()
            separator =\
                GameCharacter("separator", separator_location, emoji.separator)
            separator_is_on_screen = True
            game_loop_counter = 0
            characters[tuple(separator.location)] = separator.icon
            separator_is_on_screen = True
    
    # set conditions that destroy booster and separator
    if (
        booster_is_on_screen is True or separator_is_on_screen is True
    ) and game_loop_counter > 10:
        if Probability.generate() < 60:
            booster_is_on_screen = False
            separator_is_on_screen = False
            game_loop_counter = 0
    if player_is_boosted is True and boosted_counter > 8:
        if Probability.generate() < 40:
            player.icon = emoji.normal_player
            player_is_boosted = False
            game_loop_counter = 0
    if separator_is_on_screen is True:
        characters[tuple(separator.location)] = emoji.separator
    elif booster_is_on_screen is True:
        characters[tuple(booster.location)] = emoji.booster
    # initialize game environment
    print(colored(f"Hi {logged_in_user}", "magenta"))
    print("")
    print(*hearts)
    Board.create_board(shown_character=characters)
    print("\n")
    # get command from user
    user_command = input(colored("\tPlease make Your move!", "cyan"))
    while user_command not in gs.VALID_COMMANDS:
        commandlog.info(f"user enter {user_command}")
        user_command = input(colored("\tplease make a valid move: ", "red"))
    if user_command in gs.EXIT_COMMANDS:
        break
    player_old_location = player.location.copy()
    player.move_character(user_command)
    characters = Tools.shown_character(player, dragons)
    if separator_is_on_screen is True:
        characters[tuple(separator.location)] = emoji.separator
    elif booster_is_on_screen is True:
        characters[tuple(booster.location)] = emoji.booster
        
    Tools.clear_screen()
    print(colored(f"Hi {logged_in_user}", "magenta"))
    print("")
    print(*hearts)
    Board.create_board(shown_character=characters)
    print("\n")
    print(colored("Please wait to dragons make their moves! ", "light_red"))
    if booster_is_on_screen is True:
        if player.location == booster.location:
            booster_is_on_screen = False
            player_is_boosted = True
            player.icon = emoji.boosted_player
            characters[tuple(booster.location)] = emoji.boosted_player
            boosted_counter = 0
            game_loop_counter = 0
    if separator_is_on_screen is True:
        if separator_is_on_screen and player.location == separator.location:
            booster_is_on_screen = False
            dragon_number = len(dragons)
            dragons_location = Tools.initialize_dragons_location(
                dragon_number, player.location
            )
            dragons.clear()
            for num in range(len(dragons_location)):
                name = f"dragon{num + 1}"
                name = Dragon(name, dragons_location[num], emoji.dragon)
                dragons.append(name)
            characters[tuple(separator.location)] = emoji.normal_player
            separator_is_on_screen = False
    for dragon in dragons:
        characters[tuple(dragon.location)] = dragon.icon
    if player_is_boosted is True:
        num = 0
        for item in dragons:
            if player.location == item.location:
                dragons.pop(num)
                player_is_boosted = False
                player.icon = emoji.normal_player
            num += 1
    sleep(0.5)
    for dragon in dragons:
        dragons_location = list()
        for item in dragons:
            dragons_location.append(item.location)
        dragon_previous_location = dragon.location.copy()
        if player_is_boosted is True:
            dragon.escape_mode_move(player.location)
        else:
            if player.location != dragon.location:
                dragon.follow_mode_move(player.location)
            else:
                dragon.location = dragon_previous_location
        if dragon.location in dragons_location:
            dragon.location = dragon_previous_location
        if (
            booster_is_on_screen
            and dragon.location == booster_location
            or separator_is_on_screen
            and dragon.location == separator.location
        ):
            dragon.location = dragon_previous_location
    gamelog.info(f" dragons location --> {dragons}")
    gamelog.info(f" player location --> {player.location}")
    gamelog.info(f"booster is {player_is_boosted}")
    if player_is_boosted is True:
        num = 0
        for item in dragons:
            if player.location == item.location:
                dragons.pop(num)
                player_is_boosted = False
                player.icon = emoji.normal_player
            num += 1
    if player_is_boosted is False:
        for item in dragons:
            if player.location == item.location:
                Tools.clear_screen()
                dragon_number = len(dragons)
                hearts.remove("❤️")
                print("Dragons ate one of your hearts!")
                print(f"now you have {len(hearts)} heart! ")
                sleep(2)
                dragons_location = Tools.initialize_dragons_location(
                    dragon_number, player.location
                )
                dragons.clear()
                for num in range(len(dragons_location)):
                    name = f"dragon{num + 1}"
                    name = Dragon(name, dragons_location[num], emoji.dragon)
                    dragons.append(name)
    if not hearts:
        Tools.clear_screen()
        print("game over")
        break
    if not dragons:
        Tools.clear_screen()
        print("YOU WIN`!")
        break
