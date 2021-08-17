# Objective 
# In this challenge, we will use loops to do some math.
# Task 
# Given an integer,n,print its 10 multiples. Each multiple n x i( where 1 <= i <= 10) should be printed on a new line in the form: n x i = result
# In simple words we have to print the table of the given number (don't include n x 0 = 0)
# We can range() function to do that and rest is just the calculation.


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
for x in range(1,11):
    print(n,"x",x,"=",n*x  )
    
