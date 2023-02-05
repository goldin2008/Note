"""
设置一个虚拟头结点在进行删除操作

while fast.next and fast.next.next:
    fast = fast.next.next
    slow = slow.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

区别在slow停在的位置，第1个要从slow.next断，第2个要从slow断!!!
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


# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre
