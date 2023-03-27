class Node:
    def __init__(self,key):
        self.key=key
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None

    def deletelinklist(self,del_data):
        temp=self.head
        while temp is not None:
            if temp.key==del_data:
                self.head=temp.next
                temp =None
                return 

        while temp is not None:
            if temp.key == del_data:
                break
            prev=temp
            temp=temp.next

        if temp==None:
            return
        prev.next=temp.next
        temp=None



    def printlinkedlist(self):
        # import pdb;pdb.set_trace()
        p= self.head
        while p:
            print(p.key)
            p=p.next

if __name__=='__main__':
    ll=LinkedList()
    ll.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)

    ll.head.next=second
    second.next=third
    third.next=fourth

    print(ll.printlinkedlist())
    ll.deletelinklist(1)
    ll.printlinkedlist()