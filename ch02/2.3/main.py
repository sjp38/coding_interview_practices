#!/usr/bin/env python

"""
Delete a node in the middle of a singly linked list, given only access to that
node.
"""

import sys
sys.path.append("../")

from llist import *

def delete(head, val):
    n = head
    while n.nxt != None:
        if n.data == val:
            n.data = n.nxt.data
            n.nxt = n.nxt.nxt
        n = n.nxt

if __name__ == "__main__":
    questions = [([1, 2, 3, 4, 5], 3)]
    answers = [[1,2,4,5]]

    for i, q in enumerate(questions):
        llst = lst_to_llst(q[0])
        delete(llst, q[1])
        if llst_to_lst(llst) != answers[i]:
            print "[FAIL] %s,%d -> %s" % (q[0], q[1], llst_to_lst(llst))
            exit(1)
        print "[PASS] %s, %d" % (q[0], q[1])
