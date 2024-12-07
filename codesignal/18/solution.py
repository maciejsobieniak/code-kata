def solution(sentences, words):
    result_list = []
    for sentence, word in zip(sentences, words):
        if word in sentence:
            reversed_word = word[::-1]
            result_list.append(sentence.replace(word, reversed_word))
        elif word.capitalize() in sentence:
            word_capitalize = word.capitalize()
            reversed_word = word[::-1].capitalize()
            result_list.append(sentence.replace(word_capitalize, reversed_word))
        else:
            result_list.append(sentence)
    return result_list
