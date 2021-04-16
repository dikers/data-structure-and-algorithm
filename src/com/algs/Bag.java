package com.algs;

import java.util.Iterator;

public class Bag<Item> implements Iterable<Item> {
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

    private Node first;
    private class Node{
        Item item;
        Node next;
    }

    public void add(Item item){
        Node oldFirst = first;
        first = new Node();
        first.item = item;
        first.next = oldFirst;

    }


    @Override
    public String toString() {

        StringBuilder stringBuilder = new StringBuilder();
        Node cur = first;
        while( cur != null){
            stringBuilder.append(cur.item +", ");
            cur = cur.next;
        }

        return "Bag{ " +
                stringBuilder.toString() +
                '}';
    }

    public static void main(String[] args) {
        System.out.println("hello");
        Bag<Integer> numbers = new Bag<>();
        numbers.add(1);
        numbers.add(2);
        System.out.println(numbers);

    }
}
