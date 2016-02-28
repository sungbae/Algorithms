# Name: Sung Bae
# Email: Sung.Bae@colorado.edu
# SUID: 101412061
#

import sys
import random
import time
import matplotlib.pyplot as plt

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort
    n = len(lst)
    if (n == 1):
        return lst
    else:
        t = (n/2)
        l1 = mergeSort(lst[0:t])
        l2 = mergeSort(lst[t:n])
        return merge(l1, l2)
def merge(a, b):
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    result = []
    while (i < m and j < n):
        if (a[i] <= b[j]):
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1
    while (i < m):
        result.append(a[i])
        i = i + 1
    while (j < n):
        result.append(b[j])
        j = j + 1
    return result

#------ Quick Sort --------------
def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
    n = len(lst)
    if (n < 2):
        return lst
    pivot = random.choice(lst)
    lst_left = []
    lst_mid = []
    lst_right = []
    i = 0
    while (i < n):
        if (lst[i] < pivot):
            lst_left.append(lst[i])
            i = i + 1
        elif (lst[i] == pivot):
            lst_mid.append(lst[i])
            i = i + 1
        else:
            lst_right.append(lst[i])
            i = i + 1
    return quickSort(lst_left) + lst_mid + quickSort(lst_right)

# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity

##################################################
# I have commented out certain parts of the code #
# depending upon which sort to display           #
##################################################
def runningTimeCases():
    i = 5
    j = 0
    ###lst_insertion = []
    ###lst_merge = []
    lst_quick = []
    ###avg_insertion_lst = []
    ###worst_insertion_lst = []
    ###avg_merge_lst = []
    ###worst_merge_lst = []
    avg_quick_lst = []
    worst_quick_lst = []
    n = []
    while (i < 505):
        while (j < 20):
            r_lst = generateRandomList(i)
            ###insertion_time = measureRunningTimeComplexity(insertionSort, r_lst)
            ###lst_insertion.append(insertion_time)
            ###merge_time = measureRunningTimeComplexity(mergeSort, r_lst)
            ###lst_merge.append(merge_time)
            quick_time = measureRunningTimeComplexity(quickSort, r_lst)
            lst_quick.append(quick_time)
            j = j + 1
        ###avg_insertion = sum(lst_insertion)/float(len(lst_insertion))
        ###avg_insertion_lst.append(avg_insertion)
        ###worst_insertion = max(lst_insertion)
        ###worst_insertion_lst.append(worst_insertion)
        ###avg_merge = sum(lst_merge)/float(len(lst_merge))
        ###avg_merge_lst.append(avg_merge)
        ###worst_merge = max(lst_merge)
        ###worst_merge_lst.append(worst_merge)
        avg_quick = sum(lst_quick)/float(len(lst_quick))
        avg_quick_lst.append(avg_quick)
        worst_quick = max(lst_quick)
        worst_quick_lst.append(worst_quick)
        n.append(i)
        j = 0
        i = i + 5
    ###plt.plot(n, avg_insertion_lst, 'bs')
    ###plt.plot(n, worst_insertion_lst, 'ro')
    ###plt.plot(n, avg_merge_lst, 'bs')
    ###plt.plot(n, worst_merge_lst, 'ro')
    plt.plot(n, avg_quick_lst, 'bs')
    plt.plot(n, worst_quick_lst, 'ro')
    plt.ylabel('average/worst-case time (seconds)')
    plt.xlabel('lists size n')
    ###plt.title('Time table of insertionSort')
    ###plt.title('Time table of mergeSort')
    plt.title('Time table of quickSort')
    plt.show()
runningTimeCases()
