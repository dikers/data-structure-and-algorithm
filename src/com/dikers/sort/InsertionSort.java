package com.dikers.sort;

import com.dikers.utils.ArrayGenerator;
import com.dikers.utils.SortingHelper;

public class InsertionSort {

    private InsertionSort(){}

    private static  <E extends Comparable<E>>  void swap(E [] arr, int i, int j){
        E temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static <E extends Comparable<E>>  void sort2(E[] arr){

        for (int i=0; i< arr.length; i++){
            for(int j=i; j-1 >= 0; j--){
                if(arr[j].compareTo(arr[j-1])< 0){
                    swap(arr, j, j-1);
//                    printArr(arr);
                }else {
                    break;
                }
//                printArr(arr);
            }
        }
    }

    public static <E extends Comparable<E>>  void sort(E[] arr){

        for (int i=0; i< arr.length; i++){
            E t = arr[i];
            int j;

            for(j =i; j-1 >=0 && t.compareTo(arr[j-1]) < 0; j--){
                arr[j] = arr[j-1];
            }
            arr[j] = t;
        }
    }

    private  static <E extends  Comparable<E>> void printArr(E[] arr){

        for(int i=0; i< arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println(" ");
    }

    public static void main(String[] args) {

        Integer [] arr = {9, 5, 2, 7, 1};
        sort(arr);
        for(int i = 0; i< arr.length; i++){
            System.out.print(arr[i] +" ");
        }

        Student[] students = {
                new Student("Alice", 24),
                new Student("Dikers", 23),
                new Student("Bobo", 56),
                new Student("Charles", 34)
        };


        sort(students);
        System.out.println("");
        for(Student student: students){
            System.out.println(student);
        }


        int [] dataSize = {10000, 100000};

        for (int n: dataSize){
            Integer[] arr1 = ArrayGenerator.generateRandomArray(n, n);
            SortingHelper.sortTest("InsertionSort", arr1);
        }

    }
}
