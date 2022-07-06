package main

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	res := twoSum([]int{2, 7, 11, 15}, 9)
	expected := []int{0, 1}
	if reflect.DeepEqual(res, expected) != true {
		t.Error("failed")
	}
	res = twoSum([]int{3, 2, 4}, 6)
	expected = []int{1, 2}
	if reflect.DeepEqual(res, expected) != true {
		t.Error("failed")
	}
}
