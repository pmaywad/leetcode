'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        _dict={}
        res=[]
        for i in nums1:
            if i not in _dict:
                _dict[i]=1
            else:
                _dict[i]+=1
        for i in nums2:
            if i in _dict:
                res.append(i)
                _dict[i]-=1
                if _dict[i]==0:
                    _dict.pop(i)
        return res
