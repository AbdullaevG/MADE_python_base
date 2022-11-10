#!/bin/env/python

l1 = [1, 2, 3, 4]
l2 = [2, 4, 6]

# out: [2, 4]


def merge(lst1, lst2):
    i, j = 0, 0
    res = []    
    while i < len(lst1) and  j < len(lst2):
        if lst1[i] == lst2[j]:
            if not res or res[-1]!=lst1[i]:
                res.append(lst1[i])
            i += 1
            j += 1
            continue 
        elif lst1[i] < lst2[j]:
            i += 1

        else:
            j += 1
    
    print(res)
    return res


def merge_k(lists, k):
    res = []
    return res


def main():
    pass


if __name__ == "__main__":
    main()
