import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;


public class CF1857F {
    
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int t = fs.nextInt();
        while (t-- > 0) {
            int n = fs.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = fs.nextLong();
            Map<Long, Integer> map = new HashMap<>();
            for (var x : a) {
                map.put(x, map.getOrDefault(x, 0) + 1);
            }
            int q = fs.nextInt();
            long[] ans = new long[q];
            for (int i = 0; i < q; i++) {
                long x = fs.nextLong(), y = fs.nextLong();
                long z = x * x - 4 * y;
                if (z < 0) {
                    continue;
                } else {
                    long sqrt = (long) Math.sqrt(z);
                    if (sqrt * sqrt != z) {
                        continue;
                    } else {
                        long b = (x + sqrt) / 2, c = (x - sqrt) / 2;
                        if (b == c) {
                            ans[i] = (long) map.getOrDefault(b, 0) * (map.getOrDefault(b, 0) - 1) / 2;
                        } else {
                            ans[i] = (long) map.getOrDefault(b, 0) * map.getOrDefault(c, 0);
                        }
                    }
                }
            }
            StringJoiner sj = new StringJoiner(" ");
            for (var x : ans) {
                sj.add(String.valueOf(x));
            }
            out.println(sj.toString());
        }
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
