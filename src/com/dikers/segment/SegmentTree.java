package com.dikers.segment;

import java.util.Objects;

public class SegmentTree<E> {
    private E[] data;
    private E[] tree;  // 满二叉树
    private Merger<E> merger;
    public SegmentTree(E[] arr, Merger<E> merger){
        data = (E[]) new Object[arr.length];
        this.merger = merger;
        for(int i=0; i< arr.length; i++){
            data[i] = arr[i];
        }

        tree = (E[]) new Object[4 * arr.length];
        buildSegmentTree(0, 0, data.length-1);
    }

    //[l...r] 的线段树
    private void buildSegmentTree(int treeIndex, int l , int r){
        if(l == r){
            tree[treeIndex] = data[l];
            return;
        }

        int leftTreeIndex = leftChild(treeIndex);
        int rightTreeIndex = rightChild(treeIndex);

        int mid = l + (r - l )/2;
        buildSegmentTree(leftTreeIndex, l, mid);
        buildSegmentTree(rightTreeIndex, mid+ 1, r);

        tree[treeIndex] = merger.merge(tree[leftTreeIndex] ,tree[rightTreeIndex]);

    }


    public E get(int index){
        if(index< 0 || index >= data.length) {
            throw new IllegalArgumentException("index is illegal.");
        }

        return data[index];
    }

    private int leftChild(int index){
        return 2* index + 1;
    }

    private int rightChild(int index){

        return 2*index + 2;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append('[');
        for (int i=0; i< tree.length; i++){
            if (tree[i] != null){
                res.append(tree[i]);
            }else{
                res.append("null");
            }
            if(i!=tree.length - 1){
                res.append(", ");
            }
        }
        res.append("]");
        return res.toString();
    }

    public E query(int queryL, int queryR){

        if (queryL < 0 || queryL >= data.length ||
               queryR < 0 || queryR >= data.length ||
                queryL > queryR){
            throw new IllegalArgumentException("index is illegal.");
        }

        return query(0, 0, data.length-1, queryL, queryR);
    }





    private E query(int treeIndex, int l , int r, int queryL, int queryR){

        if (l == queryL && r == queryR){
            return tree[treeIndex];
        }

        int mid = l + (r-l)/2;
        int leftTreeIndex = leftChild(treeIndex);
        int rightTreeIndex = rightChild(treeIndex);

        if(queryL>= mid + 1){
            return query(rightTreeIndex, mid + 1, r, queryL, queryR);
        }else if(queryR <= mid){
            return query(leftTreeIndex, l, mid, queryL, queryR);
        }

        E leftResult = query(leftTreeIndex, l, mid, queryL, mid);
        E rightResult = query(rightTreeIndex, mid+1, r, mid+1, queryR);

        return this.merger.merge(leftResult, rightResult);
    }


    public static void main(String[] args) {
        Integer[] nums = {-2, 0, 3, -5, 2, -1};
        SegmentTree<Integer> segmentTree = new SegmentTree<>(nums, new Merger<Integer>() {
            @Override
            public Integer merge(Integer a, Integer b) {
                return a + b;
            }
        });

        System.out.println(segmentTree);

        int r = segmentTree.query(0, 2);
        System.out.println(r);
    }
}
