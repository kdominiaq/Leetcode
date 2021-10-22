# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = 0
        nodes_to_save = []
        
        # counter nodes in the list
        while head:
            nodes_to_save.append(head.val)
            head = head.next
            itr += 1
            
        # decide which node from end is to remove, '-1' cuz nodes are itered by the '0'
        itr =  n - 1

        # reverse the value of the node for correct save 
        nodes_to_save.reverse()
        
        result = None
        for i, ele in enumerate(nodes_to_save):
            print(ele, i, itr)
            if i != itr and i == 0:
                result = ListNode(ele)
            elif i != itr and i != itr:
                result = ListNode(ele, result)
                    
        return result
