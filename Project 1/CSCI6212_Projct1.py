"""
CSCI 6212 Project 1 - Zihan Yang
Option 0

Reference:
1. the use of time.perf_counter() referenced from below two websites
https://www.geeksforgeeks.org/python/python-measure-time-taken-by-program-to-execute/
https://www.tutorialspoint.com/how-to-measure-time-with-high-precision-in-python

2. the use of log2() referenced from below website
https://www.digitalocean.com/community/tutorials/python-log-function-logarithm
"""

import time
import math

"""
the function with the given code from Option 0
"""
def nested_loop(n):
    # Assume the length of arrary a and b both are n
    a = list(range(n))
    b = list(range(n))
    Sum = 0 # initialize sum
    
    j = 2
    while j < n:
        k = j
        while k < n:
            Sum += a[j] * b[k]
            k = k * k
        j =  2 * j
    

"""
the function to get the actual elapsed time when run the given code
"""
def experimental_time(n):
    start = time.perf_counter()
    nested_loop(n)
    end = time.perf_counter()
    etime_taken = end - start
    #print("for case n = " + str(n) + ": ")
    #print(time_taken)
    return etime_taken


# T(n) = cf(n)
# Θ(logn)
T0 = experimental_time(10)
f_10 = math.log2(10) #f(10)
c = T0/f_10  #the constant c
#print(c)


"""
the function to calculate theoretical time with the theoretical time complexity
the theoretical time complexity of the given code is Θ(logn)
"""
def theoretical_time(n):
    ttime_taken = c * math.log2(n)  # T(n) = cf(n)
    return ttime_taken

"""
while loop to generate the elapsed time of experimental and theoretical
for input n range from [10, 100000000], multiply n by 10 each time
"""
n = 10
while n <= 100000000:
    print("n = " + str(n))
    print(experimental_time(n))
    print(theoretical_time(n))
    n *= 10 #multiply n by 10

#print("n = 10: ")
#print(experimental_time(10))
#print(theoretical_time(10))


    
"""
# case 1: test n = 5
start1  = time.perf_counter()
nested_loop(10000)
end1 = time.perf_counter()
time1 = end1 - start1
print(time1)
"""

#experimental_time(10000)

