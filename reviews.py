data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 ==0:
			print(len(data))
print('總共', len(data), '筆')




