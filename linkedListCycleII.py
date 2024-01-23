def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        if fast == None or fast.next == None:
            return None

        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        
        return fast
