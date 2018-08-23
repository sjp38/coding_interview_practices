#!/usr/bin/env python

"""
Remove duplicated string from unsorted linked list
"""

import sys
sys.path.append("../")

from llist import *

def kth_to_last(head, k):
    if head == None:
        return head

    n = head
    while k > 0 and n != None:
        k -= 1
        n = n.nxt
    return n

if __name__ == "__main__":
    questions = [([1, 2, 3, 4, 5], 3), ([1, 2], 1), ([1], 1), ([], 2)]
    answers = [[4, 5], [2], [], []]

    for i, q in enumerate(questions):
        q_ = lst_to_llst(q[0])
        answer = kth_to_last(q_, q[1])
        answer = llst_to_lst(answer)
        if answers[i] != answer:
            print "[FAIL] q: %s, a: %s" % (q, answer)
            exit(1)
        print "[PASS] %s" % q[0]
