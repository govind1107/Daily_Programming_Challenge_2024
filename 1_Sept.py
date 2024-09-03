"""Kth largest element of list"""


def kth_largst(arr,k):

    for i in range(k):
        print(max(arr))
    # K_largest = arr[:k]

    # for nums in arr[k:]:
    #     min_index = K_largest.index(min(K_largest))

    #     if nums>K_largest[min_index]:
    #         K_largest[min_index] = nums

    # return min(K_largest)


arr = [3,2,1,5,6,4]

k = 2

print(kth_largst(arr,k))
