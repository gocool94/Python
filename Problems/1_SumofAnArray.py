"""
Sum of Array Elements

Given an integer array arr of size n, you need to sum the elements of arr.

Example 1:

Input:
n = 3
arr[] = {3 2 1}
Output: 6
"""

def sumElement(arr,n):
    count = 0
    for i in arr:
        count+=i
    return count
