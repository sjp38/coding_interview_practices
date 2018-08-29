#!/usr/bin/env python

"""
Numbers are represented by a linked list.  Implement sum.
"""

import sys
sys.path.append("../")

from llist import *

def get_data_safe(node):
    if node == None:
        return 0
    return node.data

def sum_llst(head1, head2):
    ret = None
    n1 = head1
    n2 = head2
    carry = 0

    while n1 != None or n2 != None:
        d1 = get_data_safe(n1)
        d2 = get_data_safe(n2)

        digit = d1 + d2 + carry
        if digit > 10:
            digit -= 10
            carry = 1
        else:
            carry = 0

        if ret == None:
            ret = Node(digit)
        else:
            new_r = Node(digit)
            new_r.nxt = ret
            ret = new_r

        if n1 != None:
            n1 = n1.nxt
        if n2 != None:
            n2 = n2.nxt
    return ret

if __name__ == "__main__":
    questions = [ ([7,1,6], [5,9,2]) ]
    answers = [[9,1,2]]

    for i, q in enumerate(questions):
        llst1 = lst_to_llst(q[0])
        llst2 = lst_to_llst(q[1])
        llst = sum_llst(llst1, llst2)
        if llst_to_lst(llst) != answers[i]:
            print "[FAIL] %s + %s -> %s" % (q[0], q[1], llst_to_lst(llst))
            exit(1)
        print "[PASS] %s, %s" % (q[0], q[1])
