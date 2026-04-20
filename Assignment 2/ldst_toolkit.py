class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data

        self.data[self.size] = value
        self.size += 1
        print(f"Added {value} | size={self.size}, capacity={self.capacity}")

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None

        value = self.data[self.size - 1]
        self.size -= 1
        print(f"Removed {value} | size={self.size}, capacity={self.capacity}")
        return value

    def show(self):
        print("Array:", [self.data[i] for i in range(self.size)])


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete_value(self, value):
        curr = self.head

        if curr and curr.value == value:
            self.head = curr.next
            return

        prev = None
        while curr and curr.value != value:
            prev = curr
            curr = curr.next

        if not curr:
            print("Value not found")
            return

        prev.next = curr.next

    def show(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        print("SLL:", result)


class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        node = DNode(value)

        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node
        node.prev = curr

    def insert_after(self, target, value):
        curr = self.head

        while curr:
            if curr.value == target:
                node = DNode(value)
                node.next = curr.next
                node.prev = curr

                if curr.next:
                    curr.next.prev = node

                curr.next = node
                return

            curr = curr.next

        print("Target not found")

    def delete_position(self, pos):
        if not self.head:
            print("List is empty")
            return

        curr = self.head

        if pos == 0:
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        while curr and count < pos:
            curr = curr.next
            count += 1

        if not curr:
            print("Position out of range")
            return

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def show(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        print("DLL:", result)


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            print("Stack empty")
            return None

        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if not self.head:
            return None
        return self.head.value


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, value):
        node = Node(value)

        if not self.rear_node:
            self.front_node = self.rear_node = node
            return

        self.rear_node.next = node
        self.rear_node = node

    def dequeue(self):
        if not self.front_node:
            print("Queue empty")
            return None

        value = self.front_node.value
        self.front_node = self.front_node.next

        if not self.front_node:
            self.rear_node = None

        return value

    def front(self):
        if not self.front_node:
            return None
        return self.front_node.value


def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.peek() is None or stack.pop() != pairs[ch]:
                return False

    return stack.peek() is None


if __name__ == "__main__":

    print("Task 1 Dynamic Array")
    arr = DynamicArray(2)
    for i in range(1, 11):
        arr.append(i)
    arr.show()

    arr.pop()
    arr.pop()
    arr.pop()
    arr.show()

    print("\nTask 2 Singly Linked List")
    sll = SinglyLinkedList()
    sll.insert_begin(10)
    sll.insert_begin(20)
    sll.insert_begin(30)
    sll.show()

    sll.insert_end(40)
    sll.insert_end(50)
    sll.show()

    sll.delete_value(20)
    sll.show()

    print("\nTask 2 Doubly Linked List")
    dll = DoublyLinkedList()
    for i in range(1, 5):
        dll.insert_end(i)
    dll.show()

    dll.insert_after(2, 99)
    dll.show()

    dll.delete_position(1)
    dll.show()

    dll.delete_position(3)
    dll.show()

    print("\nTask 3 Stack from Singly Linked List ")
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)

    print("Top:", st.peek())
    print("Pop:", st.pop())
    print("Top:", st.peek())

    print("\nTask 3 Queue from Singly Linked List")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Front:", q.front())
    print("Dequeue:", q.dequeue())
    print("Front:", q.front())

    print("\n Task 4 Paranthesis Check")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(f"{t} -> {is_balanced(t)}")