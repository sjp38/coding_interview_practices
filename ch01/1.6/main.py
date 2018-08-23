#!/usr/bin/env python

"""
Rotate a matrix by 90 degree
"""

def rotate(matrix):
    N = len(matrix[0])
    ret = []
    for i in range(0, len(matrix)):
        ret.append([0] * N)

    for idx_r, r in enumerate(matrix):
        for idx_c, field in enumerate(r):
            row = N - 1 - idx_c
            col = idx_r
            ret[row][col] = field
    return ret

def pr_matrix(matrix):
    for r in matrix:
        print r

def pr_question_answer(q, a):
    print "questions:"
    pr_matrix(q)
    print "answer:"
    pr_matrix(a)

def is_same_matrix(a, b):
    if len(a) != len(b):
        return False
    for i, r in enumerate(a):
        if r != b[i]:
            return False
    return True

if __name__ == "__main__":
    questions = [
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                    [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16],
                    ],
                ]
    answers =    [
                   [
                        [3, 6, 9],
                        [2, 5, 8],
                        [1, 4, 7],
                    ],
                    [
                        [4, 8, 12, 16],
                        [3, 7, 11, 15],
                        [2, 6, 10, 14],
                        [1, 5, 9, 13],
                    ],
                ]

    for i, q in enumerate(questions):
        answer = rotate(q)
        if not is_same_matrix(answer, answers[i]):
            print "[FAIL]"
            pr_question_answer(q, answer)
            exit(1)
        print "[PASS]"
