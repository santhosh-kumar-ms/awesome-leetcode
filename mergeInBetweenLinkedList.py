def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = list1 
        aNode = bNode = lastNode = None
        index = 0
        j = list2
        while i != None:
            if index == (a - 1):
                aNode = i
            elif index == (b + 1):
                bNode = i
            i = i.next
            index += 1
        while j != None:
            lastNode = j
            j = j.next
        aNode.next = list2
        lastNode.next = bNode
        return list1
