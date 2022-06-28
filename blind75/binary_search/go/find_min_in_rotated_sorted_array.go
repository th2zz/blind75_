package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func findMin(nums []int) int {
	if len(nums) == 0 {
		return -1
	}
	start, end := 0, len(nums)-1
	for start+1 < end {
		mid := (start + end) / 2
		if nums[mid] > nums[end] {
			start = mid
		} else {
			end = mid
		}
	}
	return min(nums[start], nums[end])

}

// func main() {
// 	arr := []int{3, 4, 5, 1, 2}
// 	fmt.Println(findMin(arr))
// 	arr = []int{4, 5, 6, 7, 0, 1, 2}
// 	fmt.Println(findMin(arr))
// 	arr = []int{11, 13, 15, 17}
// 	fmt.Println(findMin(arr))
// }
