class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
         prev, curr = head, head
         stk = []
         size = 0
         while curr:
             stk.append(curr.val)
             curr = curr.next
         while prev:
             if prev.val != stk.pop():
                 return False
             prev = prev.next
         return True
