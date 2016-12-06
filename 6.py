repeated = open('6.in').read().split('\n')[:-1]
entries = [[version[i] for version in repeated] for i in range(len(repeated[0]))]
message1 = ''
message2 = ''
for ch in entries:
    counter = {}
    for c in ch:
        if c not in counter.keys():
            counter[c] = 1
        else:
            counter[c] += 1
    message1 += list(counter.keys())[list(counter.values()).index(max(counter.values()))]
    message2 += list(counter.keys())[list(counter.values()).index(min(counter.values()))]
   
print(message1)
print(message2)
