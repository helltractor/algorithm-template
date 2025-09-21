import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Random;
import java.util.StringTokenizer;

public class D2 {

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0, t = fs.nextInt(); i < t; i++) {
            int n = fs.nextInt();
            int[] a = fs.readArray(n);
            RangeAddRangeSum2D tree = new RangeAddRangeSum2D(n + 2, n + 2);
            tree.rangeAdd(1, 1, 1, 1, 1);
            for (int x : a) {
                for (int l = x + 1; l <= n; l++) {
                    long res = tree.rangeQuery(l, 1, l, x);
                    tree.rangeAdd(l, x, l, x, res % MOD1);
                }
                for (int r = 1; r <= x; r++) {
                    long res = tree.rangeQuery(r, r, x, r);
                    tree.rangeAdd(x, r, x, r, res % MOD1);
                }
            }
            long ans = tree.rangeQuery(1, 1, n + 1, n + 1);
            out.println(ans % MOD1);
        }
        out.close();
    }

    static class RangeAddRangeSum2D {

        private int m; // row
        private int n; // col
        private long[][] t1;
        private long[][] t2;
        private long[][] t3;
        private long[][] t4;

        public RangeAddRangeSum2D(int m, int n) {
            this.m = m;
            this.n = n;
            this.t1 = new long[m + 1][n + 1];
            this.t2 = new long[m + 1][n + 1];
            this.t3 = new long[m + 1][n + 1];
            this.t4 = new long[m + 1][n + 1];
        }

        private void add(int x, int y, long val) {
            int i = x;
            while (i <= m) {
                int j = y;
                while (j <= n) {
                    t1[i][j] += val;
                    t2[i][j] += val * x;
                    t3[i][j] += val * y;
                    t4[i][j] += val * x * y;
                    j += (j & -j);
                }
                i += (i & -i);
            }
        }

        public void rangeAdd(int x1, int y1, int x2, int y2, long val) {
            add(x1, y1, val);
            add(x1, y2 + 1, -val);
            add(x2 + 1, y1, -val);
            add(x2 + 1, y2 + 1, val);
        }

        private long query(int x, int y) {
            assert 0 <= x && x <= m && 0 <= y && y <= n;
            long res = 0;
            int i = x;
            while (i > 0) {
                int j = y;
                while (j > 0) {
                    res += (x + 1L) * (y + 1L) * t1[i][j] - (y + 1L) * t2[i][j] - (x + 1L) * t3[i][j] + t4[i][j];
                    j -= (j & -j);
                }
                i -= (i & -i);
            }
            return res;
        }

        public long rangeQuery(int x1, int y1, int x2, int y2) {
            return query(x2, y2) - query(x2, y1 - 1) - query(x1 - 1, y2) + query(x1 - 1, y1 - 1);
        }
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
        if (exp == 0) {
            return 1;
        }
        long half = exp(base, exp / 2);
        if (exp % 2 == 0) {
            return mul(half, half);
        }
        return mul(half, mul(half, base));
    }

    static long[] factorials = new long[2_000_001];
    static long[] invFactorials = new long[2_000_001];

    static void preCalFacts() {
        factorials[0] = 1;
        for (int i = 1; i < factorials.length; i++) {
            factorials[i] = mul(factorials[i - 1], i);
        }
        invFactorials[factorials.length - 1] = exp(factorials[factorials.length - 1], MOD1 - 2);
        for (int i = invFactorials.length - 2; i >= 0; i--) {
            invFactorials[i] = mul(invFactorials[i + 1], i + 1);
        }
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
            for (int i = 0; i < n; i++) {
                a[i] = nextInt();
            }
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

}
