import json
import numpy as np


def task():
    f = open("Ранжировка  A.json")
    data = json.load(f)
    data_to_range_table(data)


def item_counter(data):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += len(item)
        else:
            count += 1
    return count


def data_to_range_table(data):
    range_dict = {}
    weight = 0
    for item in data:
        if isinstance(item, list):
            range_dict[tuple(item)] = weight
        else:
            range_dict[item] = weight
        weight += 1

    n = item_counter(data)
    range_table = np.zeros((n, n))

    curr = 0
    temps = [0 for i in range(n)]
    i = 0

    for key in range_dict.keys():
        val = range_dict[key]
        if isinstance(key, tuple):
            for k in range(len(key)):
                temps[val:] = [1 for i in range(val, n)]
                range_table[i] = temps
                i += 1
            temps = [0 for i in range(n)]
        else:
            row = [1 for i in range(val, n)]
            temps[val:] = row
            range_table[i] = temps
            i += 1
            temps = [0 for i in range(n)]

    print(range_table)







def main():
    task()


if __name__ == "__main__":
    main()
