#!/usr/bin/env python

"""
Partition a linked list around a value X, such that all nodes less than X come
before all nodes greater than or equal to X.
"""

import sys
sys.path.append("../")

from llist import *

def mv_to_head(head, prev, node):
    prev.nxt = node.nxt
    node.nxt = head.nxt
    head.nxt = node

def partition(head, val):
    if head == None or head.nxt == None:
        return

    # Seek middle
    n = head
    while n.nxt != None:
        if n.data >= val:
            break
        n = n.nxt
    if n.nxt == None:
        return

    # If head is middle, record old head
    old_head = None
    if n == head:
        # Assume that -1 is the smallest number that can exist
        sentinel = Node(-1)
        sentinel.nxt = head
        prev = head
        old_head = head
        prev_old_head = sentinel
        head = sentinel
    else:
        prev = n

    # Move larger node to next of head
    n = n.nxt
    while n.nxt != None:
        if n.data < val:
            mv_to_head(head, prev, n)
            if old_head:
                prev_old_head = n
        prev = n
        n = n.nxt
    # For last node which is smaller than the value
    if n.data < val:
        mv_to_head(head, prev, n)
        if old_head:
            prev_old_head = n

    # Restore old head
    if old_head:
        # s->a->b->oh->c
        new_node = Node(old_head.data)
        new_node.nxt = old_head.nxt
        prev_old_head.nxt = new_node
        old_head.nxt = sentinel.nxt.nxt
        old_head.data = sentinel.nxt.data

if __name__ == "__main__":
    questions = [([1, 4, 3, 3, 2], 3), ([3,5,8,5,10,2,1], 5), ([], 3),
            ([1,3],2), ([3,1],2)]
    answers = [[1,2,4,3,3], [3,1,2,5,8,5,10], [], [1,3], [1,3]]

    for i, q in enumerate(questions):
        llst = lst_to_llst(q[0])
        partition(llst, q[1])
        if llst_to_lst(llst) != answers[i]:
            print "[FAIL] %s,%d -> %s" % (q[0], q[1], llst_to_lst(llst))
            exit(1)
        print "[PASS] %s, %d" % (q[0], q[1])
