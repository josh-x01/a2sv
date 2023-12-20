class Solution:
  def reverseNumber(self, x: int):
    r_n = "".join(list(str(x))[::-1])
    return r_n
  def isPalindrome(self, x: int) -> bool:
      return str(x) == self.reverseNumber(x)