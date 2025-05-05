import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.util.ArrayDeque;


public class CF1997D {
    
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int t = fs.nextInt();
        while (t-- > 0) {
            int n = fs.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = fs.nextLong();
            int[] b = fs.readArray(n - 1);
            List<List<Integer>> adj = new ArrayList<>();
            for (int i = 1; i <= n; i++)
                adj.add(new ArrayList<>());
            for (int i = 1; i < n; i++)
                adj.get(b[i - 1] - 1).add(i);

            long lo = 0, hi = 2_000_000_001L;
            while (lo <= hi) {
                long mid = (lo + hi) / 2;
                if (check(mid, a, adj)) lo = mid + 1;
                else hi = mid - 1;
            }
            out.println(hi);
        }
        out.close();
    }

    static boolean check(long m, long[] a, List<List<Integer>> g) {
        Deque<long[]> deque = new ArrayDeque<>();
        deque.add(new long[] {0, Math.max(0, m - a[0])});

        while (!deque.isEmpty()) {
            long[] current = deque.pollLast();
            int i = (int) current[0];
            long pre = current[1];

            if (g.get(i).isEmpty()) {
                if (a[i] < pre) {
                    return false;
                }
                continue;
            }
            if (pre > 1e9) {
                return false;
            }

            for (int j : g.get(i)) {
                long nextPre = pre - Math.min(0, a[j] - pre);
                deque.add(new long[] {j, nextPre});
            }
        }
        return true;
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
    
    static long[] factorials = new long[2_000_001];
    static long[] invFactorials = new long[2_000_001];
    
    static void preCalFacts() {
        factorials[0] = 1;
        for (int i = 1; i < factorials.length; i++)
            factorials[i] = mul(factorials[i - 1], i);
        invFactorials[factorials.length - 1] = exp(factorials[factorials.length - 1], MOD1 - 2);
        for (int i = invFactorials.length - 2; i >= 0; i--)
            invFactorials[i] = mul(invFactorials[i + 1], i + 1);
    }
    
    static long comb(int n, int k) {
        return mul(factorials[n], mul(invFactorials[k], invFactorials[n - k]));
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
