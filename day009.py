import re

seq = open('day009.in').read().split('\n')[0]


def decompress(seq):
    result = ''
    i = 0
    marker = ''
    while i < len(seq):
        if seq[i] not in '()':
            if not marker:
                result += seq[i]
            else:
                marker += seq[i]
        elif seq[i] == '(':
            marker += seq[i]
        elif seq[i] == ')':
            marker += seq[i]
            match = re.findall(r'\((\d+)x(\d+)\)', marker)
            if len(match):
                l, t = match[0]
                l, t = int(l), int(t)
                result += seq[i + 1:i + l + 1] * t
                marker = ''
                i += l
        i += 1
    return result

print(len(decompress(seq)))


def get_len(seq, e, i=0, result=0):
    # print(seq[i:e], " ", result)
    marker = ''
    while i < e:
        if seq[i] not in '()':
            if not marker:
                result += 1
            else:
                marker += seq[i]
        elif seq[i] == '(':
            marker += seq[i]
        elif seq[i] == ')':
            marker += seq[i]
            match = re.findall(r'\((\d+)x(\d+)\)', marker)
            if len(match):
                l, t = match[0]
                l, t = int(l), int(t)
                result += t * get_len(seq, i + l + 1, i + 1)
                marker = ''
                i += l
        i += 1
    return result


# while seq.find('(') != -1:
#    seq = decompress(seq)
# print(len(seq))
print(get_len(seq, len(seq) - 1))
