package com.algs;

import com.algs.std.StdOut;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class UF2 {

    private int[] id;
    private int count;

    public UF2(int N){
        count = N;
        id = new int[N];
        for(int i=0; i< N; i++){
            id[i] = i;
        }
    }

    public int count(){
        return count;
    }

    public boolean connected(int p, int q){
        return find(p) == find(q);
    }
    public void union(int p , int q){

        int pRoot = find(p);
        int qRoot = find(q);
        if(pRoot == qRoot){
            return;
        }
        id[pRoot] = qRoot;
        count --;
    }

    public int find(int p ){
        while(p != id[p]){
            p = id[p];
        }
        return p;
    }

    @Override
    public String toString() {
        return "UF{" +
                "id=" + Arrays.toString(id) +
                ", count=" + count +
                '}';
    }

    public static void main(String[] args) {
        try {
            BufferedReader in = new BufferedReader(new FileReader("./data/tinyUF.txt"));
            String str;
            int N = 0;

            str = in.readLine();
            N = Integer.valueOf(str);
            UF2 uf = new UF2(N);

            while ((str = in.readLine()) != null) {
                String arr[] = str.split(" ");
                int p = Integer.valueOf(arr[0]);
                int q = Integer.valueOf(arr[1]);
                System.out.println(p+", "+ q);
                uf.union(p, q);

            }

            StdOut.println(uf.count() + " components. ");
            StdOut.println(uf);
        } catch (IOException e) {
        }
    }
}
