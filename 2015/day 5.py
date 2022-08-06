from re import I, L


with open('prompt.txt') as f:
    lines = f.readlines()
prompt = []
for i in lines:

    prompt += [i.split('\n')[0]]
nicecount = 0
for string in prompt:
    vowelcount = 0
    double = False
    rule3 = True
    if string[-1] in ['a','e','i','o','u']:
        vowelcount +=1
    for i in range(len(string)-1):
        if string[i] in ['a','e','i','o','u']:
            vowelcount +=1
        if string[i] == string[i+1]:
            double = True
        if string[i] + string[i+1] in ('ab', 'cd', 'pq', 'xy'):
            rule3 = False
    if vowelcount >=3 and double and rule3:
        nicecount +=1
print(nicecount)

# prompt = 'uurcxstgmygtbstg'
nicecount = 0
for string in prompt:
    rule1 = False
    rule2 = False
    for i in range(len(string)-1):
        for j in range(len(string)-1):
            if (string[i] == string[j]) and (string[i+1] == string[j+1]) and (abs(i-j) > 1):
                rule1 = True
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            rule2 = True
    if rule1 and rule2:
        nicecount +=1
        # print(string)

print(nicecount)