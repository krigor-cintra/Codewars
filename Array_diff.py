"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order."""

def array_diff(a, b):
    if (len(a) == 0):
        return a
    else:
        for x in range(len(b)):
            while b[x] in a:
                a.remove(b[x])
        return a
