class Solution:  # https://leetcode-cn.com/problems/reverse-bits/
    def reverseBits(self, n):  # reverse n(32bit uint) in binary format and return reversed value (in decimal)
        res = 0
        for i in range(32):  # after 32 rounds, n's lsb is at first pos
            res = (res << 1) | (n & 1)  # res * 2左移1位后 把最后一位写成n最后一位
            n >>= 1  # n right shift 1 pos
        return res

        # m1, m2, m3, m4 = 0x55555555, 0x33333333, 0x0f0f0f0f, 0x00ff00ff
        # n = n >> 1 & m1 | (n & m1) << 1
        # n = n >> 2 & m2 | (n & m2) << 2
        # n = n >> 4 & m3 | (n & m3) << 4
        # n = n >> 8 & m4 | (n & m4) << 8
        # return n >> 16 | n << 16 & 0xffff0000
