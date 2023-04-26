from sqlalchemy import sql
from sqlalchemy import Column, Integer, String
from database import db

# from helper import exceptions as exc
# from controller.characters.base_character import BaseCharacter


class UserModel(db.Base):
    __tablename__ = "account_user"

    def __init__(self, name, family, username, password):
        self.name = name
        self.family = family
        self.username = username
        self.password = password

    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(255),
        nullable=False
    )

    family = Column(
        String(255),
        nullable=False,
    )

    username = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    @classmethod
    def read(cls, username):
        stmt = sql.select(cls).where(cls.username == username)
        user = db.session.execute(stmt).one_or_none()
        return user

    @classmethod
    def create(cls, name, family, username, password):
        user = cls(name=name, family=family, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def update_name(cls, old_name, new_name):
        stmt = sql.update(cls).where(cls.name == old_name).values(name=new_name)
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def update_family(cls, old_family, new_family):
        stmt = sql.update(cls).where(cls.family == old_family).values(family=new_family)
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def update_username(cls, old_username, new_username):
        stmt = (
            sql.update(cls)
            .where(cls.username == old_username)
            .values(username=new_username)
        )
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def update_password(cls, old_password, new_password):
        stmt = (
            sql.update(cls)
            .where(cls.password == old_password)
            .values(password=new_password)
        )
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def delete(cls, username):
        stmt = sql.delete(cls).where(cls.username == username)
        db.session.execute(stmt)
        db.session.commit()

    def __str__(self):
        return f"{self.name} {self.family}"

    def __repr__(self):
        return f"{self.name} {self.family}"


class LoginModel(db.Base):
    __tablename__ = "logged_in_user"

    def __init__(self, name, family, username, password):
        self.name = name
        self.family = family
        self.username = username
        self.password = password

    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(255),
        nullable=False
    )

    family = Column(
        String(255),
        nullable=False,
    )

    username = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    @classmethod
    def read(cls):
        stmt = sql.select(cls)
        user = db.session.execute(stmt).one_or_none()
        return user

    @classmethod
    def create(cls, name, family, username, password):
        user = cls(
            name=name,
            family=family,
            username=username,
            password=password
            )
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete(cls):
        stmt = sql.delete(cls)
        db.session.execute(stmt)
        db.session.commit()

    def __str__(self):
        return f"{self.name} {self.family}"

    def __repr__(self):
        return f"{self.name} {self.family}"