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
        freq_1 = {}
        freq_2 = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] in freq_1:
                freq_1[nums1[i]]+=1
            else:
                freq_1[nums1[i]] = 1
                
        for i in range(len(nums2)):
            if nums2[i] in freq_2:
                freq_2[nums2[i]]+=1
            else:
                freq_2[nums2[i]] = 1
                
        for i in freq_1:
            print(i)
            if i in freq_2 and freq_1[i] <= freq_2[i]:
                freq_2[i] -= freq_1[i]
                for j in range(freq_1[i]):
                    res.append(i)
            elif i in freq_2 and freq_1[i] > freq_2[i]:
                freq_1[i] -= freq_2[i]
                for j in range(freq_2[i]):
                    res.append(i)
                
        return res
