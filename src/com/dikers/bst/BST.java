package com.dikers.bst;

import com.dikers.chapter2.Array;

import java.util.*;

/**
 * 二分搜索树
 * @param <E>
 */
public class BST<E extends Comparable<E>> {

    private class Node{
        public E e;
        public Node left, right;

        public Node(E e) {

            this.e = e;
            left = null;
            right = null;
        }

        @Override
        public String toString() {
            return e.toString();
        }
    }

    private Node root;
    private int size;

    public BST(){
        root = null;
        size = 0;
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){

        return size == 0;
    }

    /**
     * 添加元素
     * @param e
     */
    public void add(E e){
        root = add(root, e);

    }

    /**
     * 内部添加
     * @param node
     * @param e
     */


    private Node add(Node node, E e){
        //递归终止条件

        if(node == null){
            size ++;
            return new Node(e);
        }
        if(e.compareTo(node.e)< 0){
            node.left = add(node.left, e);
        }else if(e.compareTo(node.e) > 0){
            node.right = add(node.right, e);
        }else {
            System.out.println("已经包含了该元素");
        }
        return node;
    }

    /**
     * 是否包含元素
     * @param e
     * @return
     */
    public boolean contains(E e){
        return contains(root, e);
    }

    private boolean contains(Node node, E e){

        if (node == null){
            return false;
        }

        if(e.compareTo(node.e) == 0){
            return true;
        }else if(e.compareTo(node.e) < 0){
            return contains(node.left, e);
        }else{
            return contains(node.right, e);
        }
    }

    public void preOrder(){
        System.out.println("前序遍历");
        preOrder(root);

    }

    private void preOrder(Node node){
        if (node == null){
            return;
        }

        System.out.print(node.e +" -> ");

        preOrder(node.left);
        preOrder(node.right);
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();

        generateBSTString(root, 0, res);

        return res.toString();
    }

    private void generateBSTString(Node node, int depth, StringBuilder res) {

        if(node == null){
            res.append(generateDepthString(depth) + "null\n");
            return;
        }

        res.append(generateDepthString(depth) + node.e + "\n");

        generateBSTString(node.left, depth+1, res);
        generateBSTString(node.right, depth+1, res);


    }

    private String generateDepthString(int depth) {
        StringBuilder res = new StringBuilder();
        for(int i =0; i< depth; i++){
            res.append("--");
        }
        return res.toString();
    }

    public void  levelOrder(){
        System.out.println("层序遍历");
        if (root == null){
            return ;
        }
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);

        while (!queue.isEmpty()){

            Node temp = queue.remove();
            System.out.println("\t"+ temp.e);
            if(temp.left != null){
                queue.add(temp.left);
            }
            if(temp.right != null){
                queue.add(temp.right);
            }
        }//end while
    }



    /**
     * 中序遍历
     */
    public void inOrder(){
        System.out.println("中序遍历");
        inOrder(root);
    }
    private void inOrder(Node node){

        if (node == null){
            return ;
        }
        inOrder(node.left);
        System.out.println(node.e);
        inOrder(node.right);
    }

    /**
     * 后序遍历
     * @param
     */
    public void postOrder(){
        System.out.println("后序遍历");
        postOrder(root);
    }
    private void postOrder(Node node){

        if(node == null){
            return ;
        }

        postOrder(node.left);
        postOrder(node.right);
        System.out.println(node.e);

    }
    public void preOrderNR(){
        System.out.println("非递归前序遍历");
        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while(!stack.isEmpty()){
            Node cur = stack.pop();
            System.out.println(cur.e);

            if (cur.right != null) {
                stack.push(cur.right);
            }
            if (cur.left != null){
                stack.push(cur.left);
            }
        }

    }

    public E minimum(){
        if(size ==0){
            throw new IllegalArgumentException("BST is empyt!");
        }
        return minimum(root).e;
    }

    private Node minimum(Node node){
        if (node.left == null){
            return node;
        }
        return minimum(node.left);
    }

    public E maximum(){
        if(size ==0){
            throw new IllegalArgumentException("BST is empyt!");
        }
        return maximum(root).e;
    }

    private Node maximum(Node node){
        if (node.right == null){
            return node;
        }
        return maximum(node.right);
    }


    public E removeMin(){
        E ret = minimum();
        root = removeMin(root);
        return ret;
    }
    private Node removeMin(Node node){
        if(node.left == null){
            Node rightNode = node.right;
            node.right = null;
            size --;
            return rightNode;
        }
        node.left = removeMin(node.left);
        return node;
    }


    public E removeMax(){
        E ret = maximum();
        root = removeMax(root);
        return ret;
    }

    private Node removeMax(Node node){
        if(node.right == null){
            Node leftNode = node.left;
            node.left = null;
            size --;
            return leftNode;
        }
        node.right = removeMin(node.right);
        return node;
    }

    public Node delete(E e){
        return delete(root, e);
    }

    private Node delete(Node node, E e){
        if(node == null){
            return null;
        }
        if(e.compareTo(node.e) == 0){

            if(node.left == null){
                Node rightNode = node.right;
                node.right = null;
                size --;
                return rightNode;
            }
            if(node.right == null){
                Node leftNode = node.left;
                node.left = null;
                size --;
                return leftNode;
            }

            Node miniNode = minimum(node.right);
            node.e = miniNode.e;
            node.right = delete(node.right, miniNode.e);

        }else if(e.compareTo(node.e) < 0){
            node.left = delete(node.left, e);
        }else if(e.compareTo(node.e) > 0 ){
            node.right = delete(node.right, e);
        }
        return node;


    }


    public static void main(String[] args) {
        BST<Integer> bst = new BST<>();

        int [] nums = {5,3, 6, 8, 4, 2};
        for (int num: nums){
            bst.add(num);
        }
        bst.preOrderNR();
        bst.delete(3);
        bst.preOrderNR();
        bst.levelOrder();
        System.out.println(bst);

//
//        System.out.println(bst.contains(7));
//        System.out.println(bst.contains(3));
//
//        bst.preOrder();
//        System.out.println("\n"+bst.toString());
//
//        bst.inOrder();
//        bst.postOrder();
//
//        bst.preOrderNR();
//        Random random = new Random();
//        int n = 100;
//        for (int i = 0;i< n; i++){
//            bst.add(random.nextInt(10000));
//        }
//
//        ArrayList<Integer> nums = new ArrayList<>();
//        while(! bst.isEmpty()){
//            nums.add(bst.removeMin());
//        }
//
//        System.out.println(nums);
//        for(int i=1; i< nums.size(); i++ ){
//            if(nums.get(i-1) > nums.get(i)){
//                throw new IllegalArgumentException("Error");
//            }
//        }
//        System.out.println("remove MIN test success.");

    }
}
