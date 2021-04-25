package com.algs.sort;

import com.algs.std.StdOut;

public abstract class SortExample {

    public abstract  void sort(Comparable [] a);

    static boolean less(Comparable v, Comparable w){
        return v.compareTo(w) < 0;
    }

    void exch(Comparable [] a, int i, int j){
        Comparable t = a[i];
        a[i] = a[j];
        a[j] = t;

    }

    void show(Comparable [] a){
        for(int i=0; i< a.length; i++){
            StdOut.print(a[i] + " ");
        }
        StdOut.println();
    }

    boolean isSorted(Comparable [] a){

        if (a== null || a.length <= 1){
            return true;
        }

        for(int i=1; i< a.length; i++){
            if(less(a[i], a[i-1])){
                return false;
            }
        }
        return true;
    }



}
