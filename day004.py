class Room:
    def __init__(self, s):
        _, *self.name = s.split('-')[::-1]
        self.name = ''.join(self.name)[::-1]        
        self.id, *self.hash = _[:-1].split('[')
        self.id = int(self.id)
        self.hash = self.hash[0]

        self.name_with_dashes = '-'.join(s.split('-')[:-1])

    def __repr__(self):
        return '{}-{}[{}]'.format(self.name_with_dashes, self.id, self.hash)
        
    def _get_hash(self, external=None):
        if external:
            name = external
        else:
            name = self.name
            
        entries = {}
        hash = ''
        for ch in name:
            if ch not in entries.keys():
                entries[ch] = 1
            else:
                entries[ch] += 1
        for entry_count in sorted(list(set(entries.values())), reverse=True):
            temp = ''
            for key in entries.keys():
                if entries[key] is entry_count:
                    temp += key
            hash += ''.join(sorted(temp))

        return hash[:5]                    

    def is_valid(self):
        return True if self._get_hash() == self.hash else False

    def decrypt(self):
        result = ''
        base_shift = self.id % 26        
        for ch in self.name_with_dashes:           
            if ch is '-':
                result += ' '
                continue
            result_shift = base_shift + ord(ch)            
            if result_shift <= 122:
                result += chr(result_shift)
            else:               
                result += chr(97 + (result_shift - 123))
        return result


rooms = open('day004.in').read()
rooms = rooms.split('\n')[:-1]

result = 0
target_name = 'northpole object storage'
search = 0

for name in rooms:
    room = Room(name)
    if room.is_valid():
        result += room.id       
        if room.decrypt() == target_name:
            search = room.id
            
print(result)
print(search)
