# -*- coding:utf-8 -*-

data = []
count = 0
with open('/Users/kevin/Desktop/read/food.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print(len(data))
print(data)

