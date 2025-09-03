class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_beg(self,val):
        nn=Node(val)
        nn.next=self.head
        self.head=nn
    def ins_pos(self,val,pos):
        nn=Node(val)
        n=0
        if pos == 0:
            self.insert_beg(val)
            return
        curr=self.head
        while n<pos-1:
            curr=curr.next
        nn.next=curr.next
        curr.next=nn
    def ins_end(self,val):
        nn=Node(val)
        curr=self.head
        if self.head is None:
            self.head = nn
            return
        while curr.next:
            curr=curr.next
        curr.next=nn
    


