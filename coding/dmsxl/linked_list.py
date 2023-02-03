"""
设置一个虚拟头结点在进行删除操作
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head) #添加一个虚拟节点
        cur = dummy_head
        while(cur.next!=None):
            if(cur.next.val == val):
                # 如果找到了对应值,就跳过next到下一个next.next
                # 本来应该是cur.next = cur.next
                cur.next = cur.next.next #删除cur.next节点
            else:
                # 如果没有找到对应值,就遍历下一个node
                cur = cur.next
                # return到dummy节点的next node
        return dummy_head.next
