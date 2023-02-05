 #反转后半部分链表
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Find the end of first half and reverse second half.

        # find mid point which including (first) mid point into the first half linked list
        first_half_end = self.end_of_first_half(head)
        # reverse second half linked list
        second_half_start = self.reverse_list(first_half_end.next)

        # compare reversed and original half; must maintain reversed linked list is shorter than 1st half
        left = head
        right = second_half_start
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        pre = None # dummy head
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


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
