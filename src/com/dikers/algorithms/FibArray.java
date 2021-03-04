package com.dikers.algorithms;

public class FibArray {

    int num = 0;
    int N = 40;
    int [] memo = new int[N];
    public int fib(int n){
        num ++;

        if (n ==0){
            return 0;
        }else if(n == 1){
            return 1;
        }
        if(memo[n] == -1 ){
            memo[n] = fib(n-1) + fib(n-2);
        }

        return memo[n];
    }

    public void dealWith(){
        long start = System.currentTimeMillis();
        for(int i=0; i<memo.length; i++){
            memo[i] = -1;
        }
        int result = fib(N-1);
        long end = System.currentTimeMillis();

        System.out.println(" Result: " + result +  " use time " + (end - start));

    }


    public static void main(String[] args) {
        FibArray fibArray = new FibArray();
        fibArray.dealWith();

    }
}
