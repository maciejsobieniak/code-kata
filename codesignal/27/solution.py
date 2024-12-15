def evaluatePath(numbers):
    position = 0
    moves = 0
    direction = 1  # 1 for right, -1 for left
    direction_changes = 0
    while direction_changes < 2:
        current_value = numbers[position]
        if current_value == 0:
            break
        new_position = position + direction * current_value
        if new_position < 0 or new_position >= len(numbers):
            direction *= -1
            direction_changes += 1
        else:
            position = new_position
            moves += 1
    return (position, moves)