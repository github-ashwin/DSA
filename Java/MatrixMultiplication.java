import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner in = new Scanner(System.in);
        
        int t = in.nextInt();
        
        for (int testCase = 0; testCase < t; testCase++) {
            int n = in.nextInt();
            
            int A[][] = new int[n][n];
            int B[][] = new int[n][n];
            int C[][] = new int[n][n];
            
            for (int row = 0; row < n; row++) {
                for (int col = 0; col < n; col++) {
                    A[row][col] = in.nextInt();
                }
            }
            
            for (int row = 0; row < n; row++) {
                for (int col = 0; col < n; col++) {
                    B[row][col] = in.nextInt();
                }
            }
            
            for (int row = 0; row < n; row++) {
                for (int col = 0; col < n; col++) {
                    for (int k = 0; k < n; k++) {
                        C[row][col] += A[row][k] * B[k][col];
                    }
                }
            }
            
            for (int row = 0; row < n; row++) {
                for (int col = 0; col < n; col++) {
                    System.out.print(C[row][col] + " ");
                }
            }
            
            System.out.println();
        }
    }
}