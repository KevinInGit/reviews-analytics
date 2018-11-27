# -*- coding:utf-8 -*-

data = []
count = 0
with open('/Users/kevin/Desktop/read/food.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('文档读取完毕，共有', len(data), '个资料')

sum_len = 0
for d in data:
    sum_len += len(d)

print('平均每个字符串长度是', sum_len/len(data))