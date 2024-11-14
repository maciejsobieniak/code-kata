def reversed_triple_chars(s: str) -> str:
    result = ''
    length = len(s)
    for i in range(0, length, 3):
        if len(s[i:i+3]) == 3:
            result += s[i:i+3][::-1]
        else:
            result += s[i:i+3]
    return result