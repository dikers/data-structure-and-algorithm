package com.dikers.chapter1;

public class LinearSearch {

    private LinearSearch(){}
    public static <E> int search(E[] data, E target){
        for (int i=0; i<data.length; i++){
            if(data[i].equals(target)){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        LinearSearch linearSearch = new LinearSearch();
        Integer [] data = {2, 3, 5, 7, 32, 66};
        Integer target = 3;

        int result = linearSearch.search(data, target);
        System.out.println(result);



        Student[] students = {
                new Student("Alice"),
                new Student("Dikers"),
                new Student("Bobo"),
                new Student("Charles")
        };

        Student bobo = new Student("Bobo");

        int res3 = LinearSearch.search(students, bobo);

        System.out.println(res3);

    }
}
