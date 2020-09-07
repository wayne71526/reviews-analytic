data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 ==0:
			print(len(data))
print('總共', len(data), '筆')

length = 0
for word in data:
	length = length + len(word)
average_length = length / len(data)	
print('平均長度為： ', average_length)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))
print(good[0])		




