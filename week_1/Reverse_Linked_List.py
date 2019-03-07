class Stack_Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        # save current listked list to stack
        stack = []
        node_for_stack = head
        while node_for_stack is not None:
            stack.append(node_for_stack.val)
            node_for_stack = node_for_stack.next
            
        result = head # to save head so we can return
        for val in reversed(stack):
            result.val = val=
            result = result.next
        return head


# O(1) Space Solution
# it needs 3 pointers
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        prev_node = None
        current = head
        next_node = head
        
        while current:
            next_node = next_node.next # save before we brake connection
            current.next = prev_node # break it and reconnect to prev node
            prev_node = current 
            current = next_node # move on to next node to repeat
        return prev_node
    