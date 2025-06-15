import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class CF644B {
    
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int n = fs.nextInt();
        int b = fs.nextInt();
        long[] ans = new long[n];
        Deque<Long> dq = new ArrayDeque<>();
        Arrays.fill(ans, -1);
        for (int i = 0; i < n; i++) {
            int t = fs.nextInt();
            int d = fs.nextInt();
            while (!dq.isEmpty() && dq.peekFirst() <= t)
                dq.pollFirst();
            if (dq.size() <= b) {
                if (dq.isEmpty())
                    ans[i] = t + d;
                else {
                    ans[i] = dq.peekLast() + d;
                    
                }
                dq.addLast(ans[i]);
            }
        }
        StringJoiner sj = new StringJoiner(" ");
        for (long x : ans)
            sj.add(String.valueOf(x));
        out.println(sj);
        out.close();
    }
    
    static final int MOD1 = 1000000007;
    static final int MOD9 = 998244353;
    static final Random RD = new Random();
    
    static final int[][] D4 = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    static final int[][] D8 = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    static final String Y = "YES";
    static final String N = "NO";
    static final String A = "Alice";
    static final String B = "Bob";
    
    static long add(long a, long b) {
        return (a + b) % MOD1;
    }
    
    static long sub(long a, long b) {
        return ((a - b) % MOD1 + MOD1) % MOD1;
    }
    
    static long mul(long a, long b) {
        return (a * b) % MOD1;
    }
    
    static long exp(long base, long exp) {
        if (exp == 0)
            return 1;
        long half = exp(base, exp / 2);
        if (exp % 2 == 0)
            return mul(half, half);
        return mul(half, mul(half, base));
    }
    
    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
