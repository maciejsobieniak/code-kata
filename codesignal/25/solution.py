def solution(sentence):
    words = sentence.lower().split(' ')
    result_output = ''
    for word in words:
        if len(word) % 2 != 0:
            char_count = {}
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            result_output += max(char_count, key=char_count.get)
    return result_output