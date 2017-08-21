// source https://www.hackerrank.com/challenges/ctci-array-left-rotation
// A left rotation operation on an array of size 'n' shifts each of the array's 
// elements 1 unit to the left. For example, if 2 left rotations are performed 
// on array [1,2,3,4,5], then the array would become [].

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }

        int result[] = rotateLeft(a, n, k);

        StringBuilder sb = new StringBuilder();
        for (int x : result) {
            sb.append(x + " ");
        }

        System.out.println(sb.toString());
    }

    private static int[] rotateLeft(int[] arr, int size, int nShifts) {
        int result[] = new int[size];
        for (int i = 0; i < size; i++) {
            result[(i - nShifts) % size] = arr[i];
        }
        return result;
    }
}
