import re


# phoneNumber = input()

class PhoneNumberException(Exception):
    pass


class CountryCodeException(PhoneNumberException):
    pass


class NumberLengthException(PhoneNumberException):
    pass


class NumberFormatException(PhoneNumberException):
    pass


class WrongOperatorException(PhoneNumberException):
    pass


acceptableChars = ['+', '(', ')', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']


def checkNumber(number):
    def charCheck(char):
        if char in acceptableChars:
            return True
        else:
            return False

    if False in list(map(charCheck, number)):
        raise NumberFormatException

    numberStrip = number.replace(" ", '')

    if re.match('^\+?\d[0-9,-]*(\([0-9,-]+\))?[0-9,-]*$', numberStrip) is None:
        raise NumberFormatException

    numberStrip = numberStrip.replace("(", '')
    numberStrip = numberStrip.replace(")", '')

    if re.match("^\+?\d\d*(-\d+)*$",numberStrip) is None:
        raise NumberFormatException

    numberStrip = numberStrip.replace("-", '')

    if re.match("^(\+7|8)\d+$", numberStrip) is None:
        raise CountryCodeException

    if numberStrip[0:2] not in '+7':
        numberStrip = '+7' + numberStrip[1:]

    if len(numberStrip) != 12:
        raise NumberLengthException

    mtsRe = re.compile('^\+?\d9(1|8)\d+$')
    megfonRe = re.compile('^\+?\d9(2|3)\d+$')
    bilainRe = re.compile('^\+?\d(90[2-6])|(96[0-9])\d+$')

    ops = [mtsRe, megfonRe, bilainRe]

    def checkOperatorNumber(opRegex):
        if opRegex.match(numberStrip) is not None:
            return True
        else:
            return False

    op_check = list(map(checkOperatorNumber, ops))

    if True not in op_check:
        raise WrongOperatorException

    return numberStrip


numbersArr = [
    "+7(902)123-4567",
    "8(902)1-2-3-45-67",
    "504))635(22))9 9",
    "8--9019876543-22-3--4",
    "87393))985942",
    "79623 8)487",
    "9914273 13-87",
    "8846776422",
    "+1(916)123-4567",
    "+7171((806243",
    "--9(754310--4-5",
    "+71113253136",
    "864357))4 92 8 2",
    "8 114356 30",
    "+79700830356",
    "8(916) 12 4 32-6 7"
]

numbersArr = numbersArr

for phoneNumber in numbersArr:
    try:
        print(f" {phoneNumber} : {checkNumber(phoneNumber)}")
    except NumberFormatException:
        print(f" {phoneNumber} : неверный формат!")
    except NumberLengthException:
        print(f" {phoneNumber} : неверное количество цифр!")
    except CountryCodeException:
        print(f" {phoneNumber} : неверный код страны!")
    except WrongOperatorException:
        print(f" {phoneNumber} : не определяется оператор сотовой связи!")
