#!/usr/bin/python3
"""A module to calculate the fewest number of operations needed to result in
exactly n H characters in the file
"""


def minOperations(n):
    """Computes minimum operations needed to result in n H characters"""
    if not isinstance(n, int):
        return 0
    clipboard = 0
    count = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            count += 2
        elif clipboard > 0:
            done += clipboard
            count += 1
    return count
