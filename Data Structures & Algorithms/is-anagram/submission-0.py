class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        elif sorted(s) == sorted(t):
            return True
        else:
            return False