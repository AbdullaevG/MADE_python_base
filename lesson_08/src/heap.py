#!/usr/bin/env python
import heapq

def heapsort(lst: list):
    heapq.heapify(lst)
    res = []
    while lst:
        top= heapq.heappop(lst)
        res.append(top)
    return res

def main():
    pass

if __name__ == "__main__":
    main()
