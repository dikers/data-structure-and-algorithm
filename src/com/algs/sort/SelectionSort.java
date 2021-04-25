package com.algs.sort;

import com.algs.std.StdOut;

public class SelectionSort extends SortExample {
    @Override
    public void sort(Comparable[] a) {
        int N = a.length;
        for(int i=0; i< N; i++){
            int min = i;
            for(int j=i+1; j< N; j++){
                if(less(a[j], a[min])){
                    min = j;
                }
            }
            exch(a, i, min);
        }
    }

    public static void main(String[] args) {
        Integer a[] = {1,4,3,6,2,9,10};
        SelectionSort selectionSort = new SelectionSort();

        selectionSort.sort(a);
        selectionSort.show(a);
        StdOut.println("Sorted: "+selectionSort.isSorted(a));

    }
}
