from painless.helper.tools import Tools
from dungeons_dragons.controller import Dragon, GameCharacter
from painless.helper.enums import emoji
from dungeons_dragons.view import ClearScreen
from painless.helper.probability import Probability
from dungeons_dragons.view.board import Board
from termcolor2 import colored
import setting.game_settings as gs
from time import sleep
from dungeons_dragons.controller.sweets.sweets import Sweet


def game_loop(user):
    # initialize player and dragons locations
    player_location = Tools.random_point()
    dragons_location = Tools.initialize_dragons_location(3, player_location)
    dragons = list()
    for num in range(len(dragons_location)):
        name = f"dragon{num + 1}"
        name = Dragon(name, dragons_location[num], emoji.dragon)
        dragons.append(name)
    player = GameCharacter(user.name, player_location, emoji.normal_player)
    # set game properties
    game_loop_counter = 0
    boosted_counter = 0
    booster_is_on_screen = False
    separator_is_on_screen = False
    player_is_boosted = False
    hearts = ["❤️", "❤️", "❤️"]
    # infinite loop for starting game
    while user:
        ClearScreen.clear_screen()
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
                booster = Sweet.generate_sweet(
                    'booster',
                    emoji.booster,
                    dragons_location,
                    player
                    )
                characters[tuple(booster.location)] = booster.icon
                booster_is_on_screen = True
                game_loop_counter = 0
            elif Probability.generate() < 30:
                separator = Sweet.generate_sweet(
                    'separator',
                    emoji.booster,
                    dragons_location,
                    player
                    )
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
        print("")
        print(*hearts)
        Board.create_board(shown_character=characters)
        print("\n")
        # get command from user
        user_command = input(colored("\tPlease make Your move!", "cyan"))
        while user_command not in gs.VALID_COMMANDS:
            # commandlog.info(f"user enter {user_command}")
            user_command = input(colored("\tplease make a valid move: ", "red"))
        if user_command in gs.EXIT_COMMANDS:
            break
        player.move_character(user_command)
        characters = Tools.shown_character(player, dragons)
        # check if plater eat booster
        if booster_is_on_screen is True:
            if player.location == booster.location:
                booster_is_on_screen = False
                player_is_boosted = True
                player.icon = emoji.boosted_player
                characters[tuple(booster.location)] = emoji.boosted_player
                boosted_counter = 0
                game_loop_counter = 0
        # check if player eat separator
        if separator_is_on_screen is True:
            if separator_is_on_screen and player.location == separator.location:
                booster_is_on_screen = False
                # generate new location for dragons
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
        # check for killing dragons
        if player_is_boosted is True:
            num = 0
            for item in dragons:
                if player.location == item.location:
                    dragons.pop(num)
                    player_is_boosted = False
                    player.icon = emoji.normal_player
                num += 1
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
                and dragon.location == booster.location
                or separator_is_on_screen
                and dragon.location == separator.location
            ):
                dragon.location = dragon_previous_location
        # gamelog.info(f" dragons location --> {dragons}")
        # gamelog.info(f" player location --> {player.location}")
        # gamelog.info(f"booster is {player_is_boosted}")
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
                    ClearScreen.clear_screen()
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
            ClearScreen.clear_screen()
            print("game over")
            break
        if not dragons:
            ClearScreen.clear_screen()
            print("YOU WIN!")
            break

