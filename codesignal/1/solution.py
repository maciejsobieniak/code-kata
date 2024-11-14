def repeat_char_jump(inputString, k):
    result = ''
    n = 0
    i = 0
    length = len(inputString)
    while n < length:
        if n == 0:
            result += inputString[n]
        else:
            i = (i + k) % length
            result += inputString[i]
        n += 1
    return result