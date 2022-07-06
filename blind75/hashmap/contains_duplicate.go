package main

import "fmt"

func containsDuplicate(nums []int) bool {
	visited := map[int]struct{}{}
	for _, v := range nums {
		a, b := visited[v]
		fmt.Printf("%+v %v\n", a, b)
		if _, has := visited[v]; has {
			return true
		}
		visited[v] = struct{}{}
	}
	return false
}

// func main() {
// 	containsDuplicate([]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2})
// }
