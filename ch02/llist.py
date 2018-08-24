#!/usr/bin/env python

class Node:
    nxt = None
    data = None

    def __init__(self, value):
        self.nxt = None
        self.data = value

    def __str__(self):
        values = []

        n = self
        while True:
            values.append(n.data)
            if n.nxt == None:
                break
            n = n.nxt
        return "->".join([str(x) for x in values])

    def to_pylist(self):
        values = []

        n = self
        while True:
            values.append(n.data)
            if n.nxt == None:
                break
            n = n.nxt
        return values

    def append(self, node):
        n = self
        while n.nxt != None:
            n = n.nxt
        n.nxt = node

    def delete(self, value):
        head = self
        n = head

        if n.data == value:
            return n.nxt

        while n.nxt != None:
            nxt = n.nxt
            if nxt.data == value:
                n.nxt = nxt.nxt
                return head
            n = n.nxt
        return head

def llst_to_lst(llst):
    if llst == None:
        return []
    return llst.to_pylist()

def lst_to_llst(lst):
    if len(lst) < 1:
        return None
    llst = Node(lst[0])
    for n in lst[1:]:
        llst.append(Node(n))
    return llst


if __name__ == "__main__":
    print Node(12)
