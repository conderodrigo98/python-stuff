str1 = input("First string: ")
str2 = input("Second string: ")
d = [[0 for j in range(len(str2))] for i in range(len(str1))]

def ind(i,j):
	if str1[i] == str2[j]:
		return 0
	else:
		return 1

#let's build the first row and column as a base
for j in range(len(str2)):
	d[0][j] = j
for i in range(len(str1)):
	d[i][0] = i

for i in range(1, len(str1)):
	for j in range(1, len(str2)):
		d[i][j] = min([d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + ind(i,j)])

print(d[len(str1) - 1][len(str2) - 1])
