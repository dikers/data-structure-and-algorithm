package com.dikers.chapter1;

public class LinearSearch {


    public int search(int[] data, int target){
        for (int i=0; i<data.length; i++){
            if(data[i] == target){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        LinearSearch linearSearch = new LinearSearch();
        int [] data = {2, 3, 5, 7, 32, 66};
        int target = 3;

        int result = linearSearch.search(data, target);
        System.out.println(result);

    }
}
