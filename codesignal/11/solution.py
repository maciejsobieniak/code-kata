def solution(s):
    result = ''
    letters = s.split('-')
    if len(letters) > 0 and len(letters) <= 1000:
        for i in range(len(letters)):
            if letters[i].isdigit():
                letters[i] = chr(int(letters[i]) + 96)
            else:
                letters[i] = str(ord(letters[i]) - 96)
    else:
        print('Input string is to long or is empty')
    result = '-'.join(letters)
    return result