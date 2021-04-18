package com.algs;

import com.algs.std.In;
import com.algs.std.StdIn;
import com.algs.std.StdOut;
import com.algs.std.Stopwatch;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class UF {

    private int[] id;
    private int count;

    public UF(int N){
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
        int pID = find(p);
        int qID = find(q);
        if(pID == qID){
            return;
        }
        for (int i=0; i< id.length; i++){
            if(id[i] == pID){
                id[i] = qID;
            }
        }
        count --;
    }

    public int find(int p ){
        return id[p];
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
            BufferedReader in = new BufferedReader(new FileReader("./data/tinyUF.txt"));
            String str;
            int N = 0;

            str = in.readLine();
            N = Integer.valueOf(str);
            UF uf = new UF(N);

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
