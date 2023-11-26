import re

# def checkNumber(number):
#     def charCheck(char):
#         if char in acceptableChars:
#             return True
#         else:
#             return False
#
#     if False in list(map(charCheck, number)):
#         raise NumberFormatException
#
#     numberStrip = number.replace(" ", '')
#
#     if re.match('^\+?\d[0-9,-]*(\([0-9,-]+\))?[0-9,-]*$', numberStrip) is None:
#         raise NumberFormatException
#
#     numberStrip = numberStrip.replace("(", '')
#     numberStrip = numberStrip.replace(")", '')
#
#     if re.match("^\+?\d\d*(-\d+)*$",numberStrip) is None:
#         raise NumberFormatException
#
#     numberStrip = numberStrip.replace("-", '')
#
#     if re.match("^(\+7|8)\d+$", numberStrip) is None:
#         raise CountryCodeException
#
#     if numberStrip[0:2] not in '+7':
#         numberStrip = '+7' + numberStrip[1:]
#
#     if len(numberStrip) != 12:
#         raise NumberLengthException
#
#     mtsRe = re.compile('^\+?\d9(1|8)\d+$')
#     megfonRe = re.compile('^\+?\d9(2|3)\d+$')
#     bilainRe = re.compile('^\+?\d(90[2-6])|(96[0-9])\d+$')
#
#     ops = [mtsRe, megfonRe, bilainRe]
#
#     def checkOperatorNumber(opRegex):
#         if opRegex.match(numberStrip) is not None:
#             return True
#         else:
#             return False
#
#     op_check = list(map(checkOperatorNumber, ops))
#
#     if True not in op_check:
#         raise WrongOperatorException
#
#     return numberStrip


def is_correct_mobile_phone_number_ru(s):

    stripped = re.sub(' ', '', s)
    print(stripped)

    if re.match('^((\+7)|(8))-?((\(\d{3}\))|(\d{3}))-?\d{3}-?\d{2}-?\d{2}$', stripped) is None:
        return False

    return True




def my_test_is_correct_mobile_phone_number_ru():
    test_cases = (
        ('', False),
        ('+7' + 'a' * 10, False),
        ('+89991112233', False),
        ('+79991112233', True),
        ('89991112233', True),
        ('8-800-111-11-11', True),
        ('+7-800-111-11-11', True),
        ('8 (999) 123-45-67', True),
        ('8 (999 123-45-67', False),
        ('8 )999( 123-45-67', False),  # can't just cut off parentheses
        ('8 (999) (123)-45-67', False),  # even paired parentheses may be incorrect
    )
    for in_s, correct_answer in test_cases:
        answer = is_correct_mobile_phone_number_ru(in_s)
        if answer != correct_answer:
            return False
    return True


print('YES') if my_test_is_correct_mobile_phone_number_ru() else print('NO')