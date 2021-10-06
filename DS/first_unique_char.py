"""
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = {}
        queue = []
        for i in range(len(s)):

            if s[i] in char_set and char_set[s[i]] in queue:
                queue.remove(char_set[s[i]])
            elif s[i] not in char_set:
                char_set[s[i]] = i
                queue.append(i)

                
        return queue[0] if queue else -1
