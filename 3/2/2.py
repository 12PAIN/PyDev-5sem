lang = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
nums = set('1234567890')
sla = set('йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm')
sua = set('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM')


passwordInp = input()

def checkPassword(password):
    assert len(password) >= 8, 'error'

    passwd_set = set(password)

    assert len(passwd_set & sua) != 0, 'error'
    assert len(passwd_set & sla) != 0, 'error'
    assert len(passwd_set & nums) != 0, 'error'

    for charIdx in range(len(password)-2):
        charSeq = password[charIdx:charIdx + 3].lower()
        for keyboardSeq in lang:
            assert charSeq not in keyboardSeq, 'error'

    return 'ok'
try:
    checkPasswordFlag = checkPassword(passwordInp)
except AssertionError:
    checkPasswordFlag = 'error'

print(checkPasswordFlag)
