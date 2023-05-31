"""
Given an sorted array A of size N.
Find number of elements which are less than or equal to given element X.



Example 1:

Input:
N = 6
A[] = {1, 2, 4, 5, 8, 10}
X = 9
Output:
5
"""

def countOfElements( a, n, x):
    count = 0
    for i in a:
        if(i<=x):
            count+=1
    print(count)
    return count

countOfElements([1, 2, 4, 5, 8, 10],6,9)