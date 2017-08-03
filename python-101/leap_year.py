

x = int(raw_input())
isLeapYear = False


if x % 4 == 0:
    isLeapYear = True
    if x % 100 == 0:
        isLeapYear = False
        if x % 400 == 0:
                isLeapYear = True
        else:
            isLeapYear = False
    # else:
    #     isLeapYear = False
else:
    isLeapYear = False

print isLeapYear





