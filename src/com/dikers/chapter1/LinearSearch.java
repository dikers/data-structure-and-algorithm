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
                new Student("Alice", 100),
                new Student("Dikers", 20),
                new Student("Bobo", 30),
                new Student("Charles", 40)
        };

        Student bobo = new Student("Bobo", 60);

        int res3 = LinearSearch.search(students, bobo);

        System.out.println(res3);

    }
}
