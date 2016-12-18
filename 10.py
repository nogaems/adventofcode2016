import re
import time

instructions = open('10.in').read().split('\n')[:-1]

bots = {}
outputs = {}


class Bot:
    values = tuple()
    rule = None

    def __init__(self, value=None):
        if value:
            self.values = tuple([int(value)])

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return self.__str__()

    def add_value(self, value):
        if len(self.values) == 0:
            self.values = tuple([int(value)])
        elif len(self.values) == 1:
            value = int(value)
            low = min(value, self.values[0])
            high = value if low < value else self.values[0]
            self.values = tuple([low, high])
        else:
            raise ValueError('Bot already has a couple of values')

    def add_rule(self, rule):
        if not self.rule:
            if not isinstance(rule, list):
                raise TypeError(
                    'rule must be list, not {}'.format(rule.__class__.__name__))
            self.rule = {
                'low': {
                    'type': rule[0],
                    'num': rule[1]
                },
                'high': {
                    'type': rule[2],
                    'num': rule[3]
                }
            }

    def need_action(self):
        return True if len(self.values) == 2 else False

    def give(self):
        if len(self.values) == 2:
            low, high = self.values
            self.values = tuple()
            return low, high
        else:
            raise ValueError('Bot has not 2 items')


def init():
    global bots
    bots = {}
    for line in instructions:
        if line.startswith('value'):
            match = re.findall(r'value (\d+) goes to bot (\d+)', line)
            if len(match):
                value, bot = match[0]
                if bot not in bots.keys():
                    bots[bot] = Bot(value)
                else:
                    bots[bot].add_value(value)
        else:
            match = re.findall(
                r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
            if len(match):
                raw = match[0]
                if raw[0] not in bots.keys():
                    bots[raw[0]] = Bot()
                bots[raw[0]].add_rule(list(raw[1:]))


class End(Exception):
    pass


def process(condition=None):
    try:
        end = False
        while not end:
            end = True
            for bot in bots.keys():
                if bots[bot].values == condition:
                    raise End
                if bots[bot].need_action():
                    end = False
                    low, high = bots[bot].give()
                    if bots[bot].rule['low']['type'] == 'output':
                        output_num = bots[bot].rule['low']['num']
                        if output_num not in outputs:
                            outputs[output_num] = [low]
                        else:
                            outputs[output_num] += [low]
                    else:
                        bots[bots[bot].rule['low']['num']].add_value(low)
                    if bots[bot].rule['high']['type'] == 'output':
                        output_num = bots[bot].rule['high']['num']
                        if output_num not in outputs:
                            outputs[output_num] = [high]
                        else:
                            outputs[output_num] += [high]
                    else:
                        bots[bots[bot].rule['high']['num']].add_value(high)

    except End as e:
        return bot
    except (ValueError, TypeError) as e:
        print(e)
        exit()
init()
condition = tuple([17, 61])
print(process(condition))
init()
process()
print(outputs['0'][0] * outputs['1'][0] * outputs['2'][0])
