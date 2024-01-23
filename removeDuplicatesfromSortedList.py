if head == None or head.next == None:
            return head
        prev = curr = head
        curr = curr.next
        while curr:
            temp = curr.next
            if prev.val == curr.val:
                prev.next = temp
            else:
                prev = curr
            curr = temp
        return head

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


cur = head
while cur:
    while cur.next and cur.next.val == cur.val:
        cur.next = cur.next.next
    cur = cur.next
return head
