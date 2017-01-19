import sys
import random


def prettyPrint(A):
    len_x = 2 * A - 1
    x = [[0] * len_x for _ in range(len_x)]

    for i in range(0, len_x):
        for j in range(0, len_x):
            top = j
            bot = (len_x - 1) - j
            left = i
            right = (len_x - 1) - i

            sub = min([top, bot, left, right])

            x[i][j] = A - sub
    return x


def kthsmallest(A, k):
    rand = random.randint(0, len(A) - 1)
    less = []
    greater = []
    equal = []
    pivot = A[rand]

    for i in A:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        elif i == pivot:
            equal.append(i)

    if len(less) >= k:
        return kthsmallest(less, k)
    elif len(less) + len(equal) >= k:
        return equal[0]
    else:
        adjusted_k = k - (len(less) + len(equal))
        return kthsmallest(greater, adjusted_k)


def nextGreater(A):
    result = []

    for i in range(0, len(A)):
        if i + 1 <= len(A) - 1:
            for j in range(i + 1, len(A)):
                if A[j] > A[i]:
                    result.append(A[j])
                    break
                elif j == len(A) - 1:
                    result.append(-1)
        else:
            result.append(-1)
    return result


def longestConsecutive(A):
    pairs = dict.fromkeys(A)
    cur_len = 0
    max_len = 0

    for i in A:
        if i - 1 in pairs:
            pairs[i - 1] = i

    for key, val in pairs.items():
        if key in pairs and key - 1 not in pairs:
            cur_len = 1
            while val in pairs:
                cur_len += 1
                val = pairs[val]
            if max_len < cur_len:
                max_len = cur_len
    return max_len

# Main function
def main():
    A = [-3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 9]
    k = 2

    #prettyPrint(A)
    #ksmallest(A, k)
    #nextGreater(A)
    #longestConsecutive(A)

if __name__ == '__main__':
    main()