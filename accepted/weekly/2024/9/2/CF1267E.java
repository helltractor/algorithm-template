import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class CF1267E {
    
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int n = fs.nextInt(), m = fs.nextInt();
        int[][] grid = new int[m][n];
        for (int i = 0; i < m; i++)
            grid[i] = fs.readArray(n);

        int ans = 0, idx = n - 1;
        for (int i = 0; i < n - 1; i++) {
            int[] diff = new int[m];
            for (int j = 0; j < m; j++) {
                diff[j] = grid[j][n - 1] - grid[j][i];
            }
            Arrays.sort(diff);
            int cur = 0;
            for (int j = 0; j < m; j++) {
                cur += diff[j];
                if (cur > 0)
                    break;
                if (j + 1 > ans) {
                    ans = j + 1;
                    idx = i;
                }
            }
        }
        out.println(m - ans);
        final int finalIdx = idx;
        out.println(IntStream.range(1, m + 1)
            .boxed()
            .sorted(Comparator.comparingInt(x -> grid[x - 1][n - 1] - grid[x - 1][finalIdx]))
            .skip(ans)
            .map(String::valueOf)
            .collect(Collectors.joining(" ")));
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
