import numpy as np

with open('prompt.txt') as f:
    lines = f.readlines()
prompt = []
for i in lines:
    prompt += [i.split('\n')[0]]



lights = np.zeros((1000, 1000))
lights2 = np.zeros((1000, 1000))
for instruction in prompt:
    splitted = instruction.split()
    if 'toggle' in instruction:
        a = splitted[1]
        b = splitted[-1]
        order = 'toggle'
    if 'turn' in instruction:
        a = splitted[2]
        b = splitted[-1]
        order = splitted[1]
    a_xy = a.split(',')
    b_xy = b.split(',')
    i = 0
    j = 0
    for i in range(int(a_xy[0]), int(b_xy[0])+1):
        for j in range(int(a_xy[1]), int(b_xy[1])+1):
            if order == 'off':
                lights[i][j] = 0
                lights2[i][j] = lights2[i][j] - 1
                if lights2[i][j] < 0:
                    lights2[i][j] = 0
            if order == 'on':
                lights[i][j] = 1
                lights2[i][j] = lights2[i][j] + 1
            if order == 'toggle':
                lights[i][j] = (lights[i][j] + 1) % 2
                lights2[i][j] = lights2[i][j] + 2
print(np.sum(lights))
print(np.sum(lights2))