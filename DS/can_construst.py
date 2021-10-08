"""
383. Ransom Note

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_freq = {}
        for i in ransomNote:
            if i not in ransom_freq:
                ransom_freq[i] = 1
            else:
                ransom_freq[i]+= 1
                
        mag_freq = {}
        for letter in magazine:
            if letter not in mag_freq:
                mag_freq[letter] = 1
            else:
                mag_freq[letter]+= 1
        for letter in ransom_freq:
            if not mag_freq.get(letter) or mag_freq[letter] < ransom_freq[letter]:
                return False
            
        return True
