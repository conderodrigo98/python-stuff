import json

class maze:
	array = []
	def set(self,i,j,n):
		self.array[i][j] = n

#read the maze from text file:
with open('maze.txt') as f:
	myMaze = maze()
	aux = list(f)
	for line in aux:
		splitedLine = list(line)
		if splitedLine[len(splitedLine) - 1] == '\n':
			splitedLine.pop()
		myMaze.array.append(splitedLine)
	print(myMaze.array)

#global variables
end = [0, 0, 1]
notEnded = 1


f1 = open("log1.txt", "r+")
f2 = open("log2.txt", "r+")


#recursive function to solve maze
def solve(i, j, count):
	string = " "+str(i)+"   "+str(j)+"\n"
	f1.write(string)
	f2.write(json.dumps(myMaze.array)+"\n")
	#already at the end?
	if notEnded:
			#currently at the end?
			if myMaze.array[i][j] == 'E':
				global notEnded
				global end
				notEnded = 0
				end = [i, j, count - 1]
			else:
				myMaze.set(i,j,str(count))
				count += 1
				#north
				if (i - 1 >= 0) and (myMaze.array[i - 1][j] in ['0', 'E']):
					solve(i - 1, j, count)
				#east
				if (j + 1 < len(myMaze.array[0])) and (myMaze.array[i][j + 1] in ['0', 'E']):
					solve(i, j + 1, count)
				#south
				if (i + 1 < len(myMaze.array)) and (myMaze.array[i + 1][j] in ['0', 'E']):
					solve(i + 1, j, count)
				#west
				if (j - 1 >= 0) and (myMaze.array[i][j - 1] in ['0', 'E']):
					solve(i, j - 1, count)


solve(0,0,1)
path = ""
done = 0
x = end[0]
y = end[1]
c = end[2]
while c > 1:
	if (x - 1 >= 0) and (myMaze.array[x - 1][y] == str(c)):
		x -= 1
		path = 'S' + path
	elif (y + 1 < len(myMaze.array[0])) and (myMaze.array[x][y + 1] == str(c)):
		y += 1
		path = 'W' + path
	elif (x + 1 < len(myMaze.array)) and (myMaze.array[x + 1][y] == str(c)):
		x += 1
		path = 'N' + path
	else:
		y -= 1
		path = 'E' + path
	c -= 1
if [x,y] == [0,1]:
	path = 'E' + path
else:
	path = 'S' + path

print(path)

f1.close()
f2.close()