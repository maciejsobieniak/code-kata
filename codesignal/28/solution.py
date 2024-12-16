def solution(numbers, obstacle):
    steps = [0] * len(numbers)
    for i in range(len(numbers)):
        position = i
        step_taken = 0
        while position < len(numbers):
            current_value = numbers[position]
            if current_value == obstacle:
                steps[i] = -1
                break
            new_position = position + current_value
            if new_position < len(numbers):
                step_taken += 1
                position = new_position
            else:
                steps[i] = step_taken + 1
                break
    return steps