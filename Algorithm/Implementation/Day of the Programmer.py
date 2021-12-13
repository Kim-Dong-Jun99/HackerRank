#!/bin/python3

import math
import os
import random
import re
import sys
import calendar

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    dayCount = 0
    if year > 1918:
        dayCount = 0
        for i in range(1,13):
            if dayCount + list(calendar.monthrange(year, i))[1] > 256:
                if i < 10:
                    return str(256-dayCount)+'.0'+str(i)+'.'+str(year)
                else:
                    return str(256-dayCount)+'.'+str(i)+'.'+str(year)
            elif dayCount + list(calendar.monthrange(year, i))[1] == 256:
                if i < 10:
                    return str(list(calendar.monthrange(year,i))[1])+'.0'+str(i)+'.'+str(year)
                else :
                    return str(list(calendar.monthrange(year, i)[1])+'.'+str(i)+'.'+str(year))
            else:
                dayCount += list(calendar.monthrange(year, i))[1]
    elif year == 1918:
        for i in range(1,13):
            if i == 2:
                dayCount += 15
            else:
                if dayCount + list(calendar.monthrange(year, i))[1] > 256:
                    if i < 10:
                        return str(256-dayCount)+'.0'+str(i)+'.'+str(year)
                    else:
                        return str(256-dayCount)+'.'+str(i)+'.'+str(year)
                elif dayCount + list(calendar.monthrange(year, i))[1] == 256:
                        if i < 10:
                            return str(list(calendar.monthrange(year,i))[1])+'.0'+str(i)+'.'+str(year)
                        else :
                            return str(list(calendar.monthrange(year, i)[1])+'.'+str(i)+'.'+str(year))
                else:
                     dayCount += list(calendar.monthrange(year, i))[1]
    else:
        for i in range(1,13):
            if i == 2:
                if year % 4 == 0:
                    dayCount += 29
                else:
                    dayCount += 28
            else:
                if dayCount + list(calendar.monthrange(year, i))[1] > 256:
                    if i < 10:
                        return str(256-dayCount)+'.0'+str(i)+'.'+str(year)
                    else:
                        return str(256-dayCount)+'.'+str(i)+'.'+str(year)
                elif dayCount + list(calendar.monthrange(year, i))[1] == 256:
                        if i < 10:
                            return str(list(calendar.monthrange(year,i))[1])+'.0'+str(i)+'.'+str(year)
                        else :
                            return str(list(calendar.monthrange(year, i)[1])+'.'+str(i)+'.'+str(year))
                else:
                     dayCount += list(calendar.monthrange(year, i))[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
