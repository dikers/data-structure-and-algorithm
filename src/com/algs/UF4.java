package com.algs;

import com.algs.std.StdOut;
import com.algs.std.Stopwatch;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class UF4 {

    private int[] id;
    private int count;
    private int[] rank; // 各个根节点所对应的分量的大小

    public UF4(int N){
        count = N;
        id = new int[N];
        rank = new int[N];
        for(int i=0; i< N; i++){
            id[i] = i;
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
            id[i] = j;
        }else if(rank[j] < rank[i]){
            id[j] = i;
        }else {
            id[i] = j;
            rank[i] ++ ;
        }

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
        Stopwatch stopwatch = new Stopwatch();
        try {
            BufferedReader in = new BufferedReader(new FileReader("./data/mediumUF.txt"));
            String str;
            int N = 0;

            str = in.readLine();
            N = Integer.valueOf(str);
            UF4 uf = new UF4(N);

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

        StdOut.print(stopwatch.elapsedTime());
    }
}
