def removeNfromEnd(head,n):
    if head is None or head.next is None:
        return None
    runner = head
    striker = head
    for _ in range(n):
        runner = runner.next
    if runner is None:
        head = striker.next
        return head
    while runner.next:
        runner = runner.next 
        striker = striker.next
    striker.next = striker.next.next
    return head 