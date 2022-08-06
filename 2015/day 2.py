from numpy import sort


with open('prompt.txt') as f:
    lines = f.readlines()
prompt = []
for i in lines:

    prompt += [i.split('\n')[0]]

paper_needed = 0
ribbon = 0
for i in prompt:
    string = i.split('x')
    l = int(string[0])
    w = int(string[1])
    h = int(string[2])
    area = 2*l*w + 2*l*h + 2*w*h
    smallest_side = sort([l*w, l*h, w*h])[0]

    smallest_dim = sort([l,w,h])[0]
    med_dim = sort([l,w,h])[1]
    paper_needed += area + smallest_side
    ribbon += 2*smallest_dim + 2*med_dim + l*w*h
print(paper_needed)
print(ribbon)