# Quiz Project Instruction

## Project Stack

|  Name       | Version  |
|-------------|----------|
|  Python     |  3.11    |
|  Sqlalchemy |  2.0.10  |


## Development Environment Configuration

## Clone Project

The first things to do is to clone the repository.

### Python Env Setup

create a virtual environment to install dependencies inside it and active it.

#### poetry package

Install poetry package

```sh
pip install poetry --upgrade
```

Create Virtual Environment and install dependencies command is:

```sh
poetry install 
```

Activate virtual environment
_____________________________________________________

The program utilizes the MVP (Model-View-Presenter) architecture and employs an SQLite database with ORM (Object-Relational Mapping) using sqlalchemy for simplicity. To initiate the game, simply run the "run.py" file.

Upon starting the game, you will be prompted to either register or log in. If you do not have an account, you need to complete the registration process first. Once registered, proceed to log in.

After logging in, the game will commence. Your objective is to escape from the dragons, as they relentlessly pursue you. It's important to note that the dragons can sense your presence if you get too close to them.

While navigating the board, you may encounter a ❤️ symbol. These symbols appear randomly, and if you come across them, you will receive a boost in the form of a <span style="color:green">☻</span> symbol. With this boost, you gain the ability to retaliate against the dragons, forcing them to flee from you.

It's crucial to keep in mind that the boost is not permanent, and after a random period of time, you will revert back to your default state.

Occasionally, you may come across a 💚 symbol. These symbols act as separators, causing the dragons to relocate to random positions, increasing the distance between them and you.

In addition to the previous instructions, you can control your character's movement using the following keys:
Press "up" or "8" to move upward.
Press "down" or "2" to move downward.
Press "right" or "6" to move to the right.
Press "left" or "4" to move to the left.
If you wish to quit the game at any time, simply enter "q" to exit.

The objective of the game is to eliminate all the dragons. Keep in mind that the dragons share a common goal: to eliminate you. If the dragons manage to kill you three times, the game will be over, resulting in your loss.



