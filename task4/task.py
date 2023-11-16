import sys
from math import log2


def task():
    table = [[0 for i in range(37)] for i in range(13)]
    table_H = [[0 for i in range(37)] for i in range(13)]

    c = 7
    column = 37
    row = 13
    Ha_list = [0 for i in range(row)]
    Hb_list = [0 for i in range(column)]
    Ha = 0
    Hab = 0
    Ha_b = 0

    for i in range(1, c):
        for j in range(1, c):
            table[i + j][i * j] += 1

    for i in range(1, row):
        for j in range(1, column):
            table_H[i][j] = table[i][j] / 36
            if table_H[i][j] != 0:
                table_H[i][j] *= -log2(table_H[i][j])
                Hab += table_H[i][j]

        s_a = sum(table[i])/36
        if s_a != 0:
            Ha_list[i] = -s_a * log2(s_a)

    for i in range(column):
        s_b = sum([table[k][i] for k in range(row)]) / 36
        if s_b != 0:
            Hb_list[i] = -s_b * log2(s_b)

    Hb = sum(Hb_list)
    Ha = sum(Ha_list)

    for i in range(2, row):
        s = sum(table[i])
        for j in range(1, column):
            table[i][j] /= s

    Ha_b = Hab - Ha
    print(f"H(A) = {Ha}")
    print(f"H(AB) = {Hab}")
    print(f"Ha(B) = {Ha_b}")
    print(f"H(B) = {Hb}")
    print(f"I(A,B) = {Hb - Ha_b}")


if __name__ == "__main__":
    task()