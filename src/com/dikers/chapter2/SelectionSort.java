package com.dikers.chapter2;

import com.dikers.utils.ArrayGenerator;
import com.dikers.utils.SortingHelper;

public class SelectionSort {

    private SelectionSort(){}

    private static  <E extends Comparable<E>>  void swap(E [] arr, int i, int j){
        E temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static <E extends Comparable<E>>  void sort(E[] arr){

        for (int i=0; i< arr.length; i++){
            int minIndex = i;
            for (int j=i; j<arr.length; j++){
                if (arr[j].compareTo(arr[minIndex]) < 0){
                    minIndex = j;
                }
            }
            swap(arr, i, minIndex);
        }
    }

    public static void main(String[] args) {

//        Integer [] arr = {3, 5, 6, 7, 8};
//        sort(arr);
//        for(int i = 0; i< arr.length; i++){
//            System.out.print(arr[i] +" ");
//        }
//
//        Student[] students = {
//                new Student("Alice", 24),
//                new Student("Dikers", 23),
//                new Student("Bobo", 56),
//                new Student("Charles", 34)
//        };
//
//
//        sort(students);
//        System.out.println("");
//        for(Student student: students){
//            System.out.println(student);
//        }
//

        int [] dataSize = {10000, 100000};

        for (int n: dataSize){
            Integer[] arr1 = ArrayGenerator.generateRandomArray(n, n);
            SortingHelper.sortTest("SelectionSort", arr1);
        }

    }
}
