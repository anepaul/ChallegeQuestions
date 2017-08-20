# source https://www.interviewcake.com/question/java/product-of-other-numbers
# Write a function getProductsOfAllIntsExceptAtIndex() that takes an array of integers and returns an array of the products.
# Do not use division in your solution.

def my_function(arr):
    result_arr = [0] * len(arr)
    # calculate product of increasing array
    for ind in range(len(arr)):
        if ind is 0:
            result_arr[0] = 1
        else:
            result_arr[ind] = arr[ind-1] * result_arr[ind-1]


    # calculate product of decreasing array
    for ind in range(len(arr)-1, -1, -1):
        
        if ind is len(arr)-1:
            backward_rolling_product = 1
        else:
            backward_rolling_product = arr[ind+1] * backward_rolling_product
            result_arr[ind] = result_arr[ind] * backward_rolling_product

    return result_arr

print(my_function([1, 7, 3, 4]))
print(my_function([0, 0, 0, 0]))
