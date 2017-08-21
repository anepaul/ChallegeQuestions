# source https://www.hackerrank.com/challenges/ctci-array-left-rotation
# A left rotation operation on an array of size 'n' shifts each of the array's 
# elements 1 unit to the left. For example, if 2 left rotations are performed 
# on array [1,2,3,4,5], then the array would become [].
def array_left_rotation(a, n, k):
    result = [0] * n
    for i in range(len(a)):
        result[(i - k) % n] = a[i]
    return result

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
