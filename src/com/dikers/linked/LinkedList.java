package com.dikers.linked;

public class LinkedList<E> {
    private class Node{
        public Node next;
        public E e;

        public Node(E e, Node next){
            this.e = e;
            this.next = next;
        }
        public Node(E e){
            this(e, null);
        }

        public Node(){
            this(null, null);
        }


        @Override
        public String toString() {
            return "N{" +
                    "e=" + e +
                    '}';
        }
    }


    private int size;
    private Node dummyHead;

    public LinkedList(){
        dummyHead = new Node(null, null);
        size = 0;
    }
    public int getSize(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void addFirst(E e){
//        Node node = new Node(e);
//        node.next = head;
//        head = node;
        add(0,e);

    }
    // 在链表的index(0-based)位置添加新的元素e
    // 在链表中不是一个常用的操作，练习用：）
//    public void add(int index, E e){
//
//        if(index < 0 || index > size)
//            throw new IllegalArgumentException("Add failed. Illegal index.");
//
//        Node prev = dummyHead;
//        for(int i = 0 ; i < index ; i ++)
//            prev = prev.next;
//
//        prev.next = new Node(e, prev.next);
//        size ++;
//    }

    public void add(int index, E e){
        if(index< 0 || index > size){
            throw new IllegalArgumentException("Add failed. Illegal index.");
        }
        Node prev = dummyHead;
        for (int i=0; i< index ; i++){
            prev = prev.next;
        }

        prev.next = new Node(e, prev.next);
        size ++;

    }

    public E remove(int index){
        if(index< 0 || index >= size){
            System.out.println(" index: " + index);
            throw new IllegalArgumentException("remove failed. Illegal index.");
        }
        Node prev = dummyHead;
        for (int i=0; i< index ; i++){
            prev = prev.next;
        }
        Node delNode = prev.next;
        prev.next = delNode.next;
        E e = delNode.e;
        delNode = null;
        size --;
        return e;
    }
//
//    public E remove(int index){
//        if(index < 0 || index >= size)
//            throw new IllegalArgumentException("Remove failed. Index is illegal.");
//
//        Node prev = dummyHead;
//        for(int i = 0 ; i < index ; i ++)
//            prev = prev.next;
//
//        Node retNode = prev.next;
//        prev.next = retNode.next;
//        retNode.next = null;
//        size --;
//
//        return retNode.e;
//    }

    public E removeFirst(){
        return remove(0);
    }

    public E removeLast(){
        return remove(size-1);
    }




    public void addLast(E e){
        add(size, e);
    }

    public E get(int index){
        if(index< 0 || index >= size){
            throw new IllegalArgumentException("Add failed. Illegal index.");
        }
        Node cur = dummyHead.next;
        for (int i=0; i< index ; i++){
            cur = cur.next;
        }
        return cur.e;
    }


    public void set(int index, E e){
        if(index< 0 || index >= size){
            throw new IllegalArgumentException("Add failed. Illegal index.");
        }
        Node cur = dummyHead.next;
        for (int i=0; i< index ; i++){
            cur = cur.next;
        }
        cur.e = e;
    }

    public boolean contains(E e){

        Node cur = dummyHead.next;
        while(cur != null){
            if(cur.e == e){
                return true;
            }
            cur = cur.next;
        }
        return false;
    }

    @Override
    public String toString() {

        StringBuilder res = new StringBuilder();
        Node cur = dummyHead.next;
        while(cur != null){
            res.append(cur + "->");
            cur = cur.next;
        }
        res.append("NULL");
        return res.toString();
    }

    public static void main(String[] args) {

        LinkedList<Integer> linkedList = new LinkedList<>();
        for(int i = 0 ; i < 5 ; i ++){
            linkedList.addFirst(i);
            System.out.println(linkedList);
        }

        linkedList.add(2, 666);
        System.out.println(linkedList);

        linkedList.remove(2);
        System.out.println(linkedList);

        linkedList.removeFirst();
        System.out.println(linkedList);

        linkedList.removeLast();
        System.out.println(linkedList);
    }

}
