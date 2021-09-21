# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        
        if not l1:
            return l2
        elif not l2:
            return l1
            
        
        # loop while one of the lists have at least one element
        while l1 or l2:

            # if one of list is empty add element from other list
            if not l1 and l2:
                result.append(l2.val)
                l2 = l2.next
                
            elif not l2 and l1:
                result.append(l1.val)
                l1 = l1.next
                
            # if both lists have an element, compere the values
            elif  l1.val > l2.val:
                result.append(l2.val)
                l2 = l2.next
                
            elif  l1.val <= l2.val:
                result.append(l1.val)
                l1 = l1.next
                
        # reverse the values for new Node
        
        result.reverse()
        l3 = None
        for itr, ele in enumerate(result):
            
            if itr == 0:
                l3 = ListNode(ele)
            else:
                l3 = ListNode(ele, l3)
                
        return l3
