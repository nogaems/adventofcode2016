import re

seq = open('9.in.test').read().split('\n')[0]


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


# ну ета карочи наша модная функция, рекурсивная, да
# e - это длина подстроки, которая будет повторяться
def get_len(seq, e, i=0, result=0):
    # вначале маркер пустой, т.к. входные данные с него не начинаются никогда
    marker = ''
    while i < e:  # пока не дошли до конца входных данных
        # если символы вне модификатора, например, в начале
        if seq[i] not in '()':
            if not marker:
                result += 1
            else:
                marker += seq[i]
        elif seq[i] == '(':  # начался маркер
            marker += seq[i]
        elif seq[i] == ')':  # закончился маркер
            marker += seq[i]
            match = re.findall(r'\((\d+)x(\d+)\)', marker)
            if len(match):  # если мы в распаршенной хуйне нашли таки маркер
                l, t = match[0]
                l, t = int(l), int(t)
                # ЕБАТЬ РЕКУРСИЯ
                # ну ебать карочи считаем сколько там символов в этой хуйне с
                # i+1 до i + 1 + l, где l - длина подстроки после маркера, а t
                # - сколько раз она повторяется

                print('substr: {}, i={}, l={}, t={}, result={}'.format(
                    seq[i + 1:i + 1 + l], i + 1, l, t, result))
                result += t * get_len(seq, i + l + 1, i + 1)
                marker = ''
                i += l
        i += 1
    return result + 1

# while seq.find('(') != -1:
#    seq = decompress(seq)
# print(len(seq))
print(get_len(seq, len(seq) - 1))
