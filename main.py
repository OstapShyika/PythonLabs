from Student import Student


class Node:

    def __init__(self, data: Student):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __str__(self):
        node = self.head
        nodes = []

        while node:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")

        return " -> ".join(nodes)

    def add_last(self, node):

        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def search_by_surname(self, wtf):
        current_node = self.head

        while current_node:
            if current_node.data.surname == wtf:
                print(current_node.data)
                return True
            current_node = current_node.next

        return False

    def insertion_sort_by_rating(self):
        sorted = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            sorted = sorted_insert(sorted, current_node)
            current_node = next_node

        self.head = sorted
        node = self.head
        nodes = []

        while node:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")

        return " -> ".join(nodes)


def sorted_insert(head, new_node):

    if head is None or head.data.rating >= new_node.data.rating:

        new_node.next = head
        head = new_node

    else:

        current_node = head
        while (current_node.next is not None and
               current_node.next.data.rating < new_node.data.rating):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    return head


s1 = Student("a", "Astab", "D", "18.48.283893", 2)
s2 = Student("b", "Astab8", "D", "18.48.283893", 3)
s3 = Student("c", "Astab4", "D", "18.48.283893", 1)

linkedlist = LinkedList([s1, s2])
linkedlist.add_last(Node(s3))
print(linkedlist)
print(linkedlist.insertion_sort_by_rating())
linkedlist.search_by_surname("a")
