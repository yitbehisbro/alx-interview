#!/usr/bin/python3
"""Pascal Triangle """
def pascal_triangle(n):
    """ Returns the pascal triangle for n values """
    if n <= 0:
        return []
    res = [[1]]
    for i in range(1, n):
        r = [1]
        for j in range(1, i):
            r.append(res[i-1][j-1] + res[i-1][j])
        r.append(1)
        res.append(r)
    return res
