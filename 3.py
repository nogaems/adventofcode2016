from functools import reduce

raw = open('3.in').read()
sides = [line.strip().split() for line in raw.split('\n')][:-1]

def is_triangle(s):
    s = [int(n) for n in s]
    if s[0] < s[1] + s[2] and s[1] < s[0] + s[2] and s[2] < s[0] + s[1]:
        return True
    else:
        return False

counter = 0
for triple in sides:    
    if is_triangle(triple):
        counter += 1

print(counter)

counter = 0
for col in range(3):
    new_sides = [row[col] for row in sides]
    for i in range(0, len(new_sides), 3):
        if is_triangle(new_sides[i:i+3]):
            counter += 1

print(counter)
