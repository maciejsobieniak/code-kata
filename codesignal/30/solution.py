def solution(num1, num2):
    i, j, borrow, res = len(num1) - 1, len(num2) - 1, 0, []
    while i >= 0:
        n1 = int(num1[i]) - borrow
        n2 = int(num2[j]) if j >= 0 else 0
        # Check if borrowing is needed
        if n1 < n2:
            n1 += 10  # Borrow from the next digit
            borrow = 1
        else:
            borrow = 0
        # Subtract and append the result
        res.append(str(n1 - n2))
        i, j = i - 1, j - 1
    # Remove leading zeros
    while len(res) > 1 and res[-1] == '0':
        res.pop()

    return ''.join(res[::-1])  # Reverse and join the result