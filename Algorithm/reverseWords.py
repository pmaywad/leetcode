"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        
        for i in range(len(words)):
            words[i] = self.reverseWord(words[i])
    
            
        return (" ").join(words)
                  
    def reverseWord(self, word):
        word = word[::-1]
        return word
                  
