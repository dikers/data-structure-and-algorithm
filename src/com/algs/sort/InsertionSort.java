package com.algs.sort;

import com.algs.std.StdOut;

public class InsertionSort extends SortExample {
    @Override
    public void sort(Comparable[] a) {
        int N = a.length;
        for(int i=0; i< N; i++){
         for(int j=i; j>0 && less(a[j], a[j-1]); j--){
             exch(a, j, j-1);
         }
        }
    }

    public static void main(String[] args) {
        Integer a[] = {1,4,3,6,2,9,10};
        InsertionSort insertionSort = new InsertionSort();

        insertionSort.sort(a);
        insertionSort.show(a);
        StdOut.println("Sorted: "+insertionSort.isSorted(a));

    }
}
