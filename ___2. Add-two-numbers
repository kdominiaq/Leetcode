# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        first = True
        temporary_list = []
        val_step = 0
        while l1 or l2:
            val_step = 0
            
            if l1:
                val_step += l1.val
            if l2:
                val_step += l2.val

            val_step += temp

            # checking sum of values if more then 10 must pass the 1 to next Node
            if val_step >= 10:
                temp = 1
                val_step = val_step % 10
            else:
                temp = 0
                
            # creating the first Node and adding next Node to existed Node
            
            temporary_list.append(val_step)
            # pushing Node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # if Node is not exist, but the previos value was grater then 10, must add lat Node with 1 val
            if not l1 and not l2 and temp == 1:
                temporary_list.append(1)

        # list is reversed then expected
        temporary_list.reverse()
        
        # creating ListNode with values and next Node
        for ele in temporary_list:
            if first:
                l3 = ListNode(ele)
                first = False
            else:
                l3 = ListNode(ele, l3)
        
        return l3
