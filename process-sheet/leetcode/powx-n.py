class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, abs(n))

        if n % 2 == 0:
            half_pow = n // 2
            half_pow_result = self.myPow(x, half_pow)
            return half_pow_result * half_pow_result
        else:
            half_pow = ((n - 1) // 2)
            half_pow_result = self.myPow(x, half_pow)
            return x * half_pow_result * half_pow_result

        