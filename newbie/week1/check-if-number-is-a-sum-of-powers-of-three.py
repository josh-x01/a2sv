class Solution:
    def checkPowersOfThree(self, n):
        m3 = math.floor((math.log(n, 3)))
        r3 = n
        for i in range(m3+1):
          k = m3 - i 
          if (r3 >= 3**k):
            r3 -= 3**k
        print(r3)
        if (r3 == 0):
          return True
        else:
          return False
                
        