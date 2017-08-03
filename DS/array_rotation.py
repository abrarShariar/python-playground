
#take input
T = int(raw_input())
for index in range(0,T):
    N = int(raw_input())
    A = raw_input().split()
    A = map(lambda x: int(x),A)

    limit = len(A)
    rotateTime = 0

    def rotateArray(arr):
        lastElement = arr[len(arr)-1]
        for index in range(1,len(arr)):
            arr[-index] = arr[-(index+1)]
        A[0] = lastElement
        return arr

    while rotateTime < limit-1:
        rotateTime += 1
        A = rotateArray(A)
        try:
            del A[-rotateTime]
        except IndexError:
            del A[0]

    #output
    for item in A: print item














# T = int(raw_input())
#
# for line in range(T):
#     size = int(raw_input())
#     data = raw_input().split()
#     data = map(lambda x: int(x),data)
#
#     print data
#
#     while len(data) > 1:
#         data = list(reversed(data))
#         data = data[:-1]
#
#     for x in data: print x
#
#
#
#
#
