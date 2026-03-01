from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head: Optional[ListNode]) -> None:
    """辅助函数：打印链表"""
    p = head
    while p:
        if p.next == None:
            print(p.val)
        else:
            print(p.val, end=',')
        p = p.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

        示例:
            输入:head = [1,2,3,4,5]
            输出:[5,4,3,2,1]
        '''
        p = None
        q = head
        while q:
            n = q.next
            q.next = p
            p = q
            q = n
        return p
    
    # 首先「递」到链表末尾，把末尾节点作为新链表的头节点 rev_head
    # 然后在「归」的过程中，把经过的节点依次插在新链表的末尾（尾插法）
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 判断 head is None 是为了兼容一开始链表就是空的情况
        if head is None or head.next is None:
            return head  # 链表末尾，即下面的 rev_head
        rev_head = self.reverseList(head.next)  # 「递」到链表末尾，拿到新链表的头节点
        tail = head.next  # 在「归」的过程中，head.next 就是新链表的末尾
        tail.next = head  # 把 head 插在新链表的末尾
        head.next = None  # 如果不写这行，新链表的末尾两个节点成环，这俩节点互相指向对方
        return rev_head

    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
        请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

        示例:
            输入:head = [1,2,3,4,5], left = 2, right = 4
            输出:[1,4,3,2,5]
        '''
        n = ListNode(next=head)
        p0: Optional[ListNode] = n
        for _ in range(left - 1):
            p0 = p0.next

        p: Optional[ListNode] = p0.next
        q = None
        for _ in range(right - left + 1):
            x = p.next
            p.next = q
            q = p
            p = x
        p0.next.next = p
        p0.next = q
        
        return n.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
        k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，
        那么请将最后剩余的节点保持原有顺序。
        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

        示例:
            输入:head = [1,2,3,4,5], k = 2
            输出:[2,1,4,3,5]
        '''
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        
        o = ListNode(next=head)
        p0 = o

        q = None
        p = o.next
        while n >= k:
            n -= k
            for _ in range(k):
                x = p.next
                p.next = q
                q = p
                p = x
            
            x = p0.next
            p0.next.next = p 
            p0.next = q
            p0 = x
        return o.next
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        给你单链表的头结点 head ，请你找出并返回链表的中间结点。
        如果有两个中间结点，则返回第二个中间结点。

        示例:
            输入:head = [1,2,3,4,5]
            输出:[3,4,5]
        '''
        p, q = head, head
        while q and q.next:
            p = p.next
            q = q.next.next
        return p
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        给你一个链表的头节点 head ，判断链表中是否有环。
        如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
        为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置
        （索引从 0 开始）。注意:pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
        如果链表中存在环 ，则返回 true 。 否则，返回 false 。
        示例:
            输入:head = [3,2,0,-4], pos = 1
            输出:true
        '''
        p = head
        q = head
        while p and p.next:
            p = p.next.next
            q = q.next
            if p == q:
                return True
        return False
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
        为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        如果 pos 是 -1,则在该链表中没有环。
        注意:pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
        不允许修改 链表。
        示例:
            输入:head = [3,2,0,-4], pos = 1
            输出:返回索引为 1 的链表节点
        '''
        p, q = head, head
        while p and p.next:
            p: Optional[ListNode] = p.next.next
            q: Optional[ListNode] = q.next
            if q == p:
                while q != head:
                    q = q.next
                    head = head.next
                return q
        return None

    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        给定一个单链表 L 的头节点 head ，单链表 L 表示为：
        L0 → L1 → … → Ln - 1 → Ln
        请将其重新排列后变为：
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

        示例:
            输入:head = [1,2,3,4]
            输出:[1,4,2,3]
        '''
        p, q = head, head
        while p and p.next:
            p = p.next.next
            q = q.next
        m = None
        while q:
            n = q.next
            q.next = m
            m = q
            q = n
        head2 = m
        while head2.next:
            nex1 = head.next
            nex2 = head2.next
            head.next = head2
            head2.next = nex1
            head = nex1
            head2 = nex2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

        示例:
            输入:head = [1,2,3,4,5], n = 2
            输出:[1,2,3,5]
        '''
        x = ListNode(next=head)
        p = x
        q = x
        for _ in range(n):
            q = q.next
        
        while q.next:
            p = p.next
            q = q.next
        
        p.next = p.next.next
        return x.next
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        给定一个已排序的链表的头 head , 删除原始链表中所有重复数字的节点，只留下不同的数字 。
        返回 已排序的链表 。

        示例:
            输入:head = [1,2,3,3,4,4,5]
            输出:[1,2,5]
        '''
        x = ListNode(next=head)
        p = x
        while p.next and p.next.next:
            n = p.next.val
            if p.next.next.val == n:
                while p.next and p.next.val == n:
                    p.next = p.next.next
            else:
                p = p.next
        return x.next

if __name__ == '__main__':
    soultion = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    soultion.reorderList(head=head)
    print_linked_list(head)
    