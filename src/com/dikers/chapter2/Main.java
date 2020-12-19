package com.dikers.chapter2;

public class Main {

    public static void main(String[] args) throws IllegalAccessException {
        Array<Integer> arr = new Array(20);
        for(int i=0; i<10; i++)
            arr.addLast(i);
        System.out.println(arr);
        arr.add(1, 100);
        System.out.println(arr );

        arr.remove(2);
        System.out.println(arr);
    }
}
