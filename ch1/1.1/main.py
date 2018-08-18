#!/usr/bin/env python

"""
Check whether all character in a string is unique
"""

def is_unique(string):
    """
    Returns true if all character in string is unique,
    false otherwise
    """
    sorted_str = ''.join(sorted(string))
    old_c = None
    for c in sorted_str:
        if old_c == None:
            old_c = c
            continue
        if c == old_c:
            return False
        old_c = c
    return True

if __name__ == "__main__":
    questions = ["", "aab", "abc", "ab", "bb", "abcdef", "abcdce"]
    answers = [True, False, True, True, False, True, False]

    for i, q in enumerate(questions):
        if is_unique(q) == answers[i]:
            print "PASS [%s] test" % q
            continue
        print "FAIL [%s] test" % q
        exit(1)
