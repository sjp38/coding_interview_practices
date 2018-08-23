#!/usr/bin/env python

"""
Remove duplicated string from unsorted linked list
"""

import sys
sys.path.append("../")

from llist import *

def rm_dups(head):
    if head == None:
        return head

    values = []
    n = head
    while True:
        if n == None:
            return head
        if n.data in values:
            head = head.delete(n.data)
            n = n.nxt
            continue
        values.append(n.data)
        n = n.nxt

    return head

if __name__ == "__main__":
    questions = [[1, 2, 3, 2], [1, 2, 3, 4], [1], []]
    answers = [[1, 3, 2], [1, 2, 3, 4], [1], []]

    for i, q in enumerate(questions):
        q_ = lst_to_llst(q)
        answer = rm_dups(q_)
        answer = llst_to_lst(answer)
        if not answers[i] == answer:
            print "[FAIL] q: %s, a: %s" % (q, answer)
            exit(1)
        print "[PASS] %s" % q
