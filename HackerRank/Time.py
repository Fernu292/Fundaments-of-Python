import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = 0 
    horary = ''
    if(s.endswith('AM')):
        
        horary = ''
        for i in range( len(horary) ):
            hour = s.replace(horary[i], '')
        
            i+=1
        
    return hour
    
   

n = str( input())
result = timeConversion(n)

print(result)


