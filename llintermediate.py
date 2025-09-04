# Intermediate Level
# 3. Search & Access Operations
# Search for element - Return true/false if element exists

# Access by index - Get element at specific position

# Find middle node - Use two-pointer technique

# Get nth node from end - Use two-pointer approach

# Find maximum/minimum - Traverse and track extreme values
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def search(self,el):
        curr=self.head
        while curr:
            if curr.val==el:
                return True
            else:
                curr=curr.next
        return -1
    def pos(self,p):
        curr=self.head
        n=0
        while curr:
            if n==p:
                return curr.val if curr else None
            else:
                n+=1
                curr=curr.next
        return "Out of Bounds"
    def mid(self):
        slow=self.head
        fast=self.head
        if not self.head:
            return -1
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.val
    def n_end(self,n):
        slow=self.head
        fast=self.head
        x=0
        while x<n:
            if not fast:
                return "out of bounds"
            fast=fast.next
            x+=1
        while fast.next:
            slow=slow.next
            fast=fast.next
        return slow.val
    def maxmin(self):
        Max=float("-inf")
        Min=float("inf")
        if not self.head:
            return "Empty list"
        curr=self.head
        while curr:
            Min=min(Min,curr.val)
            Max=max(Max,curr.val)
        return[Max,Min]

