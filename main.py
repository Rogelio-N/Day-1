lines = []
with open('input.txt') as f:
    lines = f.readlines()
count = 0
for i in range(len(lines)-1):
    if  int(lines[i]) < int(lines[i+1]):
        count +=1
print(count)