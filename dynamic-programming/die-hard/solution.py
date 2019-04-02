#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_time(h, a, s=0, c={}):
    if s == 0:
        h += 3
        a += 2
    elif s == 1:
        h -= 5
        a -= 10
    else:
        h -= 20
        a += 5

    if h <= 0 or a <= 0:
        return 0

    k = (h, a, s)
    if k in c:
        return c[k]

    c[k] = 1 + max(max_time(h, a, (s + 1) % 3), max_time(h, a, (s - 1) % 3))
    return c[k]


if __name__ == '__main__':
    t = int(input())

    c = {}
    for i in range(t):
        h, a = map(int, input().strip().split())
        print(max_time(h, a, 0, c))
