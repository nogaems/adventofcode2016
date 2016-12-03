
rotate = lambda move: 90 if move[0] is 'R' else 270

def move_along_sequence(sequence, start=None):
    """
    (0,0) - y, x
    """
    if not start:
        start = (0,0)
    result = start
    rotation = 0
    for move in sequence:
        rotation = rotation + rotate(move)
        direction = int((rotation % 360) / 90)
        value = int(move[1:])
        if direction is 0:
            result = (result[0] + value, result[1])
        elif direction is 1:
            result = (result[0], result[1] + value)
        elif direction is 2:
            result = (result[0] - value, result[1])
        elif direction is 3:
            result = (result[0], result[1] - value)
    return result

def move_by_step(sequence, start=None):
    if not start:
        start = (0,0)
    result = start
    rotation = 0
    for move in sequence:
        rotation = rotation + rotate(move)
        direction = int((rotation % 360) / 90)
        value = int(move[1:])
        for _ in range(value):
            if direction is 0:
                result = (result[0] + 1, result[1])
            elif direction is 1:
                result = (result[0], result[1] + 1)
            elif direction is 2:
                result = (result[0] - 1, result[1])
            elif direction is 3:
                result = (result[0], result[1] - 1)
            yield result
            
def count_blocks(d):
    return abs(d[0]) + abs(d[1])
