import numpy as np

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize variables
        final_list_is_created = False
        final_list = None
        result_odd = np.array([])
        result_even = np.array([])
        index = 0
        
        # if given head is empty 
        if head == None:
            return None
        
        # if given head has only one variable
        if head.next == None:
            final_list = ListNode(head.val)
            return final_list
        
        # creating two lists for odd and even number of nodes
        while head:
            if index % 2 == 0:
                result_even = np.append(head.val, result_even)
            else:
                result_odd = np.append(head.val, result_odd)
            head = head.next 
            index += 1
            
        # for the first loop creating new, next time adding variables to createdlist
        for itr in range(len(result_odd)):
            if not final_list_is_created:
                final_list = ListNode(int(result_odd[itr]), ListNode(int(result_even[itr])))
                final_list_is_created = True
            else:
                final_list  = ListNode(int(result_odd[itr]), ListNode(int(result_even[itr]), final_list))
                
        return final_list
