"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [0]*numRows
        if numRows == 0:
            return []
        pascal[0] = [1]
        print(pascal)
        for i in range(1, numRows):
            print(pascal[i-1]+[0])
            zipped = zip(pascal[i-1]+[0], [0]+pascal[i-1])
            pascal[i] = ([x+y for (x,y) in zipped])
            
