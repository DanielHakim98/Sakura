package methods

func TwoSum(nums []int, total int) [2]int {
	ref := make(map[int]int)
	for i, n := range nums {
		if i == 0 {
			ref[total-n] = i
			continue
		}

		if complementIdx, ok := ref[n]; ok {
			return [2]int{complementIdx, i}
		}

		ref[total-n] = i
	}
	return [2]int{0, 0}
}

func TwoSumBrute(nums []int, total int) [2]int {
	ref := make(map[int]int)
	for i, n := range nums {
		for idxKey, elementVal := range ref {
			if elementVal+n == total {
				return [2]int{idxKey, i}
			}
		}
		ref[i] = n
	}
	return [2]int{0, 0}
}

// Compared with this code snippet:
// https://github.com/Abdulsametileri/pprof-examples/blob/main/benchmarking/main.go

// Reference for reading:
// https://blog.stackademic.com/profiling-go-applications-in-the-right-way-with-examples-e784526e9481
func TwoSumAbdulSamet(nums []int, target int) []int {
	numsByIndex := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		complement := target - nums[i]

		if val, ok := numsByIndex[complement]; ok {
			return []int{val, i}
		}

		numsByIndex[nums[i]] = i
	}

	return []int{0, 0}
}
