def solution(num1, num2):
    i, j = len(num1), len(num2)
    if i > j:
        return 1
    elif j > i:
        return -1
    elif i == j:
        for n1, n2 in zip(num1, num2):
            if n1 > n2:
                return 1
            elif n2 > n1:
                return -1
        return 0