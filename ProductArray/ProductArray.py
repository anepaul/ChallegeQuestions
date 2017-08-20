# source https://www.interviewcake.com/question/java/product-of-other-numbers
# Write a function getProductsOfAllIntsExceptAtIndex() that takes an array of integers and returns an array of the products.
# Do not use division in your solution.

def my_function(arr):
    forward_arr = [0] * len(arr)
    backward_arr = [0] * len(arr)
    result_arr = []
    # calculate product of increasing array
    for ind in range(len(arr)):
        if ind is 0:
            forward_arr[0] = 1
        else:
            forward_arr[ind] = arr[ind-1] * forward_arr[ind-1]

    print(forward_arr)

    # calculate product of decreasing array
    for ind in range(len(arr)-1, -1, -1):
        if ind is len(arr)-1:
            backward_arr[len(arr)-1] = 1
        else:
            backward_arr[ind] = arr[ind+1] * backward_arr[ind+1]

    print(backward_arr)

    for ind in range(len(arr)):
        result_arr.append(forward_arr[ind] * backward_arr[ind])
    return result_arr

print(my_function([1, 7, 3, 4]))
