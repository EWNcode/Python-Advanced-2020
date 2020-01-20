"""
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones.
On the first line you will be given an integer N. On the next N lines, you will receive one username per line. Print
the collection on the console (the order does not matter):

"""


def return_unique(names):
    s = set(names)
    s = sorted(s, key=names.index)
    return '\n'.join(s)


#tests = [
#        '6',
#        [
#            'George',
#            'George',
#            'George',
#            'Peter',
#            'George',
#            'NiceGuy1234',
#        ],
#]
#
#(n, names) = [n for n in tests]


n = int(input())
names = [input() for x in range(n)]

print(return_unique(names))