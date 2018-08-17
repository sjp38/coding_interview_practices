#!/usr/bin/env python

"""
Request: Receive two strings and distinguish whether one of the strings is a
permutation of the other.
"""

def is_permutations(str1, str2):
    sorted1 = ''.join(sorted(str1))
    sorted2 = ''.join(sorted(str2))

    if sorted1 == sorted2:
        return True
    return False

if __name__ == "__main__":
    questions = [("", ""), ("a", "a"), ("a", "b"), ("abc", "bac"), ("abc",
                    "def")]
    answers = [True, True, False, True, False]

    for i, q in enumerate(questions):
        if is_permutations(q[0], q[1]) != answers[i]:
            print "[FAIL] test '%s' and '%s'" % (q[0], q[1])
            exit(1)
        print "[PASS] test '%s' and '%s'" % (q[0], q[1])
