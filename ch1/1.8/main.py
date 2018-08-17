#!/usr/bin/env python

def is_substring(s1, s2):
    return s1 in s2

def is_rotated(s1, s2):
    common = s1[len(s1) / 4:-len(s1) / 4]
    return is_substring(s1, s2 + s2)

if __name__ == "__main__":
    questions = [("erbottlewat", "waterbottle"), ("abc", "bcd")]
    answers = [True, False]

    for i, q in enumerate(questions):
        if is_rotated(q[0], q[1]) != answers[i]:
            print "[FAIL] for '%s' and '%s'" % (q[0], q[1])
            exit(1)
        print "[PASS] for '%s' and '%s'" % (q[0], q[1])
