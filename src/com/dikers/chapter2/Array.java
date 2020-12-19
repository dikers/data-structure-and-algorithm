package com.dikers.chapter2;


public class Array<E> {

    private E[] data;
    private int size;

    /**
     *
     * @param capacity
     */
    public Array(int capacity){
        data =(E[]) new Object[capacity];
        size = 0;
    }
    public Array(){
        this(10);
    }
    public int getSize(){
        return size;
    }

    public int getCapacity(){
        return data.length;
    }

    public boolean isEmpty(){
        return size ==0;
    }

    public void addLast(E e)  {
        add(size, e);
    }
    public void addFirst(E e) {
        add(0, e);
    }

    public void add(int index, E e)  {
        if(size == data.length){
            throw new IllegalArgumentException("Add failed. Array is full.");
        }
        if (index < 0 || index > size){
            throw new IllegalArgumentException("Add failed, Require index < 0 || index > size");
        }
        for(int i = size-1; i >= index; i--){
            data[i+1]= data[i];
        }
        data[index] = e;
        size += 1;
    }

    public E get(int index){
        if(index<0 || index>=size){
            throw new IllegalArgumentException("Get failed. Index is illegal.");
        }
        return data[index];
    }

    public void set(int index, E e){
        if(index<0 || index>=size){
            throw new IllegalArgumentException("Set failed. Index is illegal.");
        }
        data[index] = e;
    }

    public boolean contains(E e){
        for (int i=0; i<size; i++){
            if(data[i].equals(e)){
                return true;
            }
        }
        return false;
    }

    /**
     * 查找元素e， 如果没有找到返回-1， 如果找到返回索引
     * @param e
     * @return
     */
    public int find(E e){
        for (int i=0; i<size; i++){
            if(data[i].equals(e)){
                return i;
            }
        }
        return -1;
    }

    public E remove(int index){
        if(index<0 || index>=size){
            throw new IllegalArgumentException("Set failed. Index is illegal.");
        }

        E ret = data[index];

        for(int i= index+1; i<size; i++){
            data[i-1] = data[i];
        }
        size--;
        data[size] = null;
        return ret;
    }

    public E removeFirst(){
        return remove(0);
    }

    public int removeLast(){
        return (size -1) ;
    }

    public boolean removeElement(E e){
        int index = find(e);
        if(index != -1){
            remove(index);
            return true;
        }
        return false;
    }

    public void swap(int i, int j){

        if(i<0 || i>=size || j< 0 || j>=size){
            throw new IllegalArgumentException("Index is illegal.");
        }

        E t = data[i];
        data[i] = data[j];
        data[j] = t;
    }

    @Override
    public String toString() {

        StringBuilder res = new StringBuilder();
        res.append(String.format("Array: size=%d, capacity=%d \n", size, data.length));

        res.append('[');
        for(int i=0; i<size; i++){
            res.append(data[i]);
            if(i != size -1)
                res.append(", ");
        }
        res.append(']');

        return res.toString();
    }

}
