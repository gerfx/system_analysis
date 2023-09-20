import csv
import json
from jsonpath_ng import jsonpath, parse


def csv_reader(row, column):
    filename = "example.csv"
    f = open(filename, 'r')
    csv_file = csv.reader(f)
    csv_table = [[item for item in line] for line in csv_file]
    return csv_table[row][column]


def json_reader(jpath):
    filename = 'example.json'
    f = open(filename, 'r')
    json_data = json.load(f)
    jsonpath_expression = parse(jpath)
    match = jsonpath_expression.find(json_data)
    return match[0].value


def main():
    #row, column = map(int, input().split())
    row, column = 1, 2
    print(csv_reader(row, column))
    #jpath = '$.str.str1'
    #print(json_reader(jpath))
    return


if __name__ == "__main__":
    main()

