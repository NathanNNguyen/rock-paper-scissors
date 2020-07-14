class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        # 1. create the Node
        new_node = Node(value)
        # what do we do if self.tail = None?
        if self.tail and self.head is None:
            # set the new node to be the tail
            self.head = new_node
            self.tail = new_node
        else:
            # these steps assuming that tail is already referring to a Node (not None)
            # 2. set the old tail's next to point to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to the new Node
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # if we have a single element in a linked list
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head ref
            self.head = None
            # delete the linked list's tail ref
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # if we have a non-empty linked list
        # loop through the linked list until we get to the Node before the tail
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        # at this point, `current` is the node right before the tail
        # then set self.tail to be None
        val = self.tail.get_value()
        self.tail = None
        # set self.tail to the Node right before it
        self.tail = current
        return val

    # def traverse
