#!/usr/bin/env python

"""
Request: Receive enough space and substitute all ' ' with '%20'
"""

def subst_space(str_list, size):

    if size == 0:
        return
    i_str = size - 1
    while i_str >= 0 and str_list[i_str] == ' ':
        i_str -= 1

    i_buf = size - 1
    while i_str >= 0:
        if str_list[i_str] != ' ':
            str_list[i_buf] = str_list[i_str]
            i_buf -= 1
            i_str -= 1
            continue
        str_list[i_buf] = '0'
        str_list[i_buf - 1] = '2'
        str_list[i_buf - 2] = '%'
        i_buf -= 3
        i_str -= 1

if __name__ == "__main__":
    questions = ["", "ab", "a b  ", "a bc d    "]
    answers =   ["", "ab", "a%20b", "a%20bc%20d"]

    for i, q in enumerate(questions):
        question = list(questions[i])
        subst_space(question, len(question))
        if question != list(answers[i]):
            print "[FAIL] '%s' question, answer '%s'" % (
                    questions[i], ''.join(question))
            exit(1)
        print "[PASS] '%s' question, answer '%s'" % (
                questions[i], ''.join(question))
