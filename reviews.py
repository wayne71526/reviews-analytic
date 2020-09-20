#讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 ==0:
			print(len(data))
print('總共', len(data), '筆')


#文字計數
count = {}
for d in data:
	words = d.split()
	for word in words:
		if word not in count:
			count[word] = 1 # 新增新的 key
		else:
			count[word] += 1
for word in count:
	if count[word] > 1000000:
		print(word, count[word])	
print(len(count))		

while True:
	word_count = input('請問你要查詢哪個字的次數：')
	if word_count == 'q':
		break
	print(word_count, '出現過的次數為', count[word_count])			 
print('感謝使用')


#平均長度
length = 0
for word in data:
	length = length + len(word)
average_length = length / len(data)	
print('平均長度為： ', average_length)


#小於100個字的筆數
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆')
print(new[0])


#有good的筆數
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(good), '筆')
print(good[0])


#也可以寫成
# 1 要放入清單的東西 2 for迴圈 3 判斷條件
good1 = [d for d in data if 'good' in d]	
print('總共有', len(good1), '筆')

bad = ['bad' in d for d in data]
print(bad)



