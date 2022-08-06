from numpy import sort


with open('prompt.txt') as f:
    lines = f.readlines()
prompt = lines[0]
# print(prompt)
x = 0
y = 0

houses_visited = []
santa = 1
robot_santa = 0
for i in prompt:
    if i == '<':
        x -=1
    if i == '>':
        x -=1 
    if i == '^':
        y +=1
    if i == 'v':
        y -=1
    houses_visited += [(x,y)]
x = 0
y = 0
x1 = 0
y1 = 0
houses_visited = []
for i in prompt:
    if i == '<':
        x -= (1 * santa)
        x1 -= (1 * robot_santa)
    if i == '>':
        x += (1 * santa)
        x1 += (1 * robot_santa)
    if i == '^':
        y += (1 * santa)
        y1 += (1 * robot_santa)
    if i == 'v':
        y -= (1 * santa)
        y1 -= (1 * robot_santa)
    santa = (santa + 1) % 2
    robot_santa = (robot_santa + 1) % 2
    houses_visited += [(x1, y1)]
    houses_visited += [(x,y)]

print(set(houses_visited))
print(len(set(houses_visited)))
