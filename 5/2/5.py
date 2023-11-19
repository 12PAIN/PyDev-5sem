import hashlib
import secrets
import sqlite3
from sqlite3 import Error


def getConnection():
    connection = None
    try:
        connection = sqlite3.connect("usersDataBase.sqlite")
        return connection
    except Error as e:
        print(e)

    return connection


conn = getConnection()


def createUsersTable(connection):
    try:
        c = connection.cursor()
        c.execute(""" CREATE TABLE IF NOT EXISTS users (
                                        login text NOT NULL,
                                        password text NOT NULL,
                                        salt text NOT NULL
                                    ); """)
    except Error as e:
        print(e)


def getUser(login, connection):
    try:
        cursor = connection.cursor()
        select_stmt = """SELECT * FROM users WHERE login = ?"""
        cursor.execute(select_stmt, (login,))
        return cursor.fetchone()
    except Error as e:
        print(e)

    return None


def hashAndSalt(password, salt=None):
    if salt is None:
        salt = secrets.token_urlsafe(32)

    newPasswdStr = password + salt
    passwdHash = hashlib.sha256(bytes(newPasswdStr, 'utf-8')).hexdigest()

    return passwdHash, salt


def writeNewUser(login, password, connection) -> bool:
    try:
        passwdHash, salt = hashAndSalt(password)

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users values (?,?,?)", (login, passwdHash, salt,))
        connection.commit()
        return True
    except Error as e:
        print(e)

    return False


def checkUser(login, password, connection) -> bool:

    usrLogin, usrPasswordHash, usrSalt = getUser(login, connection)

    if usrLogin is None:
        return False

    hashedPasswd, salt = hashAndSalt(password, usrSalt)

    if hashedPasswd == usrPasswordHash:
        return True

    return False


if __name__ == "__main__":
    createUsersTable(conn)

    writeNewUser(111, '111', conn)
    choice = -1
    while choice != 0:

        if choice > 0:
            print()
            print("Введите логин ->")
            login = input()
            print("Введите пароль ->")
            password = input()

            if choice == 1:
                print("Успешно!" if writeNewUser(login, password, conn) else "Неверные данные!")

            if choice == 2:
                print("Успешно!" if checkUser(login, password, conn) else "Неверные данные!")

        print()
        print("Выберите режим:")
        print("1. Регистрация")
        print("2. Войти")
        print("0. Закрыть программу")
        choice = int(input())
