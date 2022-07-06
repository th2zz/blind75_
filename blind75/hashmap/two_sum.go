package main

func twoSum(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	val2idx := make(map[int]int, len(nums))
	for i, n := range nums {
		if _, exist := val2idx[target-n]; exist {
			return []int{val2idx[target-n], i}
		}
		val2idx[n] = i
	}
	return []int{-1, -1}
}

// func main() {
// 	fmt.Println("test")
// 	res := twoSum([]int{2, 7, 11, 15}, 9)
// 	fmt.Printf("%v\n", res)
// }
