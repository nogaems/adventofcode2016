addresses = open('7.in').read().split('\n')[:-1]

def prepare(address):
    subseqs = [s.split(']') for s in address.split('[')]
    result = []
    for ss in subseqs:
        if isinstance(ss, str):
            result.append(ss)
        if isinstance(ss, list):
            for s in ss:
                result.append(s)
    return result

class NotSupportedABBA(Exception):
    pass
class SupportedABA(Exception):
    pass

counter = 0

for address in addresses:
    try:
        abba = False
        parsed = prepare(address)
        for part in parsed:
            if len(part) < 4:
                continue
            for i in range(len(part)-4+1):
                if part[i] != part[i+1] and part[i:i+2] == part[i+2:i+4][::-1]:
                    if parsed.index(part) % 2 == 0:
                        abba = True
                    else:
                        raise NotSupportedABBA
        if abba:
            counter += 1            
    except NotSupportedABBA as e:
        pass

print(counter)

counter = 0

for address in addresses:
    try:
        aba = False
        parsed = prepare(address)
        for odd_part in parsed[::2]:
            if len(odd_part) < 3:
                continue
            for i in range(len(odd_part) -3 + 1):
                if odd_part[i] != odd_part[i+1] and odd_part[i] == odd_part[i+2]:
                    search = odd_part[i+1] + odd_part[i] + odd_part[i+1]
                    for even_part in parsed[1::2]:
                        if even_part.find(search) != -1:
                            counter += 1
                            raise SupportedABA
    except SupportedABA as e:
        pass

print(counter)
