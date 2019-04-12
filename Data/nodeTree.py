#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__mtime__ = '2019/4/11'
"""

class TreeNode:
    '''二叉数节点定义'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class OperationTree:
    def create(self, List):
        '''插入操作'''

        root = TreeNode(List[0])
        lens = len(List)
        if lens >= 2:
            root.left = self.create(List[1])
        if lens >=3:
            root.right = self.create(List[2])

        return root

    def query(self, root, data):
        if root == None:
            return False
        if root.var == data:
            return True
        elif root.left:
            return self.query(root.left, data)
        elif root.right:
            return self.query(root.right, data)

    def PreOrder(self, root):
        if root == None:
            return
        print(root.val, end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self, root):
        if root == None:
            return
        self.InOrder(root.left)
        print(root.val, end=" ")
        self.InOrder(root.right)

    def BacOrder(self, root):
        if root == None:
            return
        self.BacOrder(root.left)
        self.BacOrder(root.right)
        print(root.val, end=" ")

    def BFS(self, root):
        if root == None:
            return
        queue = []

        queue.append(root)

        while queue:
            print(queue)
            print("\n")
            currentNode = queue.pop(0)
            print(currentNode.val, end=' ')
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


    def DFS(self, root):
        if root == None:
            return

        stack = []
        stack.append(root)

        while stack:
            currentNode = stack.pop()

            print(currentNode.val, end =" ")

            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)


if __name__ == '__main__':
    List1 = [1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
    op = OperationTree()
    tree1 = op.create(List1)

    # print('先序打印: ', end = ' ')
    # op.PreOrder(tree1)
    # print("\n")
    # print("中序打印: ", end=" ")
    # op.InOrder(tree1)
    # print("\n")
    # print("后序打印: ", end=" ")
    # op.BacOrder(tree1)
    print("\n")
    print("广度优先: ", end=" ")
    op.BFS(tree1)
    # print("\n")
    # print("深度优先: ", end=" ")
    # op.DFS(tree1)
