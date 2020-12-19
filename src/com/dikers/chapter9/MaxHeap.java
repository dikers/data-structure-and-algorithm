package com.dikers.chapter9;

import com.dikers.chapter2.Array;

public class MaxHeap<E extends Comparable<E>> {
    private Array<E> data;

    public MaxHeap(int capacity){

        data = new Array<>(capacity);

    }

    public MaxHeap(){
        data = new Array<>();
    }

    public int size(){
        return data.getSize();
    }

    public boolean isEmpty(){
        return data.isEmpty();
    }

    private int parent(int index){
        if(index == 0){
            throw new IllegalArgumentException("index-0 doesn't have parent. ");
        }
        return (index - 1)/2;
    }

    private int leftChild(int index){
        return index *2 + 1;
    }

    private int rightChild(int index){
        return index * 2 + 2;
    }

    public void add(E e){

        data.addLast(e);
        siftUp(data.getSize() -1);
    }

    private void siftUp(int k){
        while(k>0 && data.get(parent(k)).compareTo(data.get(k))< 0){
            data.swap(k, parent(k));
            k = parent(k);
        }

    }
}
