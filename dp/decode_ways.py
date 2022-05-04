class Solution:  # https://leetcode-cn.com/problems/decode-ways/
    # give a digit str, return #ways to decode it to ascii letter str. A=1,B=2...
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n  # f[i]:= 前i个字符的decode ways
        for i in range(1, n + 1):
            curr_char = s[i - 1]
            if curr_char != '0':  # 使用了一个字符 前i - 1个字符有f[i - 1]种方式 使用1个字符贡献的decode ways为f[i-1]
                f[i] += f[i - 1]  # 例如1,2,3 = 12 3 or 1 2 3  3加到12或1 2上都还是原来的方案数量
            if i >= 2:
                prev_char = s[i - 2]
                group2_str = prev_char + curr_char
                if prev_char != '0' and int(group2_str) <= 26:  # s[i-2:i]
                    f[i] += f[i - 2]
        return f[n]