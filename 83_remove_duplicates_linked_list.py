class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        
        if head == None:
            return head

        while pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
                continue

            pointer = pointer.next

        return pointer

# POTENTIAL IMPROVEMENTS: none
