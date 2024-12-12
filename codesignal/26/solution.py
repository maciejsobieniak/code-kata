def solution(sentence, c):
    result_output = ''
    words = sentence.split(' ')
    half_word = 0
    char_ascii_c = ord(c)
    for word in words:
        if len(word) % 2 == 0:
            half_word = int(len(word) // 2)
            word = word[half_word:]
            for char in word:
                if ord(char) < char_ascii_c:
                    result_output += char
    return result_output