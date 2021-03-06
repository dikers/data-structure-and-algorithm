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
        return new ListIterator();
    }
    private class ListIterator implements Iterator<Item>{
        private Node current = first;
        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public Item next() {
            Item item = current.item;
            current = current.next;
            return item;
        }

        @Override
        public void remove() {

        }
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(5);
        stack.push(3);
        System.out.println(stack.pop());
    }

}
