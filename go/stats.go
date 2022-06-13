package main

import (
	"fmt"
)

func main() {
	s := 0
	fmt.Scanln(&s)
	fmt.Println("Enter of array elements")
	elements := make([]float64, s)
	for i := 0; i < s; i++ {
		fmt.Scanln(&elements[i])
	}
	fmt.Println("Entered Array of elements:", elements)
	result := 0

	for i := 0; i < s; i++ {
		float64(result) += elements[i]

	}
	fmt.Println("Sum of elements of array:", result)
	fmt.Println("Average of elements of array:", float64(result)/float64(s))
}
