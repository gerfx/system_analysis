import json
import numpy as np


def task(f):
    data = []
    for i in range(len(f)):
        data.append(json.load(f[i]))
    table = [[] for i in range(len(f))]
    for i in range(len(data)):
        cnt = 1
        for j in range(len(data[i])):
            if isinstance(data[i][j], list):
                for el in data[i][j]:
                    table[i].append(cnt)
            else:
                table[i].append(cnt)
            cnt += 1

    table = np.array(table)
    sum_row = table.sum(axis=0)
    s = sum_row.sum()
    sq_dif = []
    for item in sum_row:
        sq_dif.append((s-item) ** 2)
    disp = sum(sq_dif)/(len(table) - 1)
    return disp


def main():
    f1 = [open("Ранжировка  A.json"), open("Ранжировка  B.json")]
    d1 = task(f1)
    f2 = [open("Ранжировка  A.json"), open("Ранжировка  C.json")]
    d2 = task(f2)
    print(d1 / max(d1, d2))
    print(d2 / max(d1, d2))


if __name__ == "__main__":
    main()
