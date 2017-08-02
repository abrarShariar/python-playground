#Hacker rank
# https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort/problem
#take input

N,M = raw_input().split()
N = int(N)
M = int(M)

table = [[0 for x in range(M)] for y in range(N)]

for i in range(0,N):
    inputData = raw_input().split()
    inputData = map(lambda x: int(x), inputData)
    table[i] = inputData

K = raw_input()
K = int(K)

#making 2 parallel arrays
# valueList = [table[0][K],table[1][K],table[2][K],table[3][K],table[4][K]]

valueList = list()
for i in range(N):
    valueList.insert(i,table[i][K])

indexList = range(0,N)

#do bubble sort here of valueList and indexList
isSorted = False
while not isSorted:
    isSorted = True
    for i in range(1,N):
       if valueList[i-1] > valueList[i]:
            isSorted = False
            temp = valueList[i]
            valueList[i] = valueList[i-1]
            valueList[i-1] = temp
            #alter value
            temp = indexList[i]
            indexList[i] = indexList[i-1]
            indexList[i-1] = temp

#output
for i in range(0,N):
    for j in range(0,M):
        print table[indexList[i]][j],
    print

