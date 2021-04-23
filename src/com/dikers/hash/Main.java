package com.dikers.hash;

public class Main {

    public static void main(String[] args) {

        int a = 42;
        int b = -42;
        String d = "hello" ;
        System.out.println(((Integer) a).hashCode());
        System.out.println(((Integer) b).hashCode());
        System.out.println(d.hashCode());
    }
}
