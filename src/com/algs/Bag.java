package com.algs;

import com.algs.std.StdIn;
import com.algs.std.StdOut;

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
    private int N = 0;
    private class Node{
        Item item;
        Node next;
    }

    public void add(Item item){
        Node oldFirst = first;
        first = new Node();
        first.item = item;
        first.next = oldFirst;
        N ++;

    }

    public int size(){
        return N;
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

        Bag<Double> numbers = new Bag<Double>();

        while (!StdIn.isEmpty()){
            numbers.add(StdIn.readDouble());
        }

        int N = numbers.size();
        double sum  = 0.0;

        for(double x: numbers){
            sum += x;
        }

        double mean = sum/N;

        sum = 0.0;

        for(double x: numbers){
            sum += (x-mean) * (x-mean);
        }
        double std = Math.sqrt(sum/(N-1));

        StdOut.printf("Mean: %.2f\n", mean);
        StdOut.printf("Std dev: %.2f\n", std);

    }
}
