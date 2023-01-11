#数组模拟
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list=[]
        while head: 
            list.append(head.val)
            head=head.next
        l,r=0, len(list)-1
        while l<=r: 
            if list[l]!=list[r]:
                return False
            l+=1
            r-=1
        return True   
      
#反转后半部分链表
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        # find mid point which including (first) mid point into the first half linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None

        # reverse second half linked list
        while slow:
            slow.next, slow, node = node, slow.next, slow

        # compare reversed and original half; must maintain reversed linked list is shorter than 1st half
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
