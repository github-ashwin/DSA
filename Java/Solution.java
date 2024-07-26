import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int a,b,sum=0;
        a = in.nextInt();
        b = in.nextInt();
        sum = solveMeFirst(a,b);
        System.out.println(sum);
    }
    
    public static int solveMeFirst(int a, int b)
        {
            if(((1<=a)&&(a<=1000))&&((1<=b)&&(b<=1000)))
            {
                return a+b;
            }
            else
                return 0;
            
        }
}
