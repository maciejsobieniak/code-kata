def solution(s):
    result = 0
    words = []
    if len(s) >= 1 and len(s) <= 500:
        words = s.split(' ')
        for word in words:
            if word.isdigit():
                result += int(word)
            else:
                for w in word:
                    if w.isdigit():
                        result += int(w)
    else:
        print('Input string is to short or to long')
    return result