# source https://www.interviewcake.com/question/python/highest-product-of-3
# Given a list of integers, find the highest product you can get from three of the integers.

def get_highest_product_of_three(list_of_ints):
    largest = list_of_ints[0]
    sec_largest = 0
    thrd_largest = 0
    largest_neg = 0
    sec_largest_neg = 0

    for i in list_of_ints:
        if i > largest:
            old = largest
            largest = i
            i = old

        if i > sec_largest:
            old = sec_largest
            sec_largest = i
            i = old

        if i > thrd_largest:
            old = thrd_largest
            thrd_largest = i
            i = old

        if i < largest_neg:
            old = largest_neg
            largest_neg = i
            i = old

        if i < sec_largest_neg:
            sec_largest_neg = i


    return max(largest * sec_largest * thrd_largest, largest * largest_neg * sec_largest_neg)

print(get_highest_product_of_three([-10, -10, 1, 3, 2]))
