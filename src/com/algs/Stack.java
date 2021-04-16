package com.algs;


import java.util.Iterator;

public class Stack<Item> implements Iterable<Item>{
    private class Node{
        Item item;
        Node next;
    }

    private Node first;
    private int N;

    public boolean isEmpty(){
        return first == null;
    }

    public int size(){
        return N;
    }
    public void push(Item item){

        Node oldFirst = first;
        first = new Node();
        first.item = item;
        first.next = oldFirst;
        N++;
    }

    public Item pop(){
        if(isEmpty()){
            return null;
        }
        Item item = first.item;
        first = first.next;
        N --;
        return item;
    }


    @Override
    public Iterator<Item> iterator() {
        return null;
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(5);
        stack.push(3);
        System.out.println(stack.pop());
    }

}
