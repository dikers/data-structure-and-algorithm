package com.dikers.chapter9;

import com.dikers.utils.ArrayGenerator;
import com.dikers.utils.SortingHelper;

import java.util.Arrays;

public class HeapSort{
    private HeapSort(){}

    public static<E extends Comparable<E>> void sort(E[] data){

        MaxHeap<E> maxHeap = new MaxHeap<>();
        for(E e: data){
            maxHeap.add(e);
        }
        for(int i = data.length -1; i >= 0 ; i --){
            data[i] = maxHeap.extractMax();
        }
    }

    public static <E extends Comparable<E>> void sort2(E[] data){
        if(data.length <=1 )return;
        for(int i = (data.length-2) /2 ; i>=0; i-- ){
            siftDown(data, i, data.length);
        }

        for(int i= data.length -1; i>=0; i--){
            swap(data, 0, i);
            siftDown(data, 0, i);
        }

    }


    public static <E extends Comparable<E>> void siftDown(E[] data, int k , int n ){
        while(2*k + 1 < n){
            int j = 2*k + 1;
            //右孩子大
            if( j+1 < n && data[j+1].compareTo(data[j])>0){
                j ++;
            }
            //data[j是左右孩子里面最大值

            if(data[k].compareTo(data[j])>=0){
                break;
            }
            swap(data, k, j);

            k = j;
        }

    }

    private static<E extends Comparable<E>> void swap(E[] data, int k, int j){
        E temp = data[k];
        data[k] = data[j];
        data[j] = temp;
    }

    public static void main(String[] args) {
        int n = 10000;
        Integer [] arr = ArrayGenerator.generateRandomArray(n, n );

        Integer [] arr2 = Arrays.copyOf(arr, arr.length);
        Integer [] arr3 = Arrays.copyOf(arr, arr.length);
        Integer [] arr4 = Arrays.copyOf(arr, arr.length);

        SortingHelper.sortTest("MergeSort", arr);

        SortingHelper.sortTest("HeapSort2", arr);

    }
}
