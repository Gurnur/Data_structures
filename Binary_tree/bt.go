// Go program to implement binary tree

package main

import (
	"fmt"
)

type node struct {
	left *node
	right *node
	data int
}

type binaryTree struct {
	root *node
}

func (t *binaryTree) insert(data int) *binaryTree {
	if t.root == nil {
		t.root = &node{data: data, left: nil, right: nil}
	} else {
		t.root.insert(data)
	}
	return t
}

func (n *node) insert(data int) {
	if n == nil {
		return
	} else if data <= n.data {
		if n.left == nil {
			n.left = &node{left: nil, right: nil, data: data}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &node{left: nil, right: nil, data: data}
		} else {
			n.right.insert(data)
		}
	}
}

// Inorder traversal
func (n *node)printInorder(){
	if n == nil {
		return
	}
	n.left.printInorder()
	fmt.Printf("%d ", n.data)
	n.right.printInorder()
}

func main() {
	tree := &binaryTree{}
	tree.insert(100).
		insert(-20).
		insert(-50).
		insert(-15).
		insert(-60).
		insert(50).
		insert(60).
		insert(55).
		insert(85).
		insert(15).
		insert(5).
		insert(-10)
	tree.root.printInorder()
}