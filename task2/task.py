import csv
import sys


def task(path):
    with open(path, newline="") as csvfile:
        filedata = list(csv.reader(csvfile, delimiter=","))


    def has_grand_relative(tree):
        r4, r5, r3 = set(), set(), set()
        for node in tree:
            for child in tree[node]:
                if len(tree[node]) > 1:
                    r3.add(tuple(tree[node]))
                    a3[child] = len(tree[node]) - 1
                if child in tree:
                    if node not in a4:
                        a4[node] = 0
                    if child not in a5:
                        a5[child] = 0
                    a4[node] += 1
                    for a in tree[child]:
                        if a not in a5:
                            a5[a] = 0
                        a5[a] += 1
                    r4.add(child)
                    r5.add(node)

        return r4, r5, r3

    edges = filedata
    tree = {}
    r1, r2 = set(), set()
    a1, a2, a3, a4, a5 = dict(), dict(), dict(), dict(), dict()

    for parent, child in edges:
        if parent not in a1:
            a1[parent] = 0
        if child not in a2:
            a2[child] = 0
        a1[parent] += 1
        a2[child] += 1
        r1.add(parent)
        r2.add(child)

        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)

    r3, r4, r5 = has_grand_relative(tree)

    node_list = sorted(list(set(item for edge in edges for item in edge)))
    print("Node\t a1\t a2\t a3\t a4\t a5")
    for node in node_list:
        print(
            f"{node}\t {a1.get(node, 0)}\t {a2.get(node, 0)}\t {a3.get(node, 0)}\t {a4.get(node, 0)}\t {a5.get(node, 0)}")


if __name__ == "__main__":
    task(sys.argv[1])
