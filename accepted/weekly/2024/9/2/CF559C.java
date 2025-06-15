import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class CF559C {
    
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        preCalFacts();
        int h = fs.nextInt(), w = fs.nextInt(), n = fs.nextInt();
        int[][] g = new int[n + 1][2];
        for (int i = 0; i < n; i++) {
            g[i][0] = fs.nextInt();
            g[i][1] = fs.nextInt();
        }
        g[n][0] = h;
        g[n][1] = w;
        Arrays.sort(g, Comparator.comparing((int[] x) -> x[0]).thenComparing(x -> x[1]));
        List<Long> ans = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            ans.add(comb(g[i][0] + g[i][1] - 2, g[i][0] - 1));
            for (int j = 0; j < i; j++) {
                if (g[j][1] <= g[i][1])
                    ans.set(i, sub(ans.get(i), mul(ans.get(j), comb(g[i][0] - g[j][0] + g[i][1] - g[j][1], g[i][0] - g[j][0]))));
            }
        }
        out.println(ans.get(n));
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
