from hashlib import md5
import sys
door_id = 'cxdnnyjw'
result1 = ''
result2 = [None] * 8
i = 0
while None in result2:
    i += 1
    hash = md5(str(door_id + str(i)).encode('utf8')).hexdigest()
    if hash[:5] == '00000':
        if len(result1) < 8:
            result1 += hash[5]
        position = int(hash[5], 16)
        if position in range(8) and not result2[position]:
            result2[position] = hash[6]        

print(result1)
print(''.join(result2))
    
