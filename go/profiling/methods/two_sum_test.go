package methods

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	tests := []struct {
		nums  []int
		total int
		want  [2]int
	}{
		{
			nums:  []int{2, 7, 11, 15},
			total: 9,
			want:  [2]int{0, 1},
		},
		{
			nums:  []int{3, 2, 4},
			total: 6,
			want:  [2]int{1, 2},
		},
		{
			nums:  []int{3, 3},
			total: 6,
			want:  [2]int{0, 1},
		},
	}
	for _, tt := range tests {
		got := TwoSum(tt.nums, tt.total)
		if !reflect.DeepEqual(got, tt.want) {
			t.Errorf("got %v want %v", got, tt.want)
		}
	}

}

func TestTwoSumBrute(t *testing.T) {
	tests := []struct {
		nums  []int
		total int
		want  [2]int
	}{
		{
			nums:  []int{2, 7, 11, 15},
			total: 9,
			want:  [2]int{0, 1},
		},
		{
			nums:  []int{3, 2, 4},
			total: 6,
			want:  [2]int{1, 2},
		},
		{
			nums:  []int{3, 3},
			total: 6,
			want:  [2]int{0, 1},
		},
	}
	for _, tt := range tests {
		got := TwoSumBrute(tt.nums, tt.total)
		if !reflect.DeepEqual(got, tt.want) {
			t.Errorf("got %v want %v", got, tt.want)
		}
	}

}

func TestTwoSumAbdulSamet(t *testing.T) {
	tests := []struct {
		nums  []int
		total int
		want  []int
	}{
		{
			nums:  []int{2, 7, 11, 15},
			total: 9,
			want:  []int{0, 1},
		},
		{
			nums:  []int{3, 2, 4},
			total: 6,
			want:  []int{1, 2},
		},
		{
			nums:  []int{3, 3},
			total: 6,
			want:  []int{0, 1},
		},
	}
	for _, tt := range tests {
		got := TwoSumAbdulSamet(tt.nums, tt.total)
		if !reflect.DeepEqual(got, tt.want) {
			t.Errorf("got %v want %v", got, tt.want)
		}
	}

}

func BenchmarkTwoSumBrute(b *testing.B) {
	for i := 0; i < b.N; i++ {
		TwoSumBrute([]int{2, 7, 11, 15}, 9)
	}
}

func BenchmarkTwoSum(b *testing.B) {
	for i := 0; i < b.N; i++ {
		TwoSum([]int{2, 7, 11, 15}, 9)
	}
}

func BenchmarkTwoSumAbdulSamet(b *testing.B) {
	for i := 0; i < b.N; i++ {
		TwoSumAbdulSamet([]int{2, 7, 11, 15}, 9)
	}
}
