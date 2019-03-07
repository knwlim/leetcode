# recursive - 68 ms
class Recursive_Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# iterative - 48 ms
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cuurent = head = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                cuurent.next = l1
                l1 = l1.next
            else:
                cuurent.next = l2
                l2 = l2.next
            cuurent = cuurent.next
        cuurent.next = l1 or l2
        return head.next

# https://leetcode.com/problems/merge-two-sorted-lists/
