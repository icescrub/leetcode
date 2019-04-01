# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        traverse_fast = head
        traverse_slow = head
        
	# There are two pointers here. One traverses at twice the speed. When the fast pointer gets to the end, the slow pointer will be at the midpoint.

        while traverse_fast.next != None and traverse_fast.next.next != None:
            traverse_fast = traverse_fast.next.next
            traverse_slow = traverse_slow.next

	# If the length of the linked list is even, then there are two middle nodes. Select the one to the right of the slow pointer.        
        if traverse_fast.next != None:
            traverse_slow = traverse_slow.next
            
	# Print out all values from the middle pointer to the end of the LL.

        serialization = []
        while traverse_slow.next != None:
            serialization.append(traverse_slow.val)
            traverse_slow = traverse_slow.next
        
        serialization.append(traverse_slow.val)
        return serialization
