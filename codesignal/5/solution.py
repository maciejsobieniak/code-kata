def unusual_traversal(array):
    result = []
    mid = len(array) // 2
    result.append(array[mid])
    left = mid - 1
    right = mid + 1
    while left >= 0 and right < len(array):
        if left == 0:
            result.append(array[left])
        else:
            result.append(array[left - 1])
            result.append(array[left])
        if right == len(array) - 1 :
            result.append(array[right])
        else:
            result.append(array[right])
            result.append(array[right + 1])
        left -= 2
        right += 2  
        
    return result