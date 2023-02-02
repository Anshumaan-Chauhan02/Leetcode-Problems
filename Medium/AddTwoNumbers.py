# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1= l1.val + l1.next.val*10 + l1.next.next.val*100
        number2= l2.val + l2.next.val*10 + l2.next.next.val*100
        number1+=number2
        l1.val=number1%10
        number1= (int)(number1/10)
        l1.next.val= number1%10
        number1= (int)(number1/10)
        l1.next.next.val= number1%10 
        return l1
