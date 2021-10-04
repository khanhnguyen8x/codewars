class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        current = head
        node_list = list()
        data_set = set()

        while current:
            if current.data not in data_set:
                node_list.append(current)
                data_set.add(current.data)

            current = current.next


        if len(node_list) == 1:
            node_list[0].next = None
            return node_list[0]

        current = node_list[0]
        for i in range(1,len(node_list)):
            node = node_list[i]
            current.next = node
            current = node
        current.next = None

        return node_list[0]


if __name__ == "__main__":
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    head = mylist.removeDuplicates(head)
    mylist.display(head)
