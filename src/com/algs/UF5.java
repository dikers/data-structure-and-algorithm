package com.algs;

import com.algs.std.StdOut;
import com.algs.std.Stopwatch;
import com.algs.std.StopwatchCPU;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class UF5 {

    private int[] parent;
    private int count;
    private int[] rank; // 各个根节点所对应的分量的大小

    public UF5(int N){
        count = N;
        parent = new int[N];
        rank = new int[N];
        for(int i=0; i< N; i++){
            parent[i] = i;
            rank[i] = 1;
        }

    }

    public int count(){
        return count;
    }

    public boolean connected(int p, int q){
        return find(p) == find(q);
    }
    public void union(int p , int q){
        int i = find(p);
        int j = find(q);

        if(i == j){
            return ;
        }

        if (rank[i]< rank[j]){
            parent[i] = j;
        }else if(rank[j] < rank[i]){
            parent[j] = i;
        }else {
            parent[i] = j;
            rank[i] ++ ;
        }

        count --;
    }

    public int find(int p ){
//        while(p != parent[p]){
//            parent[p] = parent[parent[p]];
//            p = parent[p];
//        }
//        return p;

        if(p != parent[p]){
            parent[p] = find(parent[p]);
        }
        return parent[p];

    }

    @Override
    public String toString() {
        return "UF{" +
                "id=" + Arrays.toString(parent) +
                ", count=" + count +
                '}';
    }

    public static void main(String[] args) {

        try {
            BufferedReader in = new BufferedReader(new FileReader("./data/mediumUF.txt"));
            String str;
            int N = 0;
            StopwatchCPU stopwatch = new StopwatchCPU();
            str = in.readLine();
            N = Integer.valueOf(str);
            UF5 uf = new UF5(N);

            while ((str = in.readLine()) != null) {
                String arr[] = str.split(" ");
                int p = Integer.valueOf(arr[0]);
                int q = Integer.valueOf(arr[1]);
                System.out.println(p+", "+ q);
                uf.union(p, q);

            }
            StdOut.print(stopwatch.elapsedTime());
            StdOut.println(uf.count() + " components. ");
            StdOut.println(uf);
        } catch (IOException e) {
        }


    }
}
