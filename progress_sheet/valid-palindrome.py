class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = "zxcvbnmasdfghjklqwertyuiopQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        pal = [i.lower() for i in s if i in alp]
        pal_rev = pal.copy()
        pal_rev.reverse()
        pal_rev = "".join(pal_rev)
        pal = "".join(pal)
        if (pal == pal_rev):
            return True
