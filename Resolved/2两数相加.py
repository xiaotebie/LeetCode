"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
我的解法：
需要两个函数：
1： def nodetonum(self, node: Optional[ListNode]) -> int:
第一个函数将链表倒序转换成整数，例如：
链表：2，3，4，5
结果:5432

2：def turn_to_Node(self, mynum) -> ListNode:
第二个函数将两个链表相加得到的整数结果，再倒置转换成列表
主要逻辑为，将整数除以十取小数位为列表的节点，一个个循环链接即可刚好倒置输出为需要的链表结果
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 计算结果
        result = 0
        reslisnode = None
        result = self.nodetonum(l1) + self.nodetonum(l2)
        answer = self.turn_to_Node(result)
        return answer

    def nodetonum(self, node: Optional[ListNode]) -> int:
        i = 0
        res = 0
        while node is not None:
            res = node.val * (10 ** i) + res
            i = i + 1
            node = node.next
        return res

    def turn_to_Node(self, mynum) -> ListNode:
        node = ListNode(mynum % 10)  # 提供初始值
        headofnode = node

        mynum = mynum // 10
        while mynum != 0:
            # 此时个位的数字
            resent = mynum % 10
            # 下一个循环的数字
            mynum = mynum // 10
            node.next = ListNode(resent)  # 创建新的 ListNode 并提供初始值
            node = node.next
        return headofnode


"""
Gpt的解法：
同时操作两个链表

原理：
处理时，两个链表左对齐开始操作：
x = p.val if p is not None else 0
y = q.val if q is not None else 0
然后按位相加，使用变量carry来保存进位，加到后一个的链表节点中去：
sum = carry + x + y
新的carry值为sum的除以10取整
carry = sum // 10
实际的节点值为sum除以十的余数：
current.next = ListNode(sum % 10)
因为例如：6+9=15,则进一位，除以10的余数5为当前节点值

"""


class Solution1:
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        p, q, current = l1, l2, dummy_head
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy_head.next


"""
最高效的方法：链表递归：
"""


class Solution2:
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val += l2.val  # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:
            l1.next = self.addTwoNumbers2(ListNode(l1.val // 10), l1.next)
            l1.val %= 10

        l1.next = self.addTwoNumbers2(l1.next, l2.next)
        return l1


# 测试
l11 = ListNode(2)
l11.next = ListNode(4)
l11.next.next = ListNode(3)

l22 = ListNode(5)
l22.next = ListNode(6)
l22.next.next = ListNode(4)
# l11 = [2, 4, 3]
# l22 = [5, 6, 4]
a = Solution1()
b = a.addTwoNumbers1(l11, l22)
while b is not None:
    print(b.val)
    b = b.next
