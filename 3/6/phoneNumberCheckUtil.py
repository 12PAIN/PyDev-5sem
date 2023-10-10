import re

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

    if len(numberStrip) < 11:
        raise NumberLengthException

    if re.match('^\+?\d[0-9,-]*(\([0-9,-]+\))?[0-9,-]*$', numberStrip) is None:
        raise NumberFormatException

    numberStrip = numberStrip.replace("(", '')
    numberStrip = numberStrip.replace(")", '')

    if re.match("^\+?\d\d*(-\d+)*$",numberStrip) is None:
        raise NumberFormatException

    numberStrip = numberStrip.replace("-", '')

    if re.match("^(\+7|8)\d+$", numberStrip) is None:
        raise CountryCodeException

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

    if numberStrip[0:2] not in '+7':
        numberStrip = '+7' + numberStrip[1:]

    if len(numberStrip) != 12:
        raise NumberLengthException

    return numberStrip