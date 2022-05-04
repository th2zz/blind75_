// https://leetcode-cn.com/problems/sum-of-two-integers/
func getSum(a int, b int) int {
    for b != 0 {
        carry := (a & b) << 1
        a = a ^ b
        b = carry
    }
    return a
}
