import hashlib

prompt = 'yzbqklnj'
Solved = False
digest = hashlib.md5(prompt.encode())
result = digest.hexdigest()
# print(result)

count = 0
while not Solved:
    count +=1
    digest = hashlib.md5((prompt + str(count)).encode())
    result = digest.hexdigest()
    if str(result)[:5] == '00000':
        Solved = True
print(count)
Solved = False
count = 0
while not Solved:
    count +=1
    digest = hashlib.md5((prompt + str(count)).encode())
    result = digest.hexdigest()
    if str(result)[:6] == '000000':
        Solved = True

print(count)