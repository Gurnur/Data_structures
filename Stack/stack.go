package main

import (
	"fmt"
)

type Stack struct {
	stack []string
}

func NewStack(stack []string) *Stack {
	return &Stack{stack: stack}
}

func (st *Stack) Push (str string){
	st.stack = append(st.stack, str)
}

func (st *Stack) Pop() {
	if len(st.stack) > 0 {
		n := len(st.stack) - 1
		fmt.Printf("Top element is: %d", st.stack[n])
		st.stack[n] = ""
		st.stack = st.stack[:n]
	}
}

func main(){
	newstack := NewStack([]string{"a", "c", "d", "e", "q"})
	newstack.Push("b")
	newstack.Pop()
	fmt.Printf("%+q", newstack.stack)
}