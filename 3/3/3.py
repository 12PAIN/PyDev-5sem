lang = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
nums = set('1234567890')
sla = set('йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm')
sua = set('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM')


class PasswordError(AssertionError):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


passwordInp = input()

def checkPassword(password):
    if len(password) < 8: raise LengthError

    passwd_set = set(password)

    if len(passwd_set & sua) == 0: raise LetterError
    if len(passwd_set & sla) == 0: raise LetterError
    if len(passwd_set & nums) == 0: raise DigitError

    for charIdx in range(len(password)-2):
        charSeq = password[charIdx:charIdx + 3].lower()
        for keyboardSeq in lang:
            if charSeq in keyboardSeq:
                raise SequenceError

    return 'ok'

try:
    checkPasswordFlag = checkPassword(passwordInp)
except PasswordError as error:
    checkPasswordFlag = error.__class__.__name__


print(checkPasswordFlag)
