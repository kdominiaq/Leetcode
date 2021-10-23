# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = list()
        
        # prepare list of list for spilt into list of k elements
        merged_result = list()
        merged_result.append([])
        
        # save all values from Nodes to list
        while head:
            result.append(head.val)
            head = head.next
        

        # split list into list of lists which contain reversed element
        itr_list = 0
        for itr, ele in enumerate(result):
            merged_result[itr_list].append(ele)
            if (itr + 1) % k == 0:
                merged_result.append([])
                merged_result[itr_list].reverse()
                itr_list += 1

        
        # merge list of lists in one list, clear result list
        result.clear()
        
        for ele in merged_result:
            print(ele)
            result += ele
        
        # reverse list for save values into final ListNode
        result.reverse()
        l3 = None
        for itr, ele in enumerate(result):
            if itr == 0:
                l3 = ListNode(ele)
            else:
                l3 = ListNode(ele, l3)
        
        return l3
