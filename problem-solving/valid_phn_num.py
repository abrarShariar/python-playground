#hacker rank problem
# https://www.hackerrank.com/contests/pythonist/challenges/validating-the-phone-number/problem

import re
pattern = r'([789])\d{9}$'

line = raw_input()
line = int(line)

for i in range(line):
    inputNum = raw_input()

    if re.match(pattern,inputNum):
        print 'YES'
    else:
        print 'NO'
