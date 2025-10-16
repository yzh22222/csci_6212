"""
CSCI 6212 Project 2 - Zihan Yang
Option 0: Quick selec deterministic (median of medians method)

Reference:
1. the use of time.perf_counter() referenced from below two websites
https://www.geeksforgeeks.org/python/python-measure-time-taken-by-program-to-execute/
https://www.tutorialspoint.com/how-to-measure-time-with-high-precision-in-python
"""

import time
import math
import numpy as np

"""
Quick Select Algortihm
"""

"""
Function insertion sort will be used when sort the small groups
iteratively inserting each element of an unsorted list into its correct position in
a sorted portion of  the list.
referenced from this website https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
"""
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        
        # Move elements greater than key to one position ahead
        while j >= 0 and A[j] > key:
            A[j+1] =  A[j]
            j -= 1
        A[j+1] = key
    return A


#a = [5,  20, 80, 15, 1]
#print(insertion_sort(a))


"""
Quick Select Funciton
returns k-th smallest element in the given array A
Approach referenced from textbook section 4.6.2
use of array_split referenced from this website
https://www.w3schools.com/python/numpy/numpy_array_split.asp
"""
def quick_select(A, k):
    if len(A) <= 5: #if size of array is smaller than 5
        A = insertion_sort(A)
        s = A[int(k) - 1]
        return s
    
    # Divide the array into groups of 5
    groups = np.array_split(A, 5)
    medians = []
    
    # Use inerstion sort sort the small gorups
    for g in groups:
        gsorted = insertion_sort(g)
        gs = len(gsorted)
        
        if gs % 2 == 0: #even
            mg = int((gsorted[gs//2] + gsorted[(gs//2)-1])/2)
        else:   #odd
            mg  = int(gsorted[len(gsorted) // 2])
        medians.append(mg)

    #find the median of medians
    mm = quick_select(medians, len(medians)//2 + 1)

    # Partition the array on the median of medians
    left = [e for e in A if e < mm]
    right = [e for e in A if e > mm]
    #print(left)
    #print(right)
    l = len(left)
    if k < l:
        return quick_select(left, k)
    elif k > l+1:
        return quick_select(right, k-l-1)
    else:
        return mm
        
    #print(groups)
    #print(medians)
    #print(mm)
    


"""
Function to generate array with random integer numbers in it with chosen size
the use of np.random referenced from this website
https://www.geeksforgeeks.org/python/how-to-create-a-matrix-of-random-integers-in-python/
m - max value of integer in the array, s - the size of the array
"""
def generate_a(m, s):
    return np.random.randint(m, size=(s))


#a = [10, 20 ,30, 50, 100, 1, 2, 3, 4, 5, 7, 90, 110, 200, 300, 150, 600, 10 , 30 ,20,90, 50]
#print(quick_select(generate_a(10, 30), 1))
#print(quick_select(a, len(a)+1))



"""
the function to get the actual elapsed time when run quick select
"""
def experimental_time(A, k):
    start = time.perf_counter()
    quick_select(A,k)
    end = time.perf_counter()
    etime_taken = end - start
    #print("for case n = " + str(n) + ": ")
    #print(time_taken)
    return etime_taken


# T(n) = cf(n)
#Time complexity - O(n)
# c = average of the sum of (the experimental_time of n / n)
"""
sumc = []
n = 10
while n <= 100000:
    A = generate_a(10, n)
    #print(len(A))
    tn = experimental_time(A, 1)
    cn =  tn / n
    print(cn)
    sumc.append(cn)
    n *= 10
c = sum(sumc)/len(sumc)
print("c= ", c)
"""

# run above while loop for 5 times and take the average of these 5 times c
# to make c more accurate
ca = [0.00015703161038507822, 0.0001561032448017795, 0.00015541947311448166
, 0.00015722547174611826, 0.00015649652449350107]
c = sum(ca) / len(ca)   # 0.00015645526490819174


"""
the function to calculate theoretical time with the theoretical time complexity
the theoretical time complexity of the given code is Θ(n)
c is the average of all the c get in experimental_time
"""
def theoretical_time(n):
    ttime_taken = c * n  # T(n) = cf(n)
    return ttime_taken
    


"""
while loop to generate the elapsed time of experimental and theoretical
for input n range from [10, 100000], multiply n by 10 each time
choose 1 for kth smallest number,
and choose 1000 for the maximum value of integer in the array 
"""

n = 10
while n <= 100000:
    #randomly generate array with 1000 as maximum value of integer and size of n
    A = generate_a(1000, n) 
    print("n = " + str(n))
    # for k, choose 1
    print("e = ", experimental_time(A, 1))
    print("t = ", theoretical_time(n))
    n *= 10 #multiply n by 10

#print("n = 10: ")
#print(experimental_time(10))
#print(theoretical_time(10))


