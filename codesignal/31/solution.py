def solution(num1, num2):
    product = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            # Multiply digits and add to the result
            mul = int(num1[i]) * int(num2[j])
            # Determine positions in the result list
            p1 = i + j
            p2 = i + j + 1
            # Add to the current position
            sum = mul + product[p2]
            # Update the result list
            product[p2] = sum % 10
            product[p1] += sum // 10
    result = ''.join(map(str, product))
    # Remove leading zeros
    return result.lstrip('0') or '0'