import re

sequence = open('8.in').read().split('\n')[:-1]

wide = 50
tall = 6
screen = [[False] * wide for i in range(tall)]

def rect(screen, a, b):
    for y in range(b):
        for x in range(a):
            screen[y][x] = True
    return screen

def rotate_90(screen):
    return [list(line) for line in zip(*screen)]

def rotate_row(screen, y, by):
    by = by % wide
    if by == 0:
        return screen
    screen[y] = screen[y][len(screen[y]) - by:] + screen[y][:-by]
    return screen

def rotate_column(screen, x, by):
    by = by % tall
    if by == 0:
        return screen
    screen = rotate_90(screen)
    screen = rotate_row(screen, x, by)
    screen = rotate_90(screen)
    return screen

def display(screen):
    print('#' * (wide+2))
    for y in range(tall):
        line = '#'
        for x in range(wide):
            if screen[y][x]:
                line += '+'
            else:
                line += ' '
        print(line + '#')
    print('#' * (wide+2))

for s in sequence:
    if s.startswith('rect'):
        match = re.findall(r'\D*(\d*)x(\d*)', s)
        if match:
            x, y = match[0]
            screen = rect(screen, int(x), int(y))
    else:
        match = re.findall(r'.*(row|column).*=(\d+) by (\d+)', s)
        if match:
            type, target, by = match[0]
            target, by = int(target), int(by)            
            if type == 'row':
                screen = rotate_row(screen, target, by)
            else:
                screen = rotate_column(screen, target, by)

counter = 0
for y in range(tall):
    for x in range(wide):
        if screen[y][x]:
            counter += 1

print(counter)
display(screen)
