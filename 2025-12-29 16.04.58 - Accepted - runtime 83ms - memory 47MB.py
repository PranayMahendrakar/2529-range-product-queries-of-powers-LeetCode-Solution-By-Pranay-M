class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Get powers array - powers of 2 that sum to n (sorted non-decreasing)
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        
        # Compute prefix products
        # prefix[i] = powers[0] * powers[1] * ... * powers[i]
        m = len(powers)
        prefix = [1] * (m + 1)
        for i in range(m):
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD
        
        # For each query [left, right], answer = prefix[right+1] / prefix[left]
        # But we can't divide directly with modulo, so we compute product directly
        # Actually we need to compute product from scratch or use prefix sums of exponents
        
        # Better approach: since powers[i] are powers of 2, their product is 2^(sum of exponents)
        # Let exp[i] = log2(powers[i])
        exp = []
        for p in powers:
            e = 0
            while p > 1:
                p //= 2
                e += 1
            exp.append(e)
        
        # Prefix sum of exponents
        prefix_exp = [0] * (m + 1)
        for i in range(m):
            prefix_exp[i + 1] = prefix_exp[i] + exp[i]
        
        # Answer queries
        result = []
        for left, right in queries:
            total_exp = prefix_exp[right + 1] - prefix_exp[left]
            result.append(pow(2, total_exp, MOD))
        
        return result