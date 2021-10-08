class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_freq = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in s_freq:
                s_freq[i] = 1
            else:
                s_freq[i]+= 1
                
        t_freq = {}
        for letter in t:
            if letter not in t_freq:
                t_freq[letter] = 1
            else:
                t_freq[letter]+= 1
        for letter in s_freq:
            if not t_freq.get(letter) or t_freq[letter] != s_freq[letter]:
                return False
            
        return True
