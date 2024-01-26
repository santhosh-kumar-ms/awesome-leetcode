def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
         dummy = ListNode(next = head)
         prev, curr = dummy, head
         while curr and curr.next:
             if curr.val == curr.next.val:
                 while curr and curr.next and curr.val == curr.next.val:
                     curr = curr.next
                 curr = curr.next
                 prev.next = curr
             else:
                 prev = prev.next
                 curr = curr.next
         return dummy.next
