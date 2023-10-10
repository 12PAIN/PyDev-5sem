lang = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
nums = set('1234567890')
sla = set('йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm')
sua = set('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM')

passwordInp = input()


def checkPassword(password):
    if len(password) < 8: return 'error'

    passwd_set = set(password)

    if len(passwd_set & sua) == 0: return 'error'
    if len(passwd_set & sla) == 0: return 'error'
    if len(passwd_set & nums) == 0: return 'error'

    for charIdx in range(len(password)-2):
        charSeq = password[charIdx:charIdx + 3].lower()
        for keyboardSeq in lang:
            if charSeq in keyboardSeq:
                return 'error'

    return 'ok'


print(checkPassword(passwordInp))
