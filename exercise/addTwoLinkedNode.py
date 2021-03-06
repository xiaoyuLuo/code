# -*- coding: utf-8 -*-#

"""
 Name:         addTwoNum
 Description:  https://leetcode-cn.com/problems/add-two-numbers/
 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 Author:       xiaoyuLuo
 Date:         2019/4/24
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print_linked_list(self, l1):
        head = l1
        print(head.val, end="")
        while head.next:
            head = head.next
            print("->" + str(head.val), end="")
        print("\n")

    def addTwoNumbers(self, l1, l2):
        """

        :param l1:  ListNode
        :param l2:  ListNode
        :return: ListNode
        """

        re = ListNode(0)
        result = re
        carry = 0
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s//10
            re.next = ListNode(s%10)
            re = re.next
            if(l1 != None): l1 = l1.next
            if(l2 != None): l2 = l2.next

        if(carry > 0):
            re.next = ListNode(1)

        return  result.next
       
    def addTwoNumbersSecond(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        # 两个链表都没有，但是有carry的时候说明要进一位
        if not (l1 or l2): return ListNode(1) if carry else None
        # 同一位置相加
        if l1: self.print_linked_list(l1)
        if l2: self.print_linked_list(l2)
        #     l1 = None or 1的结果是 l1 = 1
        l1, l2 = l1 or ListNode(0), l2 or ListNode(0)
        print(l1.val)
        print(l2.val)
        val = l1.val + l2.val + carry
        l1.val, l1.next = val % 10, self.addTwoNumbers(l1.next, l2.next, val > 9)
        return l1

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    solution = Solution()
    solution.print_linked_list(l1)
    solution.print_linked_list(l2)
    l3 = solution.addTwoNumbers(l1, l2)
    solution.print_linked_list(l3)
    l4 = solution.addTwoNumbersSecond(l1, l2)
    solution.print_linked_list(l4)
