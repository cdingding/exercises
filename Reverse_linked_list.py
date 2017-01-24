
def reverse(head):
    current = head
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return current


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            head.next, new_head, head = new_head, head, head.next # look Ma, no temp vars!
        return new_head

    def reverseList(self, head, prev = None): #good now
        if head == None:
            return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)

    def reverseList(self, head):
        return self.doReverse(head, None)
    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)

    def reverseList(self, item, tail=None):
        if item is None:
            return tail
        else:
            next = item.next
            item.next = tail
            return Solution().reverseList(next, item)

# class LinkedList:
#     def __init__ (self, value, next = None):
#         self.value = value
#         self.next = next
#     def __repr__ (self):
#         return 'LinkedList({}, {})'.format(self.value, repr(self.next))

def reverseList(head):
    current = head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return current

def reverseList(head,tail=None):
    if head is None:
        return tail
    current = head
    next = current.next
    current.next = tail
    return reverseList(next, head)

# def myadd(x, y=None):
#     return x + y
# x = 2
# print myadd(x,2)

# if __name__ == '__main__':
