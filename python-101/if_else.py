
inputNum = raw_input()
inputNum = int(inputNum)

if inputNum%2 != 0:
    print 'Weird'
elif (inputNum%2 == 0) and (inputNum>=2 and inputNum<=5):
    print 'Not Weird'
elif (inputNum % 2 == 0) and (inputNum >= 6 and inputNum <= 20):
    print 'Weird'
elif (inputNum % 2 == 0) and (inputNum > 20):
    print 'Not Weird'



