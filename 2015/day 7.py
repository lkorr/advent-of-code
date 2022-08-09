import numpy as np

with open('prompt.txt') as f:
    lines = f.readlines()
prompt = []
for i in lines:
    prompt += [i.split('\n')[0]]

def solve(prompt):
    dict = {}
    while True:
        if 'a' in dict:
            return dict['a']
        dict2 = dict.copy() 
        for line in prompt:
            split = line.split()
            if len(split) == 3 and split[1] == '->':
                if split[0] in dict:
                    dict[split[2]] = dict[split[0]]
                try:
                    int(split[0])
                except ValueError:
                    continue
                dict[split[2]] = int(split[0])
                dict2 = dict.copy() 
            for i in dict2:
                if i in split and split[-1] not in dict:
                    try:
                        
                        if split[0] == 'NOT':
                            if split[1] in dict:
                                dict[split[-1]] = ~dict[split[1]]
                            else: 
                                dict[split[-1]] = ~int(split[1])
                        else:
                            if split[0] in dict: a = dict[split[0]] 
                            else: a = int(split[0])
                            if split[2] in dict: b = dict[split[2]] 
                            else: b = int(split[2])
                            if split[1] == 'AND':
                                dict[split[-1]] = a & b
                            if split[1] == 'OR':
                                dict[split[-1]] = a | b
                            if split[1] == 'LSHIFT': 
                                dict[split[-1]] = a << b
                            if split[1] == 'RSHIFT':
                                dict[split[-1]] = a >> b
                    except ValueError:
                        continue

a = solve(prompt)
print(a)
for i, j in enumerate(prompt):
    split = j.split()
    if 'b' in split and len(split) == 3:  
        split[0] = str(a) 
        new_b = ' '.join(split)
        prompt[i] = new_b
a = solve(prompt)
print(a)