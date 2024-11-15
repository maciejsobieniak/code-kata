def solution(numbers):
    result = []
    mid = len(numbers) // 2
    if len(numbers) % 2 == 1:
        result.append((numbers[mid], 0))
        left = mid - 1
        right = mid + 1
    else:
        left = mid - 1
        right = mid
    while left >= 0 and right < len(numbers):
        result.append((numbers[left], numbers[right]))
        left -= 1
        right += 1        
    return result