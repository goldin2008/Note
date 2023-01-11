# 方法二 双向队列
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d = collections.deque()
        tmp = head
        while tmp.next: # 链表除了首元素全部加入双向队列
            d.append(tmp.next)
            tmp = tmp.next
        tmp = head
        while len(d): # 一后一前加入链表
            tmp.next = d.pop()
            tmp = tmp.next
            if len(d):
                tmp.next = d.popleft()
                tmp = tmp.next
        tmp.next = None # 尾部置空
 
# 方法三 反转链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None or head.next == None:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next # 分割右半边
        slow.next = None # 切断
        right = self.reverseList(right) #反转右半边
        left = head
        # 左半边一定比右半边长, 因此判断右半边即可
        while right:
            curLeft = left.next
            left.next = right
            left = curLeft

            curRight = right.next
            right.next = left
            right = curRight


    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下cur的下一个节点
            cur.next = pre # 反转
            pre = cur
            cur = temp
        return pre
