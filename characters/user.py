import json

from characters.base_character import BaseCharacter

from helper import exceptions as exc
class User(BaseCharacter):
    """
    This is user class.
    any person that wants to playe this game must be an instance of this class.
    it hase register and login method
    """
    def __str__(self):
        return f"{self.name} {self.family}"
    
    def __repr__(self):
        return f"{self.name} {self.family}"

    def register(self, username, password):
        all_users_data = self.read_data_base()
        user_registration = True
        self.username = username
        self.password = password
        user_data = dict(
            name = self.name,
            family = self.family,
            username = self.username,
            password = self.password
            # confirm_password = confirm_password 
        )
        # confirm_password = confirm_password
        all_users_data.append(user_data)
        with open("data_base/dataBase.json", mode="w") as data_base:
            json.dump(all_users_data, data_base, indent=4)
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5:
            raise exc.UsernameLengthError()
        if not value[0].isalpha():
            raise exc.WrongUserNameError()
        with open("data_base/dataBase.json", mode="r") as data_base:
            all_users_data = json.load(data_base)     
        for user in all_users_data:
            if value == user["username"]:
                raise exc.SameUserNameError()
        self.__username = value

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise exc.PasswordLengthError()
        if value.isalpha() or value.isdigit():
            raise exc.WrongPasswordError()
        self.__password = value

    @staticmethod
    def read_data_base():
        with open("data_base/dataBase.json", mode="a"):
            pass
        with open("data_base/dataBase.json", mode="r") as data_base:
            data = data_base.read()
            data_base.seek(0)
            if len(data) == 0:
                all_users_data = list()
            else:
                all_users_data = json.load(data_base)
        return all_users_data

    @classmethod
    def login(cls, username, password):
        all_user_data = cls.read_data_base()
        logging_in = False
        for user in all_user_data:
            ss = username
            cc = user["username"]
            if ss == cc:
                if password == user["password"]:
                    logged_in_user_name = user["name"]
                    logged_in_user_family = user["family"]
                    logged_in_user = user["username"]
                    logging_in = True
        if logging_in is False:
            raise exc.WrongUsernameOrPasswordError
        return logged_in_user
