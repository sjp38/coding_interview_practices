#!/usr/bin/env python

def set_zero_col_row(matrix):
    N = len(matrix[0])

    target_rows = []
    target_cols = []

    for ir, r in enumerate(matrix):
        for ic, c in enumerate(r):
            if c == 0:
                target_rows.append(ir)
                target_cols.append(ic)

    for r in target_rows:
        matrix[r] = [0] * N
    for ir, r in enumerate(matrix):
        for c in target_cols:
            r[c] = 0
    return matrix

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
                        [1, 2, 3],
                        [4, 5, 6],
                        [0, 8, 9],
                    ],
                    [
                        [1, 2, 3, 4],
                        [5, 0, 7, 8],
                        [9, 0, 11, 12],
                        [13, 14, 15, 16],
                    ],
                    [
                        [1, 2, 3, 4],
                        [5, 0, 0, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16],
                    ],
                    [
                        [1, 2, 3, 4],
                        [5, 0, 0, 8],
                        [9, 10, 0, 12],
                        [13, 14, 15, 16],
                    ],
                ]
    answers =    [
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                    [
                        [0, 2, 3],
                        [0, 5, 6],
                        [0, 0, 0],
                    ],
                    [
                        [1, 0, 3, 4],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [13, 0, 15, 16],
                    ],
                    [
                        [1, 0, 0, 4],
                        [0, 0, 0, 0],
                        [9, 0, 0, 12],
                        [13, 0, 0, 16],
                    ],
                    [
                        [1, 0, 0, 4],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [13, 0, 0, 16],
                    ],
                ]

    for i, q in enumerate(questions):
        answer = set_zero_col_row(q)
        if not is_same_matrix(answer, answers[i]):
            print "[FAIL]"
            pr_question_answer(q, answer)
            exit(1)
        print "[PASS]"

