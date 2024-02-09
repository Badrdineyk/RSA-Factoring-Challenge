#!/usr/bin/python3
import sys


def fact(num):
    i = 2

    if num < 2:
        return

    while num % i:
        i += 1
    print("{:.0f}={:.0f}*{:.0f}".format(num, num / i, i))


def main(file_path):
    with open(file_path) as file:
        line = file.readline()
        while line != "":
            number = int(line.split('\n')[0])
            fact(number)
            line = file.readline()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
