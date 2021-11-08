import numpy as np
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_ = head
        result = np.array([], int)
        final_result = None
        while head_:
            result = np.append(result, head_.val)
            head_ = head_.next
            
       
        result = np.sort(result)
        final_list_is_created = False
        
        for itr in range(result.size - 1, -1, -1):
            if not final_list_is_created:
                final_list = ListNode(int(result[itr]))
                final_list_is_created = True
            else:
                final_list  = ListNode(int(result[itr]), final_list)
        
        return final_list
