class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2, ans=ListNode()):
        ans_head = ans
        while list1 and list2 :
            if list1.val < list2.val :
                ans.next = list1
                ans = list1
                list1 = list1.next
                #print(ans.val)
            else:
                ans.next = list2
                ans = list2
                list2 = list2.next 
                #print(ans.val)
        if list1 or list2:
            if list1:
                ans.next = list1
            else:
                ans.next = list2   
        return ans_head.next

            
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solu =  Solution()
anslinkedlist = solu.mergeTwoLists(list1,list2)
#print(solu.mergeTwoLists(list1,list2))
while anslinkedlist is not None:
    print(anslinkedlist.val)
    anslinkedlist = anslinkedlist.next
    
