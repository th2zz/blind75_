class Solution:  # https://leetcode-cn.com/problems/counting-bits/
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += (n & 1)
            n >>= 1
        return res

    def hamming_weight(self, n):
        res = 0
        while n:
            res += 1
            n &= n - 1  # &n-1可以清零尾部1
        return res

    def countBits(self, n: int) -> List[int]:  # 返回n+1长度数组 位置i为i的二进制表示中1的个数  O(nlogn)
        return [self.hamming_weight(i) for i in range(n + 1)]

    def countBits1(self, n: int) -> List[int]:  # O(n) O(1)
        bits = [0]  # bits[i] = i的二进制中1的个数
        for i in range(1, n + 1):  # dynamic programming, i >> 1 = 1//2 precomputed最后一位之前的1的个数, i & 1 = 最后位是否为1
            bits.append(bits[i // 2] + (i & 1))
        return bits
