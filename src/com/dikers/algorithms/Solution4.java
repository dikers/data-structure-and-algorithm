package com.dikers.algorithms;

import java.util.Arrays;

public class Solution4 {
    private int[] memo;

    public int climbStairs(int n) {
        memo = new int[n+1];
        Arrays.fill(memo, -1);
        return calcWays(n);
    }

    private int calcWays(int n){

        if (n == 0){
            return 1;
        }
        if (n == 1){
            return 1;
        }
        if (n == 2){
            return 2;
        }

        if(memo[n] == -1){
            memo[n] = calcWays(n-1) + calcWays( n-2);
        }

        return memo[n];
    }



    public static void main(String[] args) {

        System.out.println((new Solution4()).climbStairs(10));
    }
}
