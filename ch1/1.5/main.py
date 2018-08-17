#!/usr/bin/env python

"""
Compress a string using <character><number of repeats> if compressed string is
shorter than original string.
"""

def compress(string):
    if len(string) < 3:
        return string

    ret = string[0]
    nr_chars = 1
    len_numbers = 0
    for i in range(1, len(string)):
        if ret[-1] == string[i]:
            nr_chars += 1
            continue
        ret += str(nr_chars)
        if i < len(string):
            ret += string[i]
            nr_chars = 1
    ret += str(nr_chars)
    if len(ret) < len(string):
        return ret
    return string

if __name__ == "__main__":
    questions = ["", "abc", "aaa", "abbc", "aaab", "aaaabcccccddddddd",
                "abccccccccccd"]
    answers = ["", "abc", "a3", "abbc", "aaab", "a4b1c5d7", "a1b1c10d1"]

    for i, q in enumerate(questions):
        answer = compress(q)
        if answer != answers[i]:
            print "[FAIL] question: '%s', answer: '%s'" % (q, answer)
            exit(1)
        print "[PASS] question: '%s', answer: '%s'" % (q, answer)
